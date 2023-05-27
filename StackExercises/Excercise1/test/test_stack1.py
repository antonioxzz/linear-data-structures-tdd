import pytest
from stack1.stack1 import are_parentheses_balanced


@pytest.mark.parametrize("expression, expected", [
    ("()", True),
    ("()[]{}", True),
    ("({[]})", True),
    ("(", False),
    ("[)", False),
    ("(]", False),
    ("([)]", False),
    ("{[}]", False),
    ("[{)]}", False),
])
def test_are_parentheses_balanced(expression, expected):
    result = are_parentheses_balanced(expression)
    assert result == expected
    