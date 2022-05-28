from weighted_graph import *


def main():
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


if __name__ == "__main__":
    main()
