import numpy as np
import random
np_arr = np.random.randint(0, 20, (5, 5)).astype(float)

print(np_arr)
for i in range(5):
    for j in range(5):
        a = random.randint(0, 20)
        if np_arr[i][j] == a:
            np_arr[i][j] = np.nan
print(np_arr)
row_means = np.nanmean(np_arr, axis=1)
for i in range(5):
    print(f"Для строки {i+1} среднее значение = {row_means[i]}")