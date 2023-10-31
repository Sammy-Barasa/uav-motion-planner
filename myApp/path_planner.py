def a_star(start, end, graph):
    open_set = PriorityQueue()
    open_set.put(start)

    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0

    while not open_set.empty():
        current = open_set.get()

        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + distance(current, neighbor)

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                open_set.put(neighbor)

    return None  

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    return path[::-1]
