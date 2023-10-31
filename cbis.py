from math import floor
import random, time, tracemalloc

def cbis(nums: list[int]):
    # Source: https://www.sciencedirect.com/science/article/abs/pii/S0167739X17318423
    pop = 0
    for i in range(1, len(nums)):
        cop = i
        key = nums[cop]
        if key >= nums[pop]:
            place = binary_loc_finder(nums, pop + 1, cop - 1, key)
        else:
            place = binary_loc_finder(nums, 0, pop - 1, key)
        pop = place
        nums = place_inserter(nums, pop, cop)
    
    return nums


def binary_loc_finder(nums, start, end, key):
    # Source: https://www.sciencedirect.com/science/article/abs/pii/S0167739X17318423
    if start == end:
        if nums[start] > key:
            loc = start
            return loc
        else:
            loc = start + 1
            return loc
        
    if start > end:
        loc = start
        return loc
    else:
        middle = floor((start + end) / 2)
        if nums[middle] < key:
            return binary_loc_finder(nums, middle + 1, end, key)
        elif nums[middle] > key:
            return binary_loc_finder(nums, start, middle - 1, key)
        else:
            return middle

def place_inserter(nums, start, end):
    # Source: https://www.sciencedirect.com/science/article/abs/pii/S0167739X17318423
    temp = nums[end]
    for k in range(end, start - 1, -1):
        nums[k] = nums[k - 1]
    nums[start] = temp
    return nums

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
    cbis(sorted)
    end = time.time()
    sorted_time = (end - start) * 1000

    start = time.time()
    cbis(random)
    end = time.time()
    random_time = (end - start) * 1000

    start = time.time()
    cbis(reversed)
    end = time.time()
    reversed_time = (end - start) * 1000

    print(f'Sorted list time for CBIS (n = {n}): {sorted_time}')
    print(f'Random list time for CBIS (n = {n}): {random_time}')
    print(f'Reversed list time for CBIS (n = {n}): {reversed_time}\n')

def get_memory_usage(n):
    sorted, random, reversed = generate_test_list(n)

    tracemalloc.start()
    cbis(sorted)
    print(f'Sorted memory usage for CBIS (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()

    tracemalloc.start()
    cbis(random)
    print(f'Random memory usage for CBIS (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()

    tracemalloc.start()
    cbis(reversed)
    print(f'Reversed memory usage for CBIS (n = {n}): {tracemalloc.get_traced_memory()}')
    tracemalloc.stop()


def verify_validity(n):
    sorted_list, random_list, reversed_list = generate_test_list(n)
    print(f'n = {n}')
    print(sorted(sorted_list) == cbis(sorted_list)) # Expected: True
    print(sorted(random_list) == cbis(random_list)) # Expected: True
    print(sorted(reversed_list) == cbis(reversed_list)) # Expected: True

get_elapsed_time(200)
get_elapsed_time(2000)
get_elapsed_time(20000)

get_memory_usage(200)
get_memory_usage(2000)
get_memory_usage(20000)
