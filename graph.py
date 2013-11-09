import copy

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


def traverse_graph(graph, target, start):
    open_path_list = [[]]
    open_path_list[0] = [start]
    current_path = [start]
    closed_node_list = []
    found_path_list = []

    while(len(open_path_list) != 0):

        for path in open_path_list:
            current_path = copy.deepcopy(path)
            available = graph[current_path[-1]]
            closed_node_list.append(current_path[-1])
            print("curent_path %s" % current_path)
            print("open_path_list %s" % open_path_list)
            # print("closed_node_list %s" % closed_node_list)
            print("available %s" % available)

            open_path_list.remove(current_path)
            for neighbor in available:
                if neighbor not in closed_node_list:
                    new_path = copy.deepcopy(current_path)
                    new_path.append(neighbor)
                    print("current_path %s" % current_path)
                    print("new_path %s" % new_path)
                    if(neighbor == target):  # found target
                        found_path_list.append(new_path)
                    open_path_list.append(new_path)
                    print("neighbor added to closed_node %s" % neighbor)
                    closed_node_list.append(neighbor)
        if len(available) > 0:
            next = available[0]
            current_path.append(next)
            closed_node_list.append(next)
            print("next %s" % next)
        else:
            current_path.pop()
    return found_path_list

g = graph_dict2
target = 12
start = 1
print(traverse_graph(g, target, start))
