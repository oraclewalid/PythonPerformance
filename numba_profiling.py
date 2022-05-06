import random
import numpy as np
import numba as nb

def generate_random_array_python(size):
    array = [random.randint(0, 10) for i in range(0, size)]
    result = 0
    for i in range(size):
        result += array[i]
    return result

def generate_random_array_numpy(size):
    return np.sum(np.random.randint(low=0, high=10, size=(size,)))

@nb.jit(nopython=True)
def generate_random_array_numba(size):
    array = [random.randint(0, 10) for i in range(0, size)]
    result = 0
    for i in range(size):
        result += array[i]
    return result

if __name__ == '__main__':
    import timeit
    repeat = 5
    print(timeit.repeat("generate_random_array_python(10000)", setup="from __main__ import generate_random_array_python", number=repeat))
    print(timeit.repeat("generate_random_array_numpy(10000)", setup="from __main__ import generate_random_array_numpy", number=repeat))
    print(timeit.repeat("generate_random_array_numba(10000)", setup="from __main__ import generate_random_array_numba", number=repeat))
