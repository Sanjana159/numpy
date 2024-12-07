import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [0, 2, 4]])

flattened = matrix1.ravel()

print("Flattened Array:", flattened)
