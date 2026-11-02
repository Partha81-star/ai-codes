grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
start = (0, 0)
goal = (3, 3)

queue = [(start, [start])]
visited = {start}

while queue:
    position, path = queue.pop(0)
    if position == goal:
        print("Path:", path)
        print("Goal Reached!")
        break
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x = position[0] + dx
        y = position[1] + dy

        if 0 <= x < 4 and 0 <= y < 4:
            if grid[x][y] == 0 and (x, y) not in visited:
                visited.add((x, y))
                queue.append(((x, y), path + [(x, y)]))
else:
     print("No Path Found")