from math import floor
import random, time, tracemalloc, sys
from util import generate_test_list, parse_list

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

def get_elapsed_time(n):
    print('Calculating elapsed time for CBIS...')
    
    EPOCH = 10
    types = ['sorted', 'random', 'reversed']
    
    for type in types:
        sum = 0
        for i in range(EPOCH):
            lst = parse_list(n, type)
            start = time.time()
            cbis(lst)
            end = time.time()
            current_time = (end - start) * 1000
            sum += current_time
        avg = sum / EPOCH
        print(f'Average sorting time for CBIS (n = {n}, input type = {type}): {avg} ms')
        
def get_memory_usage(n):
    print(f'Calculating memory usage for CBIS (n = {n})...')
    
    types = ['sorted', 'random', 'reversed']
    for type in types:
        lst = parse_list(n, type)
        print(f'Memory usage (array input type = {type}):')
        tracemalloc.start()
        cbis(lst)
        current_size, peak_size = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{current_size=}, {peak_size=} (in bytes)")
        print('-------------------------------------------')

def verify_validity(n):
    print(f'Verifying CBIS sorting algorithm correctness (n = {n})...')
    types = ['sorted', 'random', 'reversed']
    for type in types:
        lst = parse_list(n, type)
        print(f'Is correctly sorted for array input type of {type}: {sorted(lst) == cbis(lst)}') # Expected: True

def calculate_cbis_performance():
    ns = [200, 2000, 20000]
    for n in ns:
        print(f'Performance for n = {n}:')
        verify_validity(n)
        print('\n')
        get_elapsed_time(n)
        print('\n')
        get_memory_usage(n)
        print('\n')
        print(f'Calculation complete for n = {n}')
        print('-------------------------------------------')

    print('===' * 50)
    print('Performance calculation complete.')