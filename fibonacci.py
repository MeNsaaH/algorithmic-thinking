import sys

sys.setrecursionlimit(1000000)

number = 10


def fibo(x):
    if x < 2:
        return x 
    return fibo(x-1) + fibo(x-2)

F = [None for i in range(number + 1)]


def mem_fibo(x):
    if x < 2:
        return x
    if F[x] is None:
        F[x] = mem_fibo(x-1) + mem_fibo(x-2)
    return F[x]


def iter_fibo(x):
    F[0] = 0
    F[1] = 1

    for i in range(2, x):
        F[i] = F[i-1] + F[i - 2]
    return F[x]


def iter_fibo_2(x):
    curr = 1
    prev = 0
    for i in range(1, x):
        nxt = curr + prev
        curr, prev = nxt, curr
    return curr
