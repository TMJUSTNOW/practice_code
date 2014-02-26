def build_board():
    # 4x4 graph where each node [key] points to all neighboring edges
    # vertical, horizontal and diagonal bidirectional graph
    graph_edges = {
        0: [1, 4, 5],
        1: [0, 2, 4, 5, 6],
        2: [1, 3, 5, 6, 7],
        3: [2, 6, 7],
        4: [0, 1, 5, 8, 9],
        5: [0, 1, 2, 4, 6, 8, 9, 10],
        6: [1, 2, 3, 5, 7, 9, 10, 11],
        7: [2, 3, 6, 10, 11],
        8: [4, 5, 9, 12, 13],
        9: [4, 5, 6, 8, 10, 12, 13, 14],
        10: [5, 6, 7, 9, 11, 13, 14, 15],
        11: [6, 7, 10, 14, 15],
        12: [8, 9, 13],
        13: [8, 9, 10, 12, 14],
        14: [9, 10, 11, 13, 15],
        15: [10, 11, 14]
    }
    return graph_edges


def fill_board(input_string):
    occurances = {}
    index = 0
    for letter in input_string:
        if occurances.get(letter):
            occurances[letter].append(index)
        else:
            occurances[letter] = [index]
        index += 1
    return occurances


def traverse_graph(graph, input_string, target, storage):
    open_paths = storage
    # if storage is
        # stack: search is depth-first
        # queue: search is breadth-first

    occur = fill_board(input_string)
    start = target[0]
    if occur.get(start):
        # adds location for each occurrence of target[first letter] to open_paths
        for node in occur[start]:
            open_paths.put([node])
        visited_node_list = occur[start]
        found_target_path = []
        i = 1
        while len(open_paths) != 0 and i <= len(target):
            current_path = [open_paths.get()]
            # print("open_paths %s" % open_paths)
            edges = graph[current_path]
            # print("current_path %s" % current_path)
            available_nodes = set.intersection(set(occur[target[i]]), set(edges))
            available_nodes = available_nodes.remove(visited_node_list)


            if node == target:
                found_target_path.append(current_path + [node])
                print("target found! %s" % found_target_path[-1])
                return True
            if node not in visited_node_list:
                visited_node_list.append(node)
                # print("new node %s" % node)
                # print("visited_node_list %s" % visited_node_list)
                new_path = current_path + [node]
                # print("new path %s" % new_path)
                open_paths.put(new_path)
                # print("added new path to queue %s" % open_paths[-1])
            i += 1
    return False


class Storage(object):
    def __init__(self):
        self.storage = []

    def put(self, node):
        self.storage.append(node)

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)


class Stack(Storage):
    def get(self):
        return self.storage.pop()


class Queue(Storage):
    def get(self):
        return self.storage.pop(0)


board = build_board()
target = 'ME'
input_string = 'FGMENTPAHEMQLEFD'
storage = Stack()
print(traverse_graph(board, input_string, target, storage))
