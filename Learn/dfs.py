graph = {
    "a": ["b","c"],
    "b": ["a","c","d"],
    "c": ["a","b","d","e"],
    "d": ["b","c","e","f"],
    "e": ["c","d"],
    "f": ["d"]
}

def dfs(graph, s):
    stack = []
    stack.append(s)
    visited = set()
    visited.add(s)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for n in nodes:
            if n not in visited:
                stack.append(n)
                visited.add(n)
        print(vertex)

dfs(graph, "e")
