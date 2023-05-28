from queue import Queue


def merge_sort_queue(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    left_half_sorted = merge_sort_queue(left_half)
    right_half_sorted = merge_sort_queue(right_half)

    merged_queue = merge_queues(left_half_sorted, right_half_sorted)

    sorted_numbers = list(merged_queue.queue)
    return sorted_numbers


def merge_queues(queue1, queue2):
    merged_queue = Queue()

    while not queue1.empty() and not queue2.empty():
        if queue1.queue[0] <= queue2.queue[0]:
            merged_queue.put(queue1.get())
        else:
            merged_queue.put(queue2.get())

    while not queue1.empty():
        merged_queue.put(queue1.get())

    while not queue2.empty():
        merged_queue.put(queue2.get())

    return merged_queue
