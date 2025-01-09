

def abc ( report ):
    inc = 0
    for i in range(len(report) - 1):
        if report[i] < report[i + 1]:
            inc += 1
        else:
            inc -= 1
    unsafe = 0
    l = 0
    r = 1

    length = len(report)
    while (l < length - 1 and r < length):
        if inc > 0:
            a = report[l]
            b = report[r]
        else:
            a = report[r]
            b = report[l]
        if (b < a or (b - a < 1 or b - a > 3)):
            return False
        else:
            l += 1
            r += 1
    return True


def main():

    matrix = []
    with open("data/day02.txt") as file:

        total_max = 0
        total = 0
        m = []

        for line in file.read().splitlines():
            matrix.append([int(x) for x in line.split()])

        for report in matrix:
            save = abc ( report )
            if ( save == True) :
                total +=1
        print("The total save", total)

        # Part II
        total = 0
        for report in matrix:
            if ( abc ( report ) == True):
                total += 1
            else:
                save = 0
                for g in range ( len(report)):
                    r = report [0:g]  + report [g+1 : len(report)]
                    if ( abc ( r ) == True):
                        save +=1
                if ( save>0) :
                    total +=1


        #  412 < total < 431
        print("total save levels II: ", total)

if __name__ == "__main__":
    main()