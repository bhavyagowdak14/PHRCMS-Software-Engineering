import pytest
from shipping_quote import process_shipments, monitor_container_pressures


def ship(**kw):
    d = {
        "manifest_approved": True,
        "mode": "ground",
        "is_fragile": False,
        "express_priority": False,
        "packages": [{"weight_kg": 10, "is_hazmat": False}]
    }
    d.update(kw)
    return d


def test_ground_shipment():
    assert process_shipments([ship()], 20.0) == {
        "total_quote": 60.0, "status": "CLEARED"
    }


def test_air_shipment():
    assert process_shipments([ship(mode="air")], 0)["total_quote"] == 120.0


def test_air_heavy_express():
    s = ship(mode="air", express_priority=True,
             packages=[{"weight_kg": 40}])
    assert process_shipments([s], 10)["total_quote"] == 912.5


def test_ground_heavy():
    s = ship(packages=[{"weight_kg": 31}])
    assert process_shipments([s], 0)["total_quote"] == 186.0


def test_unapproved():
    assert process_shipments([ship(manifest_approved=False)], 5) == {
        "total_quote": 0.0, "status": "NO_CARGO"
    }


def test_unknown_mode():
    assert process_shipments([ship(mode="sea")], 5)["status"] == "NO_CARGO"


def test_invalid_shipments():
    with pytest.raises(ValueError):
        process_shipments("abc", 5)


def test_negative_fee():
    with pytest.raises(ValueError):
        process_shipments([], -1)


def test_zero_weight():
    s = ship(packages=[{"weight_kg": 0}])
    assert process_shipments([s], 5)["total_quote"] == 5.0


def test_negative_weight():
    s = ship(packages=[{"weight_kg": -5}])
    assert process_shipments([s], 5)["total_quote"] == 5.0


def test_missing_weight():
    s = ship(packages=[{}])
    assert process_shipments([s], 5)["total_quote"] == 5.0


def test_empty_packages():
    assert process_shipments([ship(packages=[])], 7)["total_quote"] == 7.0


def test_hazmat():
    s = ship(packages=[{"weight_kg": 5, "is_hazmat": True}])
    assert process_shipments([s], 10)["total_quote"] == 60.0


def test_hazmat_fragile():
    s = ship(is_fragile=True, packages=[
        {"weight_kg": 10},
        {"weight_kg": 5, "is_hazmat": True}
    ])
    assert process_shipments([s], 10)["status"] == "NO_CARGO"


def test_flagged_review():
    s = ship(packages=[{"weight_kg": 0}] * 4)
    assert process_shipments([s], 5)["status"] == "FLAGGED_REVIEW"


def test_multiple_shipments():
    r = process_shipments([
        ship(),
        ship(manifest_approved=False),
        ship(mode="air")
    ], 0)
    assert r["total_quote"] == 160.0


def test_pressure_no_data():
    assert monitor_container_pressures([]) == "NO_DATA"


def test_pressure_leak():
    assert monitor_container_pressures([[15, 13, 12]]) == "LEAK_DETECTED"


def test_pressure_stable():
    assert monitor_container_pressures([[15, 13, 15, 13, 15]]) == "STABLE"