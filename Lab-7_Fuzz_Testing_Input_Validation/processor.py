import json
import math


def calculate_dimensional_weight(dimensions_str):
    """Return dimensional weight (kg) for 'LxWxH' in cm, or None if invalid."""
    if not isinstance(dimensions_str, str):
        return None
    dims = dimensions_str.strip().split('x')
    if len(dims) != 3:
        return None
    try:
        length, width, height = (float(d) for d in dims)
        if not all(math.isfinite(v) and v > 0 for v in (length, width, height)):
            return None
        result = (length * width * height) / 5000.0
        if not math.isfinite(result):
            return None
        return round(result, 2)
    except (ValueError, TypeError, OverflowError):
        return None


def format_tracking_label(raw_code):
    """Turn e.g. 'e123' into 'E-000123', or return None if invalid."""
    if not isinstance(raw_code, str) or len(raw_code) < 2:
        return None
    prefix = raw_code[0]
    digits = raw_code[1:]
    if not (prefix.isascii() and prefix.isalpha()):
        return None
    if not (digits.isascii() and digits.isdigit()):
        return None
    try:
        tracking_num = int(digits)
    except ValueError:  # e.g. absurdly long digit strings
        return None
    return f"{prefix.upper()}-{tracking_num:06d}"


def parse_package_manifest(json_payload):
    """Return the manifest weight as a float, or None if invalid."""
    if not isinstance(json_payload, (str, bytes, bytearray)):
        return None
    try:
        data = json.loads(json_payload)
        if not isinstance(data, dict) or "weight" not in data:
            return None
        raw_weight = data["weight"]
        if isinstance(raw_weight, bool):
            return None
        weight = float(raw_weight)
        if not math.isfinite(weight) or weight < 0:
            return None
        return weight
    except (ValueError, TypeError, OverflowError, RecursionError):
        # ValueError covers json.JSONDecodeError and UnicodeDecodeError
        return None


def main():
    print("==== Running calculate_dimensional_weight ====")
    dims_input = input("Enter dimensions LxWxH in cm (e.g. 20x30x10): ")
    dim_weight = calculate_dimensional_weight(dims_input)
    if dim_weight is None:
        print("Invalid dimensions. Use format LxWxH with positive numbers.")
    else:
        print("Dimensional Weight (kg):", dim_weight)

    print("\n==== Running format_tracking_label ====")
    code_input = input("Enter raw code (e.g. E123): ")
    label = format_tracking_label(code_input)
    if label is None:
        print("Invalid code. Use one letter followed by digits.")
    else:
        print("Formatted Label:", label)

    print("\n==== Running parse_package_manifest ====")
    json_input = input('Enter manifest JSON (e.g. {"weight": 12.5}): ')
    weight = parse_package_manifest(json_input)
    if weight is None:
        print("Invalid manifest. Expected JSON with a non-negative numeric 'weight'.")
    else:
        print("Manifest Weight:", weight)


if __name__ == "__main__":
    main()
