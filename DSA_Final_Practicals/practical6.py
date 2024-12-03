from collections import deque, defaultdict

class Graph:
    """Graph implemented using an adjacency list."""
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        """Add an edge to the graph (u -> v)."""
        self.adj_list[u].append(v)

    def dfs(self, start):
        """Perform Depth-First Search (DFS)."""
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def bfs(self, start):
        """Perform Breadth-First Search (BFS)."""
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def display_graph(self):
        """Display the adjacency list of the graph."""
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {', '.join(map(str, neighbors))}")

# Example usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

print("Graph adjacency list:")
graph.display_graph()

print("\nDFS starting from node 1:", graph.dfs(1))
print("BFS starting from node 1:", graph.bfs(1))
