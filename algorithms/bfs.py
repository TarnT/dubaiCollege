def breadth_first_search(graph, node):
    
    queue = []
    visited_nodes = []

    current_node = node
    queue.append(node)
    visited_nodes.append(current_node)

    while len(queue) != 0:

        current_node = queue.pop(0)

        for neighbour_node in graph[current_node]:
            if neighbour_node not in visited_nodes:
                queue.append(neighbour_node)
                visited_nodes.append(neighbour_node)
    
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

print(breadth_first_search(graph1, "A"))