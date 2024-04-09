import numpy as np
import time

def measure_python_array(max_size):
    start = time.time()
    python_list = [i for i in range(0, max_size)]
    end = time.time() - start

    print("Python list:\n", python_list[:5])
    print("Time:", end)

def measure_numpy_array(max_size):
    start = time.time()
    ### ENTER CODE HERE
    end = time.time() - start

    print("NumPy array:\n", )
    print("Time:", end)

def create_random_int_python_array(max_int, max_size):
    import random
    rand_arr = [random.randint(0, max_int) for _ in range(max_size)]
    return rand_arr

def create_random_int_python_multi_array(max_int, max_size, max_dim):
    import random
    rand_arr = [[random.randint(0, max_int) for _ in range(max_size)] for _ in range(max_dim)]
    return rand_arr

def create_random_float_python_array(max_float, max_size):
    import random
    rand_arr = [random.uniform(0, max_float) for _ in range(max_size)]
    return rand_arr

def create_random_int_numpy_array(max_int, max_size):
    import random
    rand_arr = np.random.randint(0, max_int, max_size)
    return rand_arr

def create_random_float_numpy_array(max_size, max_dim):
    import random
    rand_arr = np.random.rand(max_dim, max_size)
    return rand_arr