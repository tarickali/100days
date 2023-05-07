class Graph:
    def __init__(self) -> None:
        self.graph: dict[int, set[int]] = {}

    def add_node(self, x: int) -> None:
        if x in self.graph:
            return
        self.graph[x] = set()

    def remove_node(self, x: int) -> None:
        if x not in self.graph:
            return

        # Remove all edges incident to x
        ys = self.graph.get(x)
        for y in ys:
            self.graph[y].remove(x)

        # Remove x from graph
        self.graph.pop(x)

    def add_edge(self, x: int, y: int) -> None:
        if x not in self.graph or y not in self.graph:
            return

        # Add edge from x to y
        self.graph[x].add(y)
        # Add edge from y to x
        self.graph[y].add(x)

    def remove_edge(self, x: int, y: int) -> None:
        if x not in self.graph or y not in self.graph[x]:
            return
        # Remove the edge x to y
        self.graph[x].remove(y)
        # Remove the edge y to x
        # NOTE: y is in graph since add_edge adds edges x to y and y to x
        self.graph[y].remove(x)

    def adjacent_nodes(self, x: int) -> set[int]:
        return self.graph.get(x, set())

    def degree(self, x: int) -> int:
        return len(self.graph.get(x, []))


if __name__ == "__main__":
    # A few tests
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)

    assert G.degree(1) == 2
    assert G.degree(2) == 2
    assert G.degree(3) == 2

    assert G.adjacent_nodes(1) == {2, 3}
    assert G.adjacent_nodes(2) == {1, 3}
    assert G.adjacent_nodes(3) == {1, 2}

    G.remove_node(1)
    assert G.adjacent_nodes(2) == {3}
    assert G.adjacent_nodes(3) == {2}
    assert G.degree(2) == 1
    assert G.degree(3) == 1

    G.remove_edge(2, 3)
    assert G.adjacent_nodes(2) == set()
    assert G.adjacent_nodes(3) == set()
    assert G.degree(2) == 0
    assert G.degree(3) == 0
