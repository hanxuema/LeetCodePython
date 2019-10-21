import unittest
graph = {
    "a": ["b","c"],
    "b": ["c","d"],
    "c": ["a","b","d","e"],
    "d": ["b","c","e","f"],
    "e": ["d","f"],
    "f": ["d"]
}

def bfs(graph, s):
    res = [s]
    queue = [s]
    visited = set()
    visited.add(s)
    while (len(queue) > 0):
        v = queue.pop(0)
        nodes = graph[v]
        for n in nodes:
            if n not in visited:
                visited.add(n)
                queue.append(n)
                res.append(n)
    return res


res = bfs(graph, "e")
print("test {} is {}".format("e", (res == ["e","d","f","b","c","a"])))