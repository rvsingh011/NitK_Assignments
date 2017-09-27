graph_nodes = [1,2,3,4,5]
paths = []


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            if newpaths:
                if len(graph_nodes) == len(newpaths):
                    paths.append(newpaths)
    return None


def yes_no(graph):
    for x in range(1,6):
        for y in range(1,6):
            find_all_paths(graph, x, y)
    if len(paths) > 0:
        return 1
    else:
        return 0


def hamiltonian():
    for x in range(1,6):
        for y in range(1,6):
            find_all_paths(graph, x, y)
    print(paths)


if __name__ == "__main__":
    graph = {1: [4, 5], 2: [5], 3: [4], 4: [1, 3, 5], 5: [1, 2, 4]}
    # hamiltonian()
    graph1 = graph
    for x in range(1,6):
        graph2 = graph1
        index = 0
        deleted_edge = graph1[x].pop(index)
        if not yes_no(graph1) == yes_no(graph):
            graph1 = graph2
    print(graph1)
