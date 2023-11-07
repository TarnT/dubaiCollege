

def dfs(graph, start_node):

    visited_nodes = set()
    stack = []

    current_node = start_node
    visited_nodes.add(start_node)

    all_child_nodes_visited = False

    for child_node in graph[start_node]:
        if 
