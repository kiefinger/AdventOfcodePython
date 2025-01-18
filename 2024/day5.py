from collections import defaultdict

rules = defaultdict(lambda: 0)
sequences = []
invalids = []

def main():

    with open("data/day05.txt") as file:

        rulesComming = True

        for line in file.read().splitlines():
            if len(line) <1:
                rulesComming = False
                continue

            if  rulesComming == True:
                a,b = line.split('|')
                if rules[a]:
                    rules[a].add ( b)
                else:
                    set_b = {b}
                    rules[a] = set_b
            else:
                numbers = line.split (',')
                sequences.append ( numbers)

        print ( rules )
        total = 0
        for sequence in sequences:
            valid = True
            for e in range ( 1, len(sequence),1 ):
                check = sequence[e]
                rule = rules[check]
                for b in range (e):
                    #print (sequence[b],check, rule)
                    if rule and sequence[b] in rule:
                        valid = False
#                        print ( "found problem in sequence: ", sequence, "check", check, " because:", rule)

            if valid:
                #print ( "found valid sequence: ", sequence )
                total += int(sequence[ int(len(sequence)/2)])
            else:
                invalids.append(sequence)

        total_of_invalids = 0
        # 4891 is too high
        for sequence in invalids:
            #print ( "check invalid sequence: ", sequence)
            e = 1
            while e < len(sequence):
                check = sequence[e]
                rule = rules[check]
                for b in range(e):
                    if rule and sequence[b] in rule:
                        item = sequence[e]
                        del  sequence[e]
                        sequence.insert (b, item )
                        e = 0
                e+=1
            total_of_invalids += int(sequence[ int(len(sequence)/2)])

        print ( len ( rules ), ", ", len (sequences), total, total_of_invalids )

if __name__ == "__main__":
    main()