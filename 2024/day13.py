import os
import re
from collections import defaultdict, Counter, deque, namedtuple
import sympy

re_button = re.compile(r"Button (?P<button>[AB]): X\+(?P<x>\d+), Y\+(?P<y>\d+)")
re_prize = re.compile(r"Prize: X=(?P<x>\d+), Y=(?P<y>\d+)")

Button = namedtuple("Button", ["name", "x", "y", "cost"])
Prize = namedtuple("Prize", ["x", "y", "xh", "yh"])
Machine = namedtuple("Machine", ["A", "B", "prize"])
Play = namedtuple("Play", ["x", "y", "cost"])
machines = []
high = 10000000000000

def main():
    p1 = 0
    p2 = 0
    seen = set()
    with open( "data/day13.txt" ) as file:
        strMachines = file.read().split('\n\n')

        for strMachine in strMachines:
            stra, strb, strp = strMachine.split('\n')
            a_button = re.match(re_button, stra).groupdict()
            a_button = Button(a_button["button"], int(a_button["x"]), int(a_button["y"]), 3)

            b_button = re.match(re_button, strb)
            b_button = Button(b_button["button"], int(b_button["x"]), int(b_button["y"]), 1)

            prize = re.match(re_prize, strp.strip()).groups()
            prize = Prize(int(prize[0]), int(prize[1]), int(prize[0])+high, int(prize[1])+high)
            m =  Machine(a_button, b_button, prize)
            machines.append(m)
        p1 = 0
        for m in machines:
            px  = m.prize.x
            py =  m.prize.y
            if  (m.A.x * 100 + m.B.x * 100) < px :
                continue
            if  (m.A.y * 100 + m.B.y * 100 ) < px:
                continue
            min_cost = 1000000
            for a in range (100):
                for b in range (100):
                    if (a * m.A.x + b * m.B.x) == m.prize.x and (a * m.A.y + b * m.B.y) == m.prize.y:
                        min_cost = min( a * 3 + b, min_cost)
            if min_cost< 1000000:
                p1 += min_cost

        print (p1)
        p2 = 0

        for m in machines:
            a_presses, b_presses = sympy.symbols('a_presses b_presses', integer=True)
            equations = [
                a_presses * m.A.x + b_presses * m.B.x - m.prize.xh,
                a_presses * m.A.y + b_presses * m.B.y - m.prize.yh
            ]
            solution = sympy.solve(equations)
            if solution :
                p2 += m.A.cost * solution[a_presses] + m.B.cost * solution[b_presses]

        print (p2)



if __name__ == "__main__":
    main()