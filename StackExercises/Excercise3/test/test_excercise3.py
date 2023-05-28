import pytest
from stack3.excercise3 import reverse_string

def test__reverse_string__returns_reversed_string__when_given_input_string():
    test_cases = [
        ("Hello World", "olleH"),
        ("Python", "nohtyP"),
        ("12345", "54321"),
        ("", ""),
    ]
    
    for input_string, expected_output in test_cases:
        assert reverse_string(input_string) == expected_output
