import re
from itertools import product

matrix = []

def main():
    with open("data/day07.txt") as file:
        for line in file.read().splitlines():

            rc, rest = line.split(':')
            args = [ int(x) for x in rest.split()]
            matrix.append( { "rc": int(rc) , "args": args, "found": False})
        print("total: ", matrix)

        total = 0
        for term in matrix:
            possible = product("*+", repeat=len(term["args"]) - 1)
            for op in possible:
                result = term["args"][0]
                for i in range(len(op)):
                    if op[i] == "*":
                        result *= term["args"][i + 1]
                    else:
                        result += term["args"][i + 1]

                if result == term["rc"]:
                    total += term["rc"]
                    break

        print ( total )

        total = 0
        for term in matrix:
            possible = product("*+|", repeat=len(term["args"]) - 1)
            for op in possible:
                result = term["args"][0]
                for i in range(len(op)):
                    if op[i] == "*":
                        result *= term["args"][i + 1]
                    elif op[i] == "+":
                        result += term["args"][i + 1]
                    else:
                        l = len(str(term["args"][i + 1]))
                        result = result * pow( 10, l) + term["args"][i + 1]
                if result == term["rc"]:
                    total += term["rc"]
                    break
        print ( total )

if __name__ == "__main__":
    main()