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
    res = []
    queue = []
    queue.append(s)
    visited = set()
    visited.add(s)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        print("current vertex is {} ".format(vertex))
        nodes = graph[vertex]
        print("current vertex has nodes {}".format(nodes))
        for w in nodes:
            print("     visit node {} of vertex {} ".format(w, vertex))
            if w not in visited:
                print("             node {} is not visited before".format(w))
                queue.append(w)
                print("             node {} is added to queue, queue is {} ".format(w, queue))
                visited.add(w)
                res.append(w)
            else:
                print("             node {} is visited before".format(w))
    print("final queue {}, visited {}, res {}".format(queue, visited, res))
    res = [s] + res
    return res


res = bfs(graph, "e")
print("test {} is {}".format("e", (res == ["e","d","f","b","c","a"])))