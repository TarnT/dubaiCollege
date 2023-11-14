def iterative_depth_first_search(node):
    stack = []
    visited_
    stack.append(node)
    while len(stack) != 0:
        current = stack.pop()
        if not current.visited:
            visit(current)
            current.visited = True
            for neighbor in current.neighbors:
                if not neighbor.visited: stack. append (neighbor)