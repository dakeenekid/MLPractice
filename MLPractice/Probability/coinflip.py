import random
import itertools


def coins(num):
    lst = [random.randrange(2) for i in range(num)]
    lst = [(i, len(list(j))) for i, j in itertools.groupby(lst)]
    tails = max(j for i, j in lst if i)
    heads = max(j for i, j in lst if not i)
    return {1: tails, 0: heads}

print(coins(1024))