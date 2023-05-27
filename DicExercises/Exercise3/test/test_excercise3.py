import pytest
from dic3.excercise3 import calculate_average_student, calculate_class_average


data_to_test = [
    {
        "grades": {"Italo": [8, 9, 10], "Antonio": [7, 6, 5], "Javier": [10, 10, 10]},
        "expected_average": {"Italo": 9, "Antonio": 6, "Javier": 10}
    },
]


@pytest.mark.parametrize("input_grade, expected", [
    (data["grades"], data["expected_average"]) for data in data_to_test
])
def test__calculate_average_student__return_a_dict_when_a_grade_is_entered(input_grade, expected):
    result = calculate_average_student(input_grade)
    assert result == expected


def test_calculate_class_average():
    for data in data_to_test:
        result = calculate_class_average(data["grades"])
        expected = data["expected_average"]
        assert result == expected
