import networkx as nx
import itertools

graph = [
        [0, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
     ]
hamiltonian_paths = []


def hamiltonian(pattern):
    for x in range(len(graph)-1):
        if not graph[pattern[x]][pattern[x+1]]:
            return 0
    return 1


if __name__ == "__main__":
    for x in list(itertools.permutations([0,1,2,3])):
        if hamiltonian(x):
            hamiltonian_paths.append(x)
    print(hamiltonian_paths)


