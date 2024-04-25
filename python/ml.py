import random 
import numpy as np

from scipy import stats
from sklearn.metrics import r2_score

from matplotlib import pyplot as plt
from matplotlib import use

from tkinter import *

use('TkAgg')

def populate(num):
    arr = []
    for i in range(num):
        arr.append(random.randint(0,100))
    return arr

def populateBigData(num):
    return np.random.uniform(0.0, 10.0, num)

def populateNormal(num):
    return np.random.normal(5.0, 1.0, num)

def statistics(arr):
    print("Mean: ", np.mean(arr))
    print("Median: ", np.median(arr))
    print("Mode: ", stats.mode(arr))
    print("Standard deviation: ", np.std(arr))
    print("90th Percentile: ", np.percentile(arr, 90))
    print("75th Percentile: ", np.percentile(arr, 75))
    print("50th Percentile: ", np.percentile(arr, 50))

def histogram(arr, bar):
    plt.hist(arr, bar)
    plt.show()

def twoArray():
    # x = np.random.uniform(1, 25, 20)
    # y = np.random.normal(80, 0.1, 20)
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    return [x,y]

def scatter():
    arr = twoArray()
    plt.scatter(arr[0], arr[1])
    plt.show()

def linearRegression():
    arr = twoArray()
    x = arr[0]
    y = arr[1]
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    line = slope * x + intercept
    model = list(line)
    print("Relationship:", r)
    plt.scatter(x, y)
    plt.plot(x, model)
    plt.show()

def polynomialRegression():
    arr = twoArray()
    x = arr[0]
    y = arr[1]
    model = np.poly1d(np.polyfit(x, y, 3))
    line = np.linspace(1, 22, 100)
    print("R-Squared: ", r2_score(y, model(x)))
    plt.scatter(x, y)
    plt.plot(line, model(line))
    plt.show()
    return model

def polyPredict(model, num):
    print("Speed: ", model(num))

if __name__ == "__main__":
    model = polynomialRegression()
    polyPredict(model, 17)

