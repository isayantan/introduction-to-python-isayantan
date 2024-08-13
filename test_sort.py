import random
import time

N = 100
random.seed(int(time.time()))

def insertion_sort(unsorted_list: list[int]) -> list[int]:
    # Implement your function here ...
    raise NotImplementedError

# Do not change the following lines
def test_insertion_sort():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = insertion_sort(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"

def test_reference():
    input_list = list(range(N))
    random.shuffle(input_list)
    output_list = sorted(input_list)
    assert output_list == sorted(output_list), "Input list is not sorted"
