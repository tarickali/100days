from queue import Queue


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


def breadth_first_search(G: Graph, s: int) -> set[int]:
    # Create the seen set and the queue
    seen = set()
    q = Queue()

    # Initialize both seen and the queue with s
    seen.add(s)
    q.put(s)

    # Loop until the queue is empty
    while not q.empty():
        # Get and remove the top node x from the queue
        x = q.get()
        # Loop through the neighbours of x
        for y in G.adjacent(x):
            # If y has been seen then continue
            if y in seen:
                continue
            # Add y to seen and the queue
            seen.add(y)
            q.put(y)
    return seen


def connected_components(G: Graph) -> list[set[int]]:
    seen = set()  # the nodes seen from each iteration
    components = []  # the list of connected components
    for x in G.nodes:
        # If x has been seen (in a component) then continue
        if x in seen:
            continue
        # Perform BFS on x
        component = breadth_first_search(G, x)
        # Update the seen nodes from the found component
        seen |= component
        # Add a new component to G
        components.append(component)
    return components


def is_connected(G: Graph) -> bool:
    # If there is <= 1 connected component then by definition G is connected
    return len(connected_components(G)) <= 1


def shortest_path(G: Graph, s: int) -> dict[int, int]:
    # Create the seen set and the queue
    seen = set()
    q = Queue()

    # Dictionary to store the distance from s to nodes in G
    # NOTE: dist will only contain nodes that are connected to s in G
    dist = {}

    # Initialize both seen and the queue with s
    seen.add(s)
    q.put(s)
    # Initialize the distance dictionary with s -> 0
    dist[s] = 0

    # Loop until the queue is empty
    while not q.empty():
        # Get and remove the top node x from the queue
        x = q.get()
        # Loop through the neighbours of x
        for y in G.adjacent(x):
            # If y has been seen then continue
            if y in seen:
                continue
            # Add y to seen and the queue
            seen.add(y)
            q.put(y)
            # By the BFS invariant, the shortest path from s to y is
            # s to x and then x to y
            dist[y] = dist[x] + 1
    return dist


if __name__ == "__main__":
    # A few tests
    G = Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge(1, 2)

    component = breadth_first_search(G, 1)
    assert component == {1, 2}

    component = breadth_first_search(G, 3)
    assert component == {3}

    assert connected_components(G) == [{1, 2}, {3}]

    assert is_connected(G) == False

    G.add_edge(2, 3)
    assert connected_components(G) == [{1, 2, 3}]
    assert is_connected(G) == True

    G.add_node(4)
    G.add_edge(2, 4)

    assert shortest_path(G, 1) == {1: 0, 2: 1, 3: 2, 4: 2}
