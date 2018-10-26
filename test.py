from sorts import merge_sort, shell_sort
from time import time

x = [1000 - i for i in range(1000)]

start = time()
a = print(merge_sort(x))
stop = time()
print("Merge Sort time: {0}".format(stop - start))

start = time()
a = shell_sort(x)
stop = time()
print("Shell Sort time: {0}".format(stop - start))