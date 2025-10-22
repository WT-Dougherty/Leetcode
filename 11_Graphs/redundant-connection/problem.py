"""
Redundant Connection - LeetCode Problem 684

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one
additional edge added.
"""

import time
from collections import defaultdict, deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(1, len(edges) + 1)]
        rank = [1 for _ in range(len(edges))]

        def find(n):
            p = parent[n - 1]
            while p != parent[p - 1]:
                p = parent[p - 1]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            elif rank[p1 - 1] >= rank[p2 - 1]:
                parent[p2 - 1] = parent[p1 - 1]
                rank[p1 - 1] += rank[p2 - 1]
            else:
                parent[p1 - 1] = parent[p2 - 1]
                rank[p2 - 1] += rank[p1 - 1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        return edges[-1]


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    edges1 = [[1, 2], [1, 3], [2, 3]]
    result1 = solution.findRedundantConnection(edges1)
    expected1 = [2, 3]
    assert (
        result1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {result1}"

    # Test Case 2: Another case
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    result2 = solution.findRedundantConnection(edges2)
    expected2 = [1, 4]
    assert (
        result2 == expected2
    ), f"Failed for another case, expected {expected2}, got {result2}"

    # Test Case 3: Linear tree with cycle
    edges3 = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    result3 = solution.findRedundantConnection(edges3)
    expected3 = [1, 5]
    assert (
        result3 == expected3
    ), f"Failed for linear tree, expected {expected3}, got {result3}"

    # Test Case 4: Star tree with cycle
    edges4 = [[1, 2], [1, 3], [1, 4], [2, 3]]
    result4 = solution.findRedundantConnection(edges4)
    expected4 = [2, 3]
    assert (
        result4 == expected4
    ), f"Failed for star tree, expected {expected4}, got {result4}"

    # Test Case 5: Complex case
    edges5 = [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [6, 7],
        [7, 8],
        [8, 9],
        [9, 10],
        [1, 10],
    ]
    result5 = solution.findRedundantConnection(edges5)
    expected5 = [1, 10]
    assert (
        result5 == expected5
    ), f"Failed for complex case, expected {expected5}, got {result5}"

    # Test Case 6: Small tree
    edges6 = [[1, 2], [2, 3], [1, 3]]
    result6 = solution.findRedundantConnection(edges6)
    expected6 = [1, 3]
    assert (
        result6 == expected6
    ), f"Failed for small tree, expected {expected6}, got {result6}"

    # Test Case 8: Minimum case
    edges8 = [[1, 2], [2, 3], [1, 3]]
    result8 = solution.findRedundantConnection(edges8)
    expected8 = [1, 3]
    assert (
        result8 == expected8
    ), f"Failed for minimum case, expected {expected8}, got {result8}"

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
        # Generate test data - create a tree with one redundant edge
        edges = []
        for i in range(1, size):
            edges.append([i, i + 1])
        # Add redundant edge
        edges.append([1, size])

        # Test approach
        start_time = time.time()
        result = solution.findRedundantConnection(edges)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(edges)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * α(n)) complexity (nearly O(n))
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (3 nodes)
    edges1 = [[1, 2], [2, 3], [1, 3]]
    result1 = solution.findRedundantConnection(edges1)
    assert result1 == [1, 3], f"Minimum constraint failed: {result1}"
    print(f"Minimum constraint: ✅")

    # Edge Case 2: Maximum constraint (1000 nodes)
    edges2 = []
    for i in range(1, 1000):
        edges2.append([i, i + 1])
    edges2.append([1, 1000])

    result2 = solution.findRedundantConnection(edges2)
    assert result2 == [1, 1000], f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum edges (1000 edges)
    edges3 = []
    for i in range(1, 1000):
        edges3.append([i, i + 1])
    edges3.append([1, 1000])

    result3 = solution.findRedundantConnection(edges3)
    assert isinstance(result3, list), f"Max edges failed: {result3}"
    print(f"Maximum edges: ✅")

    # Edge Case 4: Self-loop (should not happen per constraints, but test robustness)
    edges4 = [[1, 2], [2, 3], [1, 1]]
    result4 = solution.findRedundantConnection(edges4)
    assert isinstance(result4, list), f"Self-loop failed: {result4}"
    print(f"Self-loop: ✅")

    # Edge Case 5: Large cycle
    edges5 = []
    for i in range(1, 100):
        edges5.append([i, i + 1])
    edges5.append([1, 100])

    result5 = solution.findRedundantConnection(edges5)
    assert result5 == [1, 100], f"Large cycle failed: {result5}"
    print(f"Large cycle: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Redundant Connection:")

    # Large dataset
    edges = []
    for i in range(1, 1000):
        edges.append([i, i + 1])
    edges.append([1, 1000])

    start_time = time.time()
    result = solution.findRedundantConnection(edges)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 nodes, 1000 edges):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Redundant Connection Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findRedundantConnection method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using Union-Find data structure")
