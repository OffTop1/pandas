from pandas import *
from pandas.util.testing import rands

N = 1000
K = 50

def _random_index(howmany):
    return Index([rands(10) for _ in xrange(howmany)])

df = DataFrame(np.random.randn(N, K), index=_random_index(N),
               columns=_random_index(K))

def get1():
    for col in df.columns:
        for row in df.index:
            _ = df[col][row]

def get2():
    for col in df.columns:
        for row in df.index:
            _ = df.get_value(row, col)

def put1():
    for col in df.columns:
        for row in df.index:
            df[col][row] = 0

def put2():
    for col in df.columns:
        for row in df.index:
            df.set_value(row, col, 0)

for col in df.columns:
    for row in df.index:
        value = df.get_value(row, col)
