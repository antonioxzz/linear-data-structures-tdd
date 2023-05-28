import pytest
from queue2.queue2 import merge_sort_queue


@pytest.mark.parametrize("numbers, expected", [
    ([4, 2, 9, 6, 1, 7, 3, 5, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, 5, 2, 7, 1], [1, 2, 5, 7, 9]),
    ([3, 1, 4, 2], [1, 2, 3, 4]),
    ([1], [1]),
    ([], []),
])
def test_merge_sort_queue(numbers, expected):
    result = merge_sort_queue(numbers)
    assert result == expected
    