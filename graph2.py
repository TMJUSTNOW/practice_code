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


def initialize_graph_dict3():
    graph_dict3 = {}
    with open('connections.txt', 'r') as text_file:
        for line in text_file:
                graph_dict3_text = text_file.read()
                split_line = line.split()

                if split_line[0] in graph_dict3_text:
                    graph_dict3[split_line[0]].append(split_line[1])
                else:
                    graph_dict3[split_line[0]] = [split_line[1]]

                if split_line[1] in graph_dict3_text:
                    graph_dict3[split_line[1]].append(split_line[0])
                else:
                    graph_dict3[split_line[1]] = [split_line[0]]
    return graph_dict3


def traverse_graph(graph, start, target):
    open_path_queue = []
    open_path_queue.append([start])
    visited_node_list = [start]
    found_target_path = []
    while len(open_path_queue) != 0:
        current_path = open_path_queue[0]
        print("open_path_queue %s" % open_path_queue)
        # print("current_path %s" % current_path)
        available_nodes = graph[current_path[-1]]
        # print("available_nodes %s" % available_nodes)
        open_path_queue.pop(0)
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
                open_path_queue.append(new_path)
                # print("added new path to queue %s" % open_path_queue[-1])


g = initialize_graph_dict3()
target = 7777
start = 1
print(traverse_graph(g, start, target))
