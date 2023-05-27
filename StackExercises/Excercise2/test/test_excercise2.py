import pytest
from stack2.excercise2 import evaluate_postfix


data_to_test = [
    {
        "expression": ['2', '3', '+', '4', '*'],
        "expected_result": 20,
    },
    {
        "expression": ['5', '6', '7', '+', '*'],
        "expected_result": 65,
    },
    {
        "expression": ['9', '8', '+', '7', '2', '+', '*'],
        "expected_result": 135,
    },
]

@pytest.mark.parametrize("expression, expected_result", [
    (data["expression"], data["expected_result"]) for data in data_to_test
])
def test_evaluate_postfix(expression, expected_result):
    result = evaluate_postfix(expression)
    assert result == expected_result
