import random, time, tracemalloc
from util import parse_list

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

def get_elapsed_time(n):
    print('Calculating elapsed time for Randomized Quick Sort...')
    
    EPOCH = 10
    types = ['sorted', 'random', 'reversed']
    
    for type in types:
        sum = 0
        for i in range(EPOCH):
            lst = parse_list(n, type)
            start = time.time()
            rqs(lst, 0, len(lst) - 1)
            end = time.time()
            current_time = (end - start) * 1000
            sum += current_time
        avg = sum / EPOCH
        print(f'Average sorting time for Randomized Quick Sort (n = {n}, input type = {type}): {avg} ms')
        
def get_memory_usage(n):
    print(f'Calculating memory usage for Randomized Quick Sort (n = {n})...')
    
    types = ['sorted', 'random', 'reversed']
    for type in types:
        lst = parse_list(n, type)
        print(f'Memory usage (array input type = {type}):')
        tracemalloc.start()
        rqs(lst, 0, len(lst) - 1)
        current_size, peak_size = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{current_size=}, {peak_size=} (in bytes)")
        print('-------------------------------------------')

def verify_validity(n):
    print(f'Verifying Randomized Quick Sort algorithm correctness (n = {n})...')
    types = ['sorted', 'random', 'reversed']
    for type in types:
        lst = parse_list(n, type)
        print(f'Is correctly sorted for array input type of {type}: {sorted(lst) == rqs(lst, 0, len(lst) - 1)}') # Expected: True

def calculate_rqs_performance():
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