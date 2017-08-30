from collections import defaultdict
import heapq


class CreateNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __str__(self):
        return '(' + self.symb + ',' + str(self.freq) + ')'

    def traversal(self, root):
        if root:
            
            traversal(root.left)



if __name__ == "__main__":
    list_of_node = []
    data = [('c', 105), ('e', 15), ('t', 65)]
    for x in data:
        obj = CreateNode(x[0], x[1])
        list_of_node.append(obj)
    heapq.heapify(list_of_node)
    while len(list_of_node) > 1:
        node1 = heapq.heappop(list_of_node)
        node2 = heapq.heappop(list_of_node)
        list_of_node.append(CreateNode(None, node1.freq + node2.freq, node1, node2))
        heapq.heapify(list_of_node)







    # while len(list_of_node) > 1:
    #     list_of_node.append(CreateNode(None, node1.freq + node2.freq, node1, node2))
    #     heapq.heapify(list_of_node)
    #
    #


# def encode(frequency):
#     heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
#     heapq.heapify(heap)
#     while len(heap) > 1:
#         lo = heapq.heappop(heap)
#         hi = heapq.heappop(heap)
#         for pair in lo[1:]:
#             pair[1] = '0' + pair[1]
#         for pair in hi[1:]:
#             pair[1] = '1' + pair[1]
#         heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
#     return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
#
# if __name__ == "__main__":
#     data = "mna"
#     encoded_string = ""
#     frequency = defaultdict(int)
#     for x in data:
#         frequency[x] += 1
#     huff = encode(frequency)
#     for p in huff:
#         print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
#     huff_dict = {}
#     for x in huff:
#         huff_dict[x[0]] = x[1]
#     for y in data:
#         encoded_string = encoded_string + huff_dict[y]
#         encoded_string = encoded_string + "$"
#     print(encoded_string)
#
#
#
#
