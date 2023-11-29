def dijkstras_algorithm(graph, start_node):

    unvisited_nodes = list(graph.keys())

    current_weights = {}
    for node in unvisited_nodes:
        current_weights[node] = float("inf")
    
    current_weights[start_node] = 0
    current_node = start_node

    while len(unvisited_nodes) > 0:

        print(f"current node is {current_node}")
        for neighboring_node in graph[current_node]:
            print(f"neighbouring node is {neighboring_node}")
            print(f"sum of distance to node from current node is {current_weights[current_node] + neighboring_node[1]}")
            print(f"current distance to {neighboring_node} is {current_weights[neighboring_node[0]]}")
            if (neighboring_node[1] + current_weights[current_node]) < current_weights[neighboring_node[0]]:
                current_weights[neighboring_node] = neighboring_node[1] + current_weights[current_node]
        
        unvisited_nodes.remove(current_node)
        if len(unvisited_nodes) > 0:
            current_node = unvisited_nodes[0]

    return current_weights

graph1 = {
    "A": (("B", 8), ("C", 2)),
    "B": (("A", 8), ("D", 9), ("E", 4)),
    "C": (("A", 2), ("D", 5)),
    "D": (("C", 5), ("B", 9), ("E", 5)),
    "E": (("B", 9), ("D", 5)),
}

print(dijkstras_algorithm(graph1, "A"))