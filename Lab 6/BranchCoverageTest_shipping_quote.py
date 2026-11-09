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


def test_invalid_type():
    with pytest.raises(ValueError):
        process_shipments("abc", 5)


def test_negative_fee():
    with pytest.raises(ValueError):
        process_shipments([], -1)


def test_empty_shipments():
    assert process_shipments([], 5)["status"] == "NO_CARGO"


def test_unapproved():
    assert process_shipments([ship(manifest_approved=False)], 5)["status"] == "NO_CARGO"


def test_missing_manifest():
    assert process_shipments([{"mode": "air"}], 5)["status"] == "NO_CARGO"


def test_default_mode():
    s = {"manifest_approved": True, "packages": [{"weight_kg": 10}]}
    assert process_shipments([s], 0)["total_quote"] == 40.0


def test_unknown_mode():
    assert process_shipments([ship(mode="sea")], 5)["status"] == "NO_CARGO"


def test_air_normal():
    assert process_shipments([ship(mode="air")], 0)["total_quote"] == 120.0


def test_ground_normal():
    assert process_shipments([ship()], 0)["total_quote"] == 40.0


def test_ground_exactly_30():
    s = ship(packages=[{"weight_kg": 30}])
    assert process_shipments([s], 0)["total_quote"] == 120.0


def test_ground_heavy():
    s = ship(packages=[{"weight_kg": 31}])
    assert process_shipments([s], 0)["total_quote"] == 186.0


def test_air_heavy_express():
    s = ship(mode="air", express_priority=True,
             packages=[{"weight_kg": 40}])
    assert process_shipments([s], 10)["total_quote"] == 912.5


def test_zero_weight():
    s = ship(packages=[{"weight_kg": 0}])
    assert process_shipments([s], 5)["total_quote"] == 5.0


def test_negative_weight():
    s = ship(packages=[{"weight_kg": -2}])
    assert process_shipments([s], 5)["total_quote"] == 5.0


def test_missing_weight():
    assert process_shipments([ship(packages=[{}])], 5)["total_quote"] == 5.0


def test_empty_packages():
    assert process_shipments([ship(packages=[])], 7)["total_quote"] == 7.0


def test_hazmat_not_fragile():
    s = ship(packages=[{"weight_kg": 5, "is_hazmat": True}])
    assert process_shipments([s], 10)["total_quote"] == 60.0


def test_hazmat_fragile_break():
    s = ship(is_fragile=True, packages=[
        {"weight_kg": 10},
        {"weight_kg": 5, "is_hazmat": True},
        {"weight_kg": 99}
    ])
    assert process_shipments([s], 10)["status"] == "NO_CARGO"


def test_fragile_without_hazmat():
    s = ship(is_fragile=True)
    assert process_shipments([s], 0)["total_quote"] == 40.0


def test_express_false_and_true():
    s = ship(express_priority=True)
    assert process_shipments([s], 0)["total_quote"] == 50.0


def test_three_rejections():
    s = ship(packages=[{"weight_kg": 0}] * 3)
    assert process_shipments([s], 5)["status"] == "CLEARED"


def test_four_rejections():
    s = ship(packages=[{"weight_kg": 0}] * 4)
    assert process_shipments([s], 5)["status"] == "FLAGGED_REVIEW"


def test_multiple_shipments():
    r = process_shipments([ship(), ship(mode="air")], 0)
    assert r["total_quote"] == 160.0


def test_pressure_none():
    assert monitor_container_pressures(None) == "NO_DATA"


def test_pressure_empty():
    assert monitor_container_pressures([]) == "NO_DATA"


def test_pressure_empty_container():
    assert monitor_container_pressures([[]]) == "STABLE"


def test_pressure_stable():
    assert monitor_container_pressures([[20, 20, 15]]) == "STABLE"


def test_pressure_reset():
    assert monitor_container_pressures([[13, 15, 13, 13]]) == "LEAK_DETECTED"


def test_pressure_leak():
    assert monitor_container_pressures([[15, 13, 12]]) == "LEAK_DETECTED"


def test_second_container_leak():
    assert monitor_container_pressures([[20, 20], [13, 12]]) == "LEAK_DETECTED"