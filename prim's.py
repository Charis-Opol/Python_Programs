# Step 1: Define the Graph class
class Graph:
    def __init__(self):
        # Initialize the graph as an empty dictionary
        self.graph = {}

    # Method to add edges to the graph
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        # Add the edge in both directions because the graph is undirected
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

'''graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3, 'E': 8},
    'E': {'D': 8}
}
'''        


# Step 2: Implement Prim's Algorithm
class PrimMST:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()  # Set to keep track of visited nodes
        self.mst = []  # List to store the edges in the MST

    def find_mst(self, start_node):
        # Add the start node to the visited set
        self.visited.add(start_node)
        # Step 3: Create a list of edges with the smallest weights
        edges = []
        
        # Add all edges connected to the start node to the edges list
        for neighbor, weight in self.graph.graph[start_node]:
            edges.append((weight, start_node, neighbor))

        # Step 4: Iterate until we have the MST with all nodes connected
        while len(self.visited) < len(self.graph.graph):
            # Sort edges based on weight to pick the smallest edge
            edges.sort()  # Sorting by weight (first element in the tuple)

            # Step 5: Pick the edge with the minimum weight that connects to an unvisited node
            for edge in edges:
                weight, u, v = edge

                # If the destination node is not in visited set, we use this edge
                if v not in self.visited:
                    self.visited.add(v)  # Mark the node as visited
                    self.mst.append(edge)  # Add this edge to the MST

                    # Add all edges connected to this new node to the list
                    for neighbor, weight in self.graph.graph[v]:
                        if neighbor not in self.visited:
                            edges.append((weight, v, neighbor))
                    break  # Move to the next edge after adding one

        return self.mst


# Step 3: Test the code
# Create a graph
g = Graph()
g.add_edge("A", "B", 1)
g.add_edge("A", "C", 3)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 4)
g.add_edge("C", "D", 2)

# Create an instance of PrimMST with the graph
prim = PrimMST(g)

# Find the Minimum Spanning Tree starting from node "A"
mst = prim.find_mst("A")

# Print the result
print("Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"{edge[1]} - {edge[2]} (weight: {edge[0]})")
