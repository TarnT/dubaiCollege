

def dfs(graph, start_node):

    visited_nodes = set()
    stack = []

    current_node = start_node

    all_child_nodes_visited = False

    while not all_child_nodes_visited:
        visited_nodes.add(current_node)
        stack.append(current_node)

        all_child_nodes_visited = True 

        for child_node in graph[current_node]:
            if child_node not in visited_nodes:
                all_child_nodes_visited = False
                current_node = child_node

