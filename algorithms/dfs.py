def depth_first_search(graph, node):

    stack = []
    visited_nodes = []

    stack.append(node)

    while len(stack) != 0:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            for neighbour_node in graph[current_node]:
                if neighbour_node not in visited_nodes:
                    stack.append(neighbour_node)

    return visited_nodes

graph1 = {"A": ["C","B"],
         "B": ["A","C","D","E"],
         "C": ["A","B","F","D"],
         "D": ["C","E","B","H"],
         "E": ["B","D"],
         "F":["C","G"],
         "G":["F"],
         "H":["D"]
         }

print(depth_first_search(graph1, "A"))