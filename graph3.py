graph_dict = {}
graph_dict[1] = [2, 4]
graph_dict[2] = [1, 3, 5]
graph_dict[3] = [2]
graph_dict[4] = [1, 7]
graph_dict[5] = [2, 6, 8]
graph_dict[6] = [5, 9, 10]
graph_dict[7] = [4]
graph_dict[8] = [5]
graph_dict[9] = [6, 12]
graph_dict[10] = [6, 11]
graph_dict[11] = [10]
graph_dict[12] = [9]

graph_dict2 = {}
graph_dict2[1] = [2, 4]
graph_dict2[2] = [1, 3, 5]
graph_dict2[3] = [2, 11]
graph_dict2[4] = [1, 5, 7]
graph_dict2[5] = [2, 4, 6, 8]
graph_dict2[6] = [5, 9, 10]
graph_dict2[7] = [4, 13]
graph_dict2[8] = [5, 14]
graph_dict2[9] = [6, 12]
graph_dict2[10] = [6, 11]
graph_dict2[11] = [3, 10]
graph_dict2[12] = [9]
graph_dict2[13] = [7, 14]
graph_dict2[14] = [8, 13]


def graph_dict3():
    graph_dict3 = {}
    with open('connections.txt', 'r') as input_file:
        for line in input_file:
            split_line = line.split()
            node = int(split_line[0])
            connection = int(split_line[1])

            if node in graph_dict3:
                graph_dict3[node].append(connection)
            else:
                graph_dict3[node] = [connection]

            if connection in graph_dict3:
                graph_dict3[connection].append(node)
            else:
                graph_dict3[connection] = [node]

    return graph_dict3


def traverse_graph(graph, start, target, storage):
    open_paths = storage
    open_paths.put([start])
    visited_node_list = [start]
    found_target_path = []
    while len(open_paths) != 0:
        print("open_paths %s" % open_paths)
        current_path = open_paths.get()
        # print("current_path %s" % current_path)
        available_nodes = graph[current_path[-1]]
        # print("available_nodes %s" % available_nodes)
        for node in available_nodes:
            if node == target:
                found_target_path.append(current_path + [node])
                print("target found! %s" % found_target_path[-1])
                return found_target_path
            if node not in visited_node_list:
                visited_node_list.append(node)
                # print("new node %s" % node)
                # print("visited_node_list %s" % visited_node_list)
                new_path = current_path + [node]
                # print("new path %s" % new_path)
                open_paths.put(new_path)
                # print("added new path to queue %s" % open_paths[-1])


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


g = graph_dict2
target = 14
start = 1
storage = Stack()
print(traverse_graph(g, start, target, storage))
