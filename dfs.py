graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def dfs(node, goal, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")

    if node == goal:
        return True

    visited.add(node)

    for x in graph[node]:
        if x not in visited:
            if dfs(x, goal, visited):
                return True

    return False

dfs("A", "F")
