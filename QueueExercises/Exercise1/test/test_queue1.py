import pytest
from queue1.queue1 import simulate_supermarket_queue


@pytest.mark.parametrize("total_customers", [5, 10, 15])
def test_simulate_supermarket_queue(total_customers):
    result = simulate_supermarket_queue(total_customers)
    assert result == "all clients have been attended"
    