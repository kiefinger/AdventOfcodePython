import os
import re
from collections import defaultdict, Counter, deque

DIRS = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1,0],
]

def main():
    p1 = 0
    p2 = 0
    seen = set()
    with open( "data/day12.txt" ) as file:
        matrix = file.read().split('\n')
        R = len(matrix)
        C = len(matrix[0])
        seen = set()

        for r in range (R):
            for c in range ( C):
                if (r, c) in seen:
                    continue
                queue = deque([(r, c)])
                area = 0
                fences_counter = 0
                fences = dict()
                while queue:
                    r2, c2 = queue.popleft()
                    if (r2, c2) in seen:
                        continue
                    seen.add((r2, c2))
                    area += 1
                    for dr, dc in DIRS:
                        rr = r2 + dr
                        cc = c2 + dc
                        if 0 <= rr < R and 0 <= cc < C and matrix[rr][cc] == matrix[r2][c2]:
                            queue.append((rr, cc))
                        else:
                            fences_counter += 1
                            if (dr, dc) not in fences:
                                fences[(dr, dc)] = set()
                            # side = same direction, adjacent
                            fences[(dr, dc)].add((r2, c2))

                sides_counter = 0
                for k, vs in fences.items():
                    seen_fences = set()
                    for (pr, pc) in vs:
                        if (pr, pc) not in seen_fences:
                            sides_counter += 1
                            queue = deque([(pr, pc)])
                            while queue:
                                r2, c2 = queue.popleft()
                                if (r2, c2) in seen_fences:
                                    continue
                                seen_fences.add((r2, c2))
                                for dr, dc in DIRS:
                                    rr, cc = r2 + dr, c2 + dc
                                    if (rr, cc) in vs:
                                        queue.append((rr, cc))

                p1 += area * fences_counter
                p2 += area * sides_counter

        print ( p1,p2)

if __name__ == "__main__":
    main()