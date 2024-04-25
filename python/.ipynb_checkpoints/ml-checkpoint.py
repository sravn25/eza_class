import random 
import numpy as np
from scipy import stats


def populate(num):
    arr = []
    for i in range(num):
        arr.append(random.randint(0,100))
    return arr

if __name__ == "__main__":
    arr = populate(100)
    print(arr)
    print("Mean: ", np.mean(arr))
    print("Median: ", np.median(arr))
    print("Mode: ", stats.mode(arr))
    print("Standard deviation: ", np.std(arr))
    print("90th Percentile: ", np.percentile(arr, 90))
    print("75th Percentile: ", np.percentile(arr, 75))
    print("50th Percentile: ", np.percentile(arr, 50))
