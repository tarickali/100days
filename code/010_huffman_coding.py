import heapq


def huffman(weighted_symbols: dict[str, int]) -> dict[str, str]:
    # Create the nodes of the "tree"
    nodes = [(weight, symbol) for symbol, weight in weighted_symbols.items()]

    # Heapify the nodes to allow for O(log n) extract minimum operations
    heapq.heapify(nodes)

    codes = {}
    while len(nodes) > 1:
        # Get the two lowest weight nodes in the "tree"
        weight_a, symbol_a = heapq.heappop(nodes)
        weight_b, symbol_b = heapq.heappop(nodes)

        # Update the codes for each subsymbol of symbol a and b
        for c in symbol_a:
            # Prefix subsymbols of symbol a with 0
            codes[c] = "0" + codes.get(c, "")
        for c in symbol_b:
            # Prefix subsymbols of symbol b with 1
            codes[c] = "1" + codes.get(c, "")

        # Add the merged back to the "tree"
        heapq.heappush(nodes, (weight_a + weight_b, symbol_a + symbol_b))

    # Determine the weighted path length objective value of the computed code
    weighted_path_length = sum(len(codes[s]) * weighted_symbols[s] for s in codes)
    return codes, weighted_path_length


if __name__ == "__main__":
    # A few tests
    weighted_symbols = {"a": 4, "b": 2, "c": 1, "d": 0, "e": 3}
    codes, weighted_path_length = huffman(weighted_symbols)
    print(codes, weighted_path_length)
    assert codes == {"a": "0", "b": "101", "c": "1001", "d": "1000", "e": "11"}

    weighted_symbols = {"a": 4, "b": 4, "c": 2, "d": 2, "e": 5}
    codes, weighted_path_length = huffman(weighted_symbols)
    print(codes, weighted_path_length)
    assert codes == {"a": "00", "b": "01", "c": "100", "d": "101", "e": "11"}
