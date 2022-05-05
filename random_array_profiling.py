import random
import numpy as np


def generate_random_array_python(size):
    return [random.randint(0, 10) for i in range(0, size)]

def generate_random_array_numpy(size):
    return np.random.randint(low=0, high=10, size=(size,))

random_array = generate_random_array_python(100) 

if __name__ == "__main__":

    size = 1000
    
    generate_random_array_python(size)

    generate_random_array_numpy(size)
