from dijkstras import dijkstras
import osmnx as ox
import matplotlib.pyplot as plt

G = ox.graph_from_place('Boulder, Colorado, USA', network_type='drive')

south_boulder_coords = (39.9544, -105.2583)
north_boulder_coords = (40.0506, -105.2822)

start_node = ox.distance.nearest_nodes(G, south_boulder_coords[1], south_boulder_coords[0])  # South Boulder
target_node = ox.distance.nearest_nodes(G, north_boulder_coords[1], north_boulder_coords[0])  # North Boulder

print(f'Start node (South Boulder): {start_node}')
print(f'Target node (North Boulder): {target_node}')

# Run Dijkstra's algorithm to find the shortest path
shortest_path, total_distance = dijkstras(G, start_node, target_node)

print(f'Shortest path: {shortest_path}')
print(f'Total distance: {total_distance} meters')

fig, ax = ox.plot_graph_route(G, shortest_path, route_linewidth=4, node_size=0, bgcolor='white')
plt.show()
