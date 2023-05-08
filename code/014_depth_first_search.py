from typing import Literal


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

    def adjacent(self, x: int) -> set[int]:
        return self.graph.get(x, set())

    def degree(self, x: int) -> int:
        return len(self.graph.get(x, []))

    @property
    def nodes(self) -> list[int]:
        return list(self.graph)


def depth_first_search(
    G: Graph, s: int, method: Literal["iterative", "recursive"] = "iterative"
) -> set[int]:
    # The set of seen nodes
    seen = set()

    def iterate():
        # Create the seen set and the stack
        stack = []

        # Initialize both seen and the s with s
        seen.add(s)
        stack.append(s)

        # Loop until the stack is empty
        while len(stack) != 0:
            # Get and remove the top node x from the stack
            x = stack.pop()
            # Loop through the neighbours of x
            for y in G.adjacent(x):
                # If y has been seen then continue
                if y in seen:
                    continue
                # Add y to seen and the stack
                seen.add(y)
                stack.append(y)
        return seen

    def recurse(x: int) -> None:
        # Add x to seen
        seen.add(x)
        # Loop over neighbours y of x and recurse if y has not been seen
        for y in G.adjacent(x):
            if y not in seen:
                recurse(y)

    if method == "iterative":
        iterate()
    else:
        recurse(s)
    return seen


if __name__ == "__main__":
    # A few tests
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge(1, 2)

    component = depth_first_search(G, 1)
    assert component == {1, 2}
    component = depth_first_search(G, 1, "recursive")
    assert component == {1, 2}

    component = depth_first_search(G, 3)
    assert component == {3}
    component = depth_first_search(G, 3, "recursive")
    assert component == {3}

    G.add_node(4)
    G.add_edge(3, 4)

    component = depth_first_search(G, 4)
    assert component == {3, 4}
    component = depth_first_search(G, 4, "recursive")
    assert component == {3, 4}
