import heapq
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def h(state):
    return sum(state[i] != goal[i] for i in range(9) if state[i] != 0)

def astar(start):
    queue = [(h(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)
        pos = state.index(0)
        r, c = divmod(pos, 3)

        for x, y in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if 0 <= x < 3 and 0 <= y < 3:
                new = list(state)
                j = x * 3 + y
                new[pos], new[j] = new[j], new[pos]
                new = tuple(new)

                if new not in visited:
                    heapq.heappush(queue, (g+1+h(new), g+1, new, path+[new]))

    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
path = astar(start)

if path:
    for state in path:
        for i in range(0, 9, 3):
            print(*state[i:i+3])
        print()
    print("Total Moves:", len(path)-1)
else:
    print("No Solution")