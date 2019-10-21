graph = {
    "a": ["b","c"],
    "b": ["a","c","d"],
    "c": ["a","b","d","e"],
    "d": ["b","c","e","f"],
    "e": ["c","d"],
    "f": ["d"]
}

def dfs(graph, s):
    res = [s]
    stack = [s]
    visited = set()
    visited.add(s)
    while len(stack) > 0 :
        v = stack.pop() # pop() returns the last 1, pop(0) returns the first 1
        nodes = graph[v]
        for n in nodes:
            if n not in visited:
                visited.add(n)
                res.append(n)
                stack.append(n)
    print(res)
    return res    

print("test {} is {} ".format("e", dfs(graph, "e") == ['e','c','d','b','f','a']))
