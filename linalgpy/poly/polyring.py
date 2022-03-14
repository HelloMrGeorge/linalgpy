from typing import List, Tuple
import sympy as sp
from sympy import QQ, latex, simplify
from linalgpy.core.solver import CoreSolver

class GCDSolver(CoreSolver):
    '''
    用辗转相除法求f,g的最大公因式，f作被除数，其次数大于等于g
    '''
    def __init__(self, f: sp.Expr, g: sp.Expr, var: sp.Symbol, evaluate=True) -> None:
        self.f: sp.Poly = sp.Poly(simplify(f), var)
        self.g: sp.Poly = sp.Poly(simplify(g), var)
        self.var: sp.Symbol = var #确定多项式的主变量
        self.qrPair: List[Tuple[sp.Poly, sp.Poly]] = [] #存储每次带余除法的商和余数
        self.gcd: sp.Poly = None #存储结果
        super().__init__(evaluate)

    def toExecute(self) -> None:
        self.qrPair.append((self.g, sp.rem(self.f, self.g, domain=QQ)))
        while self.qrPair[-1][1] != 0:
            f, g = self.qrPair[-1]
            q = sp.quo(f, g)
            r = sp.rem(f, g, domain=QQ)
            self.qrPair.append((q, r))

        self.gcd = sp.gcd(f, g)

    def toDict(self) -> dict:
        js = {}
        js['gcd'] = latex(self.gcd.as_expr())
        js['f'] = latex(self.f.as_expr())
        js['g'] = latex(self.g.as_expr())
        js['qrPair'] = list(map(lambda x: (latex(x[0].as_expr()), latex(x[1].as_expr())), self.qrPair))
        return js