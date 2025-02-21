import numpy as np

def removeD(arr):
    return list(set(arr.tolist()))  # Convert NumPy array to a list before using set

a = np.array([1, 2, 44, 2, 1, 1, 4, 4, 2, 143, 2, 5, 6])
print(removeD(a))
