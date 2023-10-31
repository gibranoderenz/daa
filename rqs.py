import random, time, tracemalloc

def rqs(nums, left, right):
    # Source: https://scele.cs.ui.ac.id/pluginfile.php/195635/mod_resource/content/2/DAA-6-published.pdf
    if left < right:
        final_pivot_pos = randomized_partition(nums, left, right)
        rqs(nums, left, final_pivot_pos - 1)
        rqs(nums, final_pivot_pos + 1, right)

    return nums

def randomized_partition(nums, left, right):
    # Source: https://scele.cs.ui.ac.id/pluginfile.php/195635/mod_resource/content/2/DAA-6-published.pdf
    random_index = random.randint(left, right)

    temp = nums[random_index]
    nums[random_index] = nums[right]
    nums[right] = temp

    pivot = nums[right]
    last_filled = left - 1
    for i in range(left, right):
        if nums[i] <= pivot:
            last_filled += 1
            temp = nums[last_filled]
            nums[last_filled] = nums[i]
            nums[i] = temp
    last_filled += 1
    temp = nums[last_filled]
    nums[last_filled] = nums[right]
    nums[right] = temp
    return last_filled

def generate_random_list(n):
    # Source: https://www.tutorialspoint.com/generating-random-number-list-in-python
    random_test_list = []
    for _ in range(n):
        random_number = random.randint(1, n)
        random_test_list.append(random_number)
    return random_test_list

def generate_test_list(n):
    sorted_test_list = sorted(generate_random_list(n))
    random_test_list = generate_random_list(n)
    reversed_test_list = sorted(generate_random_list(n), reverse=True)
    
    return sorted_test_list, random_test_list, reversed_test_list

def get_elapsed_time(n):
    sorted, random, reversed = generate_test_list(n)

    start = time.time()
    rqs(sorted, 0, len(sorted) - 1)
    end = time.time()
    sorted_time = (end - start) * 1000

    start = time.time()
    rqs(random, 0, len(random) - 1)
    end = time.time()
    random_time = (end - start) * 1000

    start = time.time()
    rqs(reversed, 0, len(reversed) - 1)
    end = time.time()
    reversed_time = (end - start) * 1000

    print(f'Sorted list time for Randomized Quick Sort (n = {n}): {sorted_time}')
    print(f'Random list time for Randomized Quick Sort (n = {n}): {random_time}')
    print(f'Reversed list time for Randomized Quick Sort (n = {n}): {reversed_time}\n')

def get_memory_usage(n):
    sorted, random, reversed = generate_test_list(n)

    tracemalloc.start()
    rqs(sorted, 0, len(sorted) - 1)
    print(f'Sorted memory usage for Randomized Quick Sort (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()

    tracemalloc.start()
    rqs(random, 0, len(random) - 1)
    print(f'Random memory usage for Randomized Quick Sort (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()

    tracemalloc.start()
    rqs(reversed, 0, len(reversed) - 1)
    print(f'Reversed memory usage for Randomized Quick Sort (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()

def verify_validity(n):
    sorted_list, random_list, reversed_list = generate_test_list(n)
    print(f'n = {n}')
    print(sorted(sorted_list) == rqs(sorted_list, 0, len(sorted_list) - 1)) # Expected: True
    print(sorted(random_list) == rqs(random_list, 0, len(random_list) - 1)) # Expected: True
    print(sorted(reversed_list) == rqs(reversed_list, 0, len(reversed_list) - 1)) # Expected: True

get_elapsed_time(200)
get_elapsed_time(2000)
get_elapsed_time(20000)

get_memory_usage(200)
get_memory_usage(2000)
get_memory_usage(20000)