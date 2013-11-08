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


# current/target = key; path/visited = list of keys
def traverse_graph(graph, target, path, vistited):
    path_list = []
    while(len(path) != 0):
        if(path[-1] == target):
            new_path = copy.deepcopy(path)
            path_list.append(new_path)
        available = graph[path[-1]]
        print("path %s" % path)
        # print("vistited %s" % vistited)
        # print("available %s" % available)
        for node in available:
            if node in vistited:
                # print("remove node %s" % node)
                available.remove(node)
                # print("available %s" % available)
        if len(available) > 0:
            next = available[0]
            path.append(next)
            vistited.append(next)
            print("next %s" % next)
        else:
            path.pop()
    return path_list

g = graph_dict2
target = 12
start = [1]
history = [1]
print(traverse_graph(g, target, start, history))
