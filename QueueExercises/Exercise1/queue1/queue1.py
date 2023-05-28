import random
import time
import pytest

MIN_WAIT_TIME = 1
MAX_WAIT_TIME = 5


def simulate_supermarket_queue(total_customers):
    queue = []

    for customer in range(total_customers):
        queue.append(customer + 1)
        wait_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
        time.sleep(wait_time)
        queue.pop(0)

    return "all clients have been attended"
