import re

def main():

    with open("data/day03.txt") as file:

        total = 0
        txt = file.read()
        x = re.findall("mul\(\d\d?\d?,\d\d?\d?\)", txt)
        for d in x:
            a,b = re.findall( "\d\d?\d?", d)
            total += (int(a) * int(b))

        print("total: ", total)

        # part II with do/don't switch
        total = 0
        do = "do()"
        dont = "don't()"
        x = re.findall("(mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\))", txt)
        active = True

        for d in x:
            if d == do:
                active = True
            elif d == dont:
                active = False
            else:
                if active:
                  a,b = re.findall( "\d\d?\d?", d)
                  total += (int(a) * int(b))

        print("total: ", total)

if __name__ == "__main__":
    main()