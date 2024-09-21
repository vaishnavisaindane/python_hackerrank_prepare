from fractions import Fraction
from functools import reduce
import operator#imported this

def product(fracs):
    t = reduce(operator.mul,fracs)#one line ans
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
