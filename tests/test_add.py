import numpy as np
from sod import add

def test_add():
    for i in range(100):
        a, b = np.random.rand(2)
        assert add(a,b) == a+b