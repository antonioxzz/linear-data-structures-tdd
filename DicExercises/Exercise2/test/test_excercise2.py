import pytest
from dic2.excercise2 import convert_a_unit_value_to_other_unit_value

conversion_units = {
    "meters": {"foott": 3.28084, "inches": 39.3701},
    "foot": {"meters": 0.3048, "inches": 12},
    "inches": {"meters": 0.0254, "foot": 0.0833333}
}

data_to_test = [
    {
        "input_number": 1,
        "origin_unit": "meters",
        "target_unit": "foott",
        "expected": 3.28084,
    },
    {
        "input_number": 1,
        "origin_unit": "meters",
        "target_unit": "inches",
        "expected": 39.3701,
    },
    {
        "input_number": 1,
        "origin_unit": "foot",
        "target_unit": "meters",
        "expected": 0.3048,
    },
    {
        "input_number": 1,
        "origin_unit": "foot",
        "target_unit": "inches",
        "expected": 12,
    },
    {
        "input_number": 1,
        "origin_unit": "inches",
        "target_unit": "meters",
        "expected": 0.0254,
    },
    {
        "input_number": 1,
        "origin_unit": "inches",
        "target_unit": "foot",
        "expected": 0.0833333,
    },
]

@pytest.mark.parametrize("input_number, origin_unit, target_unit, expected", [
    (data["input_number"], data["origin_unit"], data["target_unit"], data["expected"]) for data in data_to_test
])
def test_convert_a_unit_value_to_other_unit_value_function_return_a_number_in_other_unit(
    input_number, origin_unit, target_unit, expected
):
    result = convert_a_unit_value_to_other_unit_value(input_number, origin_unit, target_unit)
    assert result == pytest.approx(expected, abs=1e-5)

