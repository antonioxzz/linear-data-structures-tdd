
conversion_units = {
    "meters": {"foott": 3.28084, "inches": 39.3701},
    "foot": {"meters": 0.3048, "inches": 12},
    "inches": {"meters": 0.0254, "foot": 0.0833333}
}


def convert_a_unit_value_to_other_unit_value(
        input_number: float,
        origin_unit: str,
        target_unit: str,
):
    conversion_factor = conversion_units[origin_unit][target_unit]
    target_number = input_number * conversion_factor
    return target_number

target_number: float = convert_a_unit_value_to_other_unit_value(1, "meters", "foott")
print (target_number)
    