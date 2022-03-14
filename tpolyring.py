from linalgpy.poly import polyring
import sympy as sp
from sympy.abc import x

def test1():
    f = x**4 + x**3 - 3*x**2 - 4*x - 1
    g = x**3 + x**2 - x**2 - x - 1
    sl = polyring.GCDSolver(f, g, x)

    print('alg:', sl.qrPair[-2][1])
    print('sp:', sp.gcd(f, g))

    print(sl.dict())


if __name__ == '__main__':
    test1()