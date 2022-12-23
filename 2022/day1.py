import os

def main():

    with open("data/day01-1.txt") as file:

        total_max = 0
        total = 0
        m = []

        for line in file.read().splitlines():

            line = line.strip()

            if (len (line)) == 0:
                total_max = max( total_max, total)
                m.append(total)
                total = 0
            else:
                total += int(line)

        print("The highest 3", sorted(m)[-3:])


if __name__ == "__main__":
    main()