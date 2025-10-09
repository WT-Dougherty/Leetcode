"""
Number of Connected Components in an Undirected Graph - LeetCode Problem 323

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array
edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.
"""

import time
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Two components
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    result1 = solution.countComponents(n1, edges1)
    assert result1 == 2, f"Failed for two components, expected 2, got {result1}"

    # Test Case 2: One component
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    result2 = solution.countComponents(n2, edges2)
    assert result2 == 1, f"Failed for one component, expected 1, got {result2}"

    # Test Case 3: No edges
    n3 = 3
    edges3 = []
    result3 = solution.countComponents(n3, edges3)
    assert result3 == 3, f"Failed for no edges, expected 3, got {result3}"

    # Test Case 4: Single node
    n4 = 1
    edges4 = []
    result4 = solution.countComponents(n4, edges4)
    assert result4 == 1, f"Failed for single node, expected 1, got {result4}"

    # Test Case 5: Three components
    n5 = 6
    edges5 = [[0, 1], [2, 3], [4, 5]]
    result5 = solution.countComponents(n5, edges5)
    assert result5 == 3, f"Failed for three components, expected 3, got {result5}"

    # Test Case 6: Complex graph
    n6 = 8
    edges6 = [[0, 1], [1, 2], [3, 4], [4, 5], [6, 7]]
    result6 = solution.countComponents(n6, edges6)
    assert result6 == 3, f"Failed for complex graph, expected 3, got {result6}"

    # Test Case 7: Star graph
    n7 = 4
    edges7 = [[0, 1], [0, 2], [0, 3]]
    result7 = solution.countComponents(n7, edges7)
    assert result7 == 1, f"Failed for star graph, expected 1, got {result7}"

    # Test Case 8: Linear graph
    n8 = 4
    edges8 = [[0, 1], [1, 2], [2, 3]]
    result8 = solution.countComponents(n8, edges8)
    assert result8 == 1, f"Failed for linear graph, expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Nodes\tEdges\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create multiple components
        edges = []
        for i in range(0, size - 1, 2):
            edges.append([i, i + 1])

        # Test approach
        start_time = time.time()
        result = solution.countComponents(size, edges)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(edges)}\t{elapsed_time:.6f}s\t{result}")

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
            prev_complexity = test_sizes[i - 1] + len(edges) // 2
            curr_complexity = test_sizes[i] + len(edges) // 2
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(V+E): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance
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
    result1 = solution.countComponents(1, [])
    assert result1 == 1, f"Single node failed: {result1}"
    print(f"Single node: ✅")

    # Edge Case 2: Maximum constraint (2000 nodes)
    edges2 = []
    for i in range(0, 2000, 2):
        edges2.append([i, i + 1])

    result2 = solution.countComponents(2000, edges2)
    assert result2 == 1000, f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum edges (5000)
    edges3 = []
    for i in range(5000):
        edges3.append([i % 2000, (i + 1) % 2000])

    result3 = solution.countComponents(2000, edges3)
    assert isinstance(result3, int), f"Max edges failed: {result3}"
    print(f"Maximum edges: ✅")

    # Edge Case 4: Self-loop (should be ignored per constraints)
    result4 = solution.countComponents(2, [[0, 0]])
    assert isinstance(result4, int), f"Self-loop failed: {result4}"
    print(f"Self-loop: ✅")

    # Edge Case 5: Large number of components
    edges5 = []
    result5 = solution.countComponents(100, edges5)
    assert result5 == 100, f"Large components failed: {result5}"
    print(f"Large components: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Connected Components:")

    # Large dataset
    n = 1000
    edges = []
    for i in range(0, 1000, 2):
        edges.append([i, i + 1])

    start_time = time.time()
    result = solution.countComponents(n, edges)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 nodes, 500 edges):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Number of Connected Components Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the countComponents method")
        print("- Aim for O(V + E) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(V + E)")
        print("- Consider using DFS, BFS, or Union-Find")
