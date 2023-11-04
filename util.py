import random
import linecache
import os
import tracemalloc

def generate_random_list(n):
    # Source: https://www.tutorialspoint.com/generating-random-number-list-in-python
    random_test_list = []
    MIN_VALUE = -10**8
    MAX_VALUE = 10**8
    for _ in range(n):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        random_test_list.append(random_number)
    return random_test_list

def generate_test_list(n):
    sorted_test_list = sorted(generate_random_list(n))
    random_test_list = generate_random_list(n)
    reversed_test_list = sorted(generate_random_list(n), reverse=True)
    
    return sorted_test_list, random_test_list, reversed_test_list

def generate_dataset():
    # Reference: https://stackoverflow.com/a/33686762
    ns = [200, 2000, 20000]
    for n in ns:
        sorted_list, random_list, reversed_list = generate_test_list(n)
        with open(f"./dataset/sorted-{n}.txt", "w") as file:
            for num in sorted_list:
                file.write(str(num) + '\n')

        with open(f"./dataset/random-{n}.txt", "w") as file:
            for num in random_list:
                file.write(str(num) + '\n')
        
        with open(f"./dataset/reversed-{n}.txt", "w") as file:
            for num in reversed_list:
                file.write(str(num) + '\n')

def parse_list(n, mode = 'sorted'):
    # mode = 'sorted' | 'random' | 'reversed'
    result = []
    with open(f"./dataset/{mode}-{n}.txt", "r") as file:
        for num in file:
            result.append(int(num))
    return result