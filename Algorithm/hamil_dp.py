import copy
graph_nodes = [1,2,3,4]
paths = []


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


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
    graph = {1: [2,3], 2: [1], 3: [1,4], 4: [3]}
    hamiltonian()

    # graph1 = copy.deepcopy(graph)
    # for x in range(1,6):
    #     paths = []
    #     graph2 = copy.deepcopy(graph1)
    #     index = 0
    #     deleted_edge = graph1[x].pop(index)
    #     if not yes_no(graph1) == yes_no(graph):
    #         graph1 = copy.deepcopy(graph2)
    # for x in range(1,6):
    #     for y in range(1,6):
    #         new_path = find_path(graph1, x, y)
    #         if new_path:
    #             if len(new_path) == len(graph_nodes):
    #                 print(new_path)
