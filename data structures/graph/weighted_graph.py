class WeightedGraph:
    def __init__(self) -> None:
        self.graph = {}
        self.vertices = 0

    def add_vertex(self, v):
        if v in self.graph:
            print(f"Vertex {v} already exists.")
        else:
            self.vertices += 1
            self.graph[v] = []

    def add_edge(self, v1, v2, weight):
        if v1 not in self.graph:
            print(f"Vertex {v1} does not exist.")
        elif v2 not in self.graph:
            print(f"Vertex {v2} does not exist")
        else:
            temp = [v2, weight]
            self.graph[v1].append(temp)

    def print_graph(self):
        for vertex in self.graph:
            for edges in self.graph[vertex]:
                print(f"{vertex} -> {edges[0]} edge weight: {edges[1]}")

    def get_vertices(self):
        return self.vertices


if __name__ == "__main__":
    graph = WeightedGraph()
    print(graph.get_vertices())
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 1, 3)
    graph.print_graph()
    print(graph.get_vertices())
