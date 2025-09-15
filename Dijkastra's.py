# Graph Representation using a Class
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to store the graph
    
    def add_edge(self, key1, key2, distance_between):
        # If key1 is not already in the graph, add it
        if key1 not in self.graph:
            self.graph[key1] = {}
        # If key2 is not already in the graph, add it
        if key2 not in self.graph:
            self.graph[key2] = {}
        
        # Add the edge in both directions (since it's an undirected graph)
        self.graph[key1][key2] = distance_between
        self.graph[key2][key1] = distance_between
    
    def get_graph(self):
        return self.graph  # Return the constructed graph


def dijkstra(graph, start):
    # Dictionary to store the shortest distance from the start key to each key
    shortest_distances = {}  # Create an empty dictionary
    for key in graph:  # Loop through each key in the graph
        shortest_distances[key] = float('inf')  # Set initial distance to infinity
    shortest_distances[start] = 0  # Distance from start key to itself is 0
    
    # List to act as a priority queue (stores (distance, key) tuples)
    priority_queue = []  # Create an empty list
    priority_queue.append((0, start))  # Add the start key with distance 0
    
    # Dictionary to track the previous keys (for path reconstruction if needed)
    visited_keys = {}  # Create an empty dictionary
    for key in graph:  # Loop through each key
        visited_keys[key] = None  # Initialize previous keys as None
    
    while priority_queue:
        # Get the key with the smallest distance from the priority queue manually
        priority_queue.sort()  # Sort to get the smallest distance key at index 0
        current_distance, current_key = priority_queue.pop(0)  # Remove and get the first element
        
        # If we have already found a shorter path before, skip processing this key
        if current_distance > shortest_distances[current_key]:
            continue  # Skip this iteration
        
        # Explore the next_vertexs of the current key
        for next_vertex in graph[current_key]:  # Loop through next_vertexing keys
            distance_between = graph[current_key][next_vertex]  # Get the distance_between of the edge
            distance = current_distance + distance_between  # Compute new distance to next_vertex
            
            # If the new distance is shorter, update shortest_distances and queue
            if distance < shortest_distances[next_vertex]:
                shortest_distances[next_vertex] = distance  # Update shortest path distance
                visited_keys[next_vertex] = current_key  # Track the path
                priority_queue.append((distance, next_vertex))  # Append new distance and key
    
    return shortest_distances, visited_keys  # Return final shortest paths and paths taken

# Create the graph using the Graph class
graph_obj = Graph()
graph_obj.add_edge('A', 'B', 4)
graph_obj.add_edge('A', 'C', 2)
graph_obj.add_edge('B', 'C', 5)
graph_obj.add_edge('B', 'D', 10)
graph_obj.add_edge('C', 'D', 3)
graph_obj.add_edge('D', 'E', 8)

graph = graph_obj.get_graph()  # Retrieve the graph dictionary

'''graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
}
'''

# Run Dijkstra's algorithm starting from key 'A'
shortest_paths, paths_taken = dijkstra(graph, 'A')

# Print the shortest path distances from 'A' to all keys
print("Shortest distances from A:")
for key in shortest_paths:  # Loop through the shortest paths dictionary
    distance = shortest_paths[key]  # Get the shortest distance
    print("Key", key, ":", distance)  # Print key and distance

# Print the paths taken to reach each key
print("\nPaths taken:")
for key in paths_taken:  # Loop through the previous keys dictionary
    previous = paths_taken[key]  # Get the previous key in the path
    print("Key", key, "<-", previous)  # Print path information
