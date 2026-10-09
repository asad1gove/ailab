import heapq

def solve(start, goal):
    open = [(0, start)]
    closed = set()

    while open:
        curr = heapq.heappop(open)[1]

        misplacedItems = sum(
            curr[i] != goal[i] and curr[i] != 0
            for i in range(9)
        )

        if misplacedItems == 0:
            return curr

        closed.add(curr)

        zero = curr.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                pos = nr * 3 + nc
                nxt = list(curr)
                nxt[zero], nxt[pos] = nxt[pos], nxt[zero]
                nxt = tuple(nxt)

                if nxt not in closed:
                    h = sum(
                        nxt[i] != goal[i] and nxt[i] != 0
                        for i in range(9)
                    )
                    heapq.heappush(open, (h, nxt))

    return "No solution"


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

print(solve(start, goal))