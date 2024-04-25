import numpy
from scipy import stats
from matplotlib import pyplot

# age = [15, 10, 12, 13, 14, 15, 17, 18, 9, 8]
#
# print(sorted(age))
# print(numpy.mean(age))
# print(numpy.median(age))
# print(stats.mode(age))
#
# speed = [100, 110, 105, 120, 95]
# print(numpy.std(speed))
# print(numpy.percentile(speed, 50))

arr = numpy.random.uniform(0, 100, 1000)
print(arr)
pyplot.hist(arr, 100)
pyplot.show()
