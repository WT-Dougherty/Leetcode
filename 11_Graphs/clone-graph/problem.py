"""
Clone Graph - LeetCode Problem 133

Given a reference of a node in a connected undirected graph, return a deep copy (clone)
of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
"""

import time
from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        head: Node = Node(node.val)
        seen = dict()

        def DFS(new: Node, old: Node) -> None:
            if new.val in seen:
                return
            seen[new.val] = new
            for nei in old.neighbors:
                if nei.val in seen:
                    new.neighbors.append(seen[nei.val])
                else:
                    new_node = Node(nei.val)
                    new.neighbors.append(new_node)
                    DFS(new_node, nei)

        DFS(head, node)
        return head


def create_graph_from_adj_list(adjList: List[List[int]]) -> Node:
    """Helper function to create a graph from adjacency list"""
    if not adjList:
        return None

    nodes = {}
    n = len(adjList)

    # Create all nodes
    for i in range(n):
        nodes[i + 1] = Node(i + 1)

    # Connect neighbors
    for i, neighbors in enumerate(adjList):
        node = nodes[i + 1]
        for neighbor_val in neighbors:
            node.neighbors.append(nodes[neighbor_val])

    return nodes[1] if nodes else None


def graph_to_adj_list(node: Node) -> List[List[int]]:
    """Helper function to convert graph to adjacency list"""
    if not node:
        return []

    visited = set()
    adj_list = {}

    def dfs(n):
        if n.val in visited:
            return
        visited.add(n.val)
        adj_list[n.val] = [neighbor.val for neighbor in n.neighbors]
        for neighbor in n.neighbors:
            dfs(neighbor)

    dfs(node)

    # Convert to list format
    result = []
    for i in range(1, len(adj_list) + 1):
        result.append(adj_list[i])

    return result


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = create_graph_from_adj_list(adjList1)
    cloned1 = solution.cloneGraph(graph1)
    result1 = graph_to_adj_list(cloned1)
    assert (
        result1 == adjList1
    ), f"Failed for basic case, expected {adjList1}, got {result1}"

    # Test Case 2: Single node
    adjList2 = [[]]
    graph2 = create_graph_from_adj_list(adjList2)
    cloned2 = solution.cloneGraph(graph2)
    result2 = graph_to_adj_list(cloned2)
    assert (
        result2 == adjList2
    ), f"Failed for single node, expected {adjList2}, got {result2}"

    # Test Case 3: Empty graph
    graph3 = None
    cloned3 = solution.cloneGraph(graph3)
    assert cloned3 == None, f"Failed for empty graph, expected None, got {cloned3}"

    # Test Case 4: Two nodes
    adjList4 = [[2], [1]]
    graph4 = create_graph_from_adj_list(adjList4)
    cloned4 = solution.cloneGraph(graph4)
    result4 = graph_to_adj_list(cloned4)
    assert (
        result4 == adjList4
    ), f"Failed for two nodes, expected {adjList4}, got {result4}"

    # Test Case 5: Linear graph
    adjList5 = [[2], [1, 3], [2]]
    graph5 = create_graph_from_adj_list(adjList5)
    cloned5 = solution.cloneGraph(graph5)
    result5 = graph_to_adj_list(cloned5)
    assert (
        result5 == adjList5
    ), f"Failed for linear graph, expected {adjList5}, got {result5}"

    # Test Case 6: Complete graph
    adjList6 = [[2, 3], [1, 3], [1, 2]]
    graph6 = create_graph_from_adj_list(adjList6)
    cloned6 = solution.cloneGraph(graph6)
    result6 = graph_to_adj_list(cloned6)
    assert (
        result6 == adjList6
    ), f"Failed for complete graph, expected {adjList6}, got {result6}"

    # Test Case 7: Star graph
    adjList7 = [[2, 3, 4], [1], [1], [1]]
    graph7 = create_graph_from_adj_list(adjList7)
    cloned7 = solution.cloneGraph(graph7)
    result7 = graph_to_adj_list(cloned7)
    assert (
        result7 == adjList7
    ), f"Failed for star graph, expected {adjList7}, got {result7}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - complete graph
        adjList = []
        for i in range(size):
            neighbors = [j + 1 for j in range(size) if j != i]
            adjList.append(neighbors)

        graph = create_graph_from_adj_list(adjList)

        # Test approach
        start_time = time.time()
        cloned = solution.cloneGraph(graph)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        result = graph_to_adj_list(cloned)
        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} nodes")

    # Verify O(V + E) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(V + E) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            # For complete graph: V + E = n + n(n-1) = n^2
            prev_complexity = test_sizes[i - 1] ** 2
            curr_complexity = test_sizes[i] ** 2
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(V+E): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(V + E)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(V + E) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(V + E), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(V + E)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 node)
    adjList1 = [[]]
    graph1 = create_graph_from_adj_list(adjList1)
    cloned1 = solution.cloneGraph(graph1)
    result1 = graph_to_adj_list(cloned1)
    assert result1 == adjList1, f"Single node failed: {result1}"
    print(f"Single node: ✅")

    # Edge Case 3: Self-loop (should not happen per constraints, but test robustness)
    adjList3 = [[1]]
    graph3 = create_graph_from_adj_list(adjList3)
    cloned3 = solution.cloneGraph(graph3)
    result3 = graph_to_adj_list(cloned3)
    assert result3 == adjList3, f"Self-loop failed: {result3}"
    print(f"Self-loop: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Clone Graph:")

    # Large dataset
    adjList = []
    for i in range(50):
        neighbors = [j + 1 for j in range(50) if j != i]
        adjList.append(neighbors)

    graph = create_graph_from_adj_list(adjList)

    start_time = time.time()
    cloned = solution.cloneGraph(graph)
    elapsed_time = time.time() - start_time

    result = graph_to_adj_list(cloned)
    print(f"Large dataset (50 nodes, complete graph):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} nodes")


if __name__ == "__main__":
    print("🧪 Testing Clone Graph Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the cloneGraph method")
        print("- Aim for O(V + E) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(V + E)")
        print("- Consider using DFS with hash map for visited nodes")
