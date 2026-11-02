from collections import deque
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
def bfs(start, goal):
    q = deque([[start]])
    visited = set()

    while q:
        path = q.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for x in graph[node]:
            q.append(path + [x])

print("BFS Path:", bfs("A", "F"))