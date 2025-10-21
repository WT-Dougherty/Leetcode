"""
Graph Valid Tree - LeetCode Problem 261

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array
edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.
"""

import time
from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        UNVISITED, VISITED = 0, 1
        states = [UNVISITED] * n

        def DFS(cur: int, parent: int):
            states[cur] = VISITED
            for nei in g[cur]:
                if states[nei] == VISITED and nei != parent:
                    return False
                elif states[nei] == VISITED:
                    continue
                else:
                    if not DFS(nei, cur):
                        return False
            return True

        cycles = DFS(0, None)
        for s in states:
            if s == UNVISITED:
                return False
        return cycles


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Valid tree
    n1 = 5
    edges1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
    result1 = solution.validTree(n1, edges1)
    assert result1 == True, f"Failed for valid tree, expected True, got {result1}"

    # Test Case 2: Invalid tree (cycle)
    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    result2 = solution.validTree(n2, edges2)
    assert result2 == False, f"Failed for cycle, expected False, got {result2}"

    # Test Case 3: Single node
    n3 = 1
    edges3 = []
    result3 = solution.validTree(n3, edges3)
    assert result3 == True, f"Failed for single node, expected True, got {result3}"

    # Test Case 4: Two nodes
    n4 = 2
    edges4 = [[0, 1]]
    result4 = solution.validTree(n4, edges4)
    assert result4 == True, f"Failed for two nodes, expected True, got {result4}"

    # Test Case 6: Too many edges
    n6 = 3
    edges6 = [[0, 1], [1, 2], [0, 2]]
    result6 = solution.validTree(n6, edges6)
    assert result6 == False, f"Failed for too many edges, expected False, got {result6}"

    # Test Case 7: Linear tree
    n7 = 4
    edges7 = [[0, 1], [1, 2], [2, 3]]
    result7 = solution.validTree(n7, edges7)
    assert result7 == True, f"Failed for linear tree, expected True, got {result7}"

    # Test Case 8: Star tree
    n8 = 4
    edges8 = [[0, 1], [0, 2], [0, 3]]
    result8 = solution.validTree(n8, edges8)
    assert result8 == True, f"Failed for star tree, expected True, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500]
    times = []

    print("\nTime Complexity Analysis:")
    print("Nodes\tEdges\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create a valid tree
        edges = []
        for i in range(size - 1):
            edges.append([i, i + 1])

        # Test approach
        start_time = time.time()
        result = solution.validTree(size, edges)
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
            prev_complexity = test_sizes[i - 1] + (test_sizes[i - 1] - 1)
            curr_complexity = test_sizes[i] + (test_sizes[i] - 1)
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
    result1 = solution.validTree(1, [])
    assert result1 == True, f"Single node failed: {result1}"
    print(f"Single node: ✅")

    # Edge Case 4: Self-loop (should be invalid)
    result4 = solution.validTree(2, [[0, 0]])
    assert result4 == False, f"Self-loop failed: {result4}"
    print(f"Self-loop: ✅")

    # Edge Case 5: Large cycle
    edges5 = []
    for i in range(100):
        edges5.append([i, (i + 1) % 100])

    result5 = solution.validTree(100, edges5)
    assert result5 == False, f"Large cycle failed: {result5}"
    print(f"Large cycle: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Graph Valid Tree:")

    # Large dataset
    n = 1000
    edges = []
    for i in range(999):
        edges.append([i, i + 1])

    start_time = time.time()
    result = solution.validTree(n, edges)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 nodes, 999 edges):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Graph Valid Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    # benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the validTree method")
        print("- Aim for O(V + E) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(V + E)")
        print("- Consider using Union-Find or DFS with cycle detection")
