from dataclasses import dataclass

ID = int


@dataclass
class Node:
    uid: ID
    parent: ID = None
    rank: int = 0


class UnionFind:
    def __init__(self) -> None:
        self.nodes: dict[ID, Node] = {}

    def add(self, uid: ID) -> None:
        # If uid is already in the collection then return
        if uid in self.nodes:
            return

        # Otherwise add it to the collection in a new set with rank 0
        self.nodes[uid] = Node(uid)

    def find(self, uid: ID) -> ID | None:
        # If uid is not in the collection then return
        if uid not in self.nodes:
            return None

        # Search for the representative element of uid.
        cid = uid
        while self.nodes[cid].parent != None:
            # Perform path-splitting while searching for the representative element
            parent = self.nodes[cid].parent
            grandparent = self.nodes[parent].parent
            cid, self.nodes[cid].parent = parent, grandparent
        return cid

    def union(self, uid: ID, vid: ID) -> None:
        # Find the representative element of each node
        uset = self.find(uid)
        vset = self.find(vid)

        # If either element is not in the collection then return
        if uset == None or vset == None:
            return

        # If the elements are already in the same set then return
        if uset == vset:
            return

        # Find the element with the lower rank to merge into
        if self.nodes[uset].rank < self.nodes[vset].rank:
            uset, vset = vset, uset

        # Union-by-rank
        self.nodes[vset].parent = uset
        if self.nodes[uset].rank == self.nodes[vset].rank:
            self.nodes[uset].rank += 1


if __name__ == "__main__":
    # A few tests
    U = UnionFind()
    U.add(1)
    U.add(2)
    U.add(3)
    U.add(4)

    assert U.find(1) == 1
    assert U.find(2) == 2

    U.union(1, 2)
    assert U.find(1) == U.find(2)

    U.union(3, 4)
    assert U.find(3) == U.find(4)

    assert U.find(1) != U.find(3)

    U.union(1, 3)
    assert U.find(1) == U.find(2) == U.find(3) == U.find(4)
