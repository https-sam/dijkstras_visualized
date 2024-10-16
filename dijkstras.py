import heapq

def dijkstras(graph, source, target):
    pq = [(0, source)]  # (cost, node)

    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[source] = 0
    previous_nodes = {node: None for node in graph}

    while pq:
        curr_distance, node = heapq.heappop(pq)

        # Target found
        if node == target:
            break

        # If current distance is longer, no need to explore
        if curr_distance > shortest_distances[node]:
            continue

        # Explore neighbors
        for neighbor, attributes in graph[node].items():
            edge_weight = attributes.get('length', 1)
            distance = curr_distance + edge_weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                previous_nodes[neighbor] = node

    # Reconstruct shortest path
    path = []
    node = target
    while previous_nodes[node] is not None:
        path.append(node)
        node = previous_nodes[node]

    path.append(source)
    return path[::-1], shortest_distances[target]
