"""
Network Delay Time - LeetCode Problem 743

You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the
source node, vi is the target node, and wi is the time it takes for a signal to travel.
"""

import time
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    result1 = solution.networkDelayTime(times1, n1, k1)
    assert result1 == 2, f"Failed for basic case, expected 2, got {result1}"

    # Test Case 2: Single edge
    times2 = [[1, 2, 1]]
    n2, k2 = 2, 1
    result2 = solution.networkDelayTime(times2, n2, k2)
    assert result2 == 1, f"Failed for single edge, expected 1, got {result2}"

    # Test Case 3: No path
    times3 = [[1, 2, 1]]
    n3, k3 = 2, 2
    result3 = solution.networkDelayTime(times3, n3, k3)
    assert result3 == -1, f"Failed for no path, expected -1, got {result3}"

    # Test Case 4: Single node
    times4 = []
    n4, k4 = 1, 1
    result4 = solution.networkDelayTime(times4, n4, k4)
    assert result4 == 0, f"Failed for single node, expected 0, got {result4}"

    # Test Case 5: Multiple paths
    times5 = [[1, 2, 1], [2, 3, 1], [1, 3, 3]]
    n5, k5 = 3, 1
    result5 = solution.networkDelayTime(times5, n5, k5)
    assert result5 == 2, f"Failed for multiple paths, expected 2, got {result5}"

    # Test Case 6: Complex case
    times6 = [
        [1, 2, 1],
        [2, 3, 1],
        [3, 4, 1],
        [4, 5, 1],
        [1, 5, 5],
    ]
    n6, k6 = 5, 1
    result6 = solution.networkDelayTime(times6, n6, k6)
    assert result6 == 4, f"Failed for complex case, expected 4, got {result6}"

    # Test Case 7: Disconnected graph
    times7 = [[1, 2, 1], [3, 4, 1]]
    n7, k7 = 4, 1
    result7 = solution.networkDelayTime(times7, n7, k7)
    assert result7 == -1, f"Failed for disconnected graph, expected -1, got {result7}"

    # Test Case 8: Self-loop
    times8 = [[1, 1, 1], [1, 2, 1]]
    n8, k8 = 2, 1
    result8 = solution.networkDelayTime(times8, n8, k8)
    assert result8 == 1, f"Failed for self-loop, expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Nodes\tEdges\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create a connected graph
        times_list = []
        for i in range(1, size):
            times_list.append([i, i + 1, 1])
        # Add some additional edges
        for i in range(1, min(size, 20)):
            times_list.append([1, i + 1, i])

        n, k = size, 1

        # Test approach
        start_time = time.time()
        result = solution.networkDelayTime(times_list, n, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(times_list)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(E * log V) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(E * log V) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (test_sizes[i - 1] + min(test_sizes[i - 1], 20)) * (
                test_sizes[i - 1].bit_length()
            )
            curr_complexity = (test_sizes[i] + min(test_sizes[i], 20)) * (
                test_sizes[i].bit_length()
            )
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(E*log V): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(E * log V)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(E * log V) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(E * log V), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(E * log V)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 node)
    result1 = solution.networkDelayTime([], 1, 1)
    assert result1 == 0, f"Single node failed: {result1}"
    print(f"Single node: ✅")

    # Edge Case 2: Maximum constraint (100 nodes)
    times2 = []
    for i in range(1, 100):
        times2.append([i, i + 1, 1])

    result2 = solution.networkDelayTime(times2, 100, 1)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum edges (6000 edges)
    times3 = []
    for i in range(1, 101):
        for j in range(1, 101):
            if i != j and len(times3) < 6000:
                times3.append([i, j, 1])

    result3 = solution.networkDelayTime(times3, 100, 1)
    assert isinstance(result3, int), f"Max edges failed: {result3}"
    print(f"Maximum edges: ✅")

    # Edge Case 4: Maximum weight (100)
    times4 = [[1, 2, 100]]
    result4 = solution.networkDelayTime(times4, 2, 1)
    assert result4 == 100, f"Max weight failed: {result4}"
    print(f"Maximum weight: ✅")

    # Edge Case 5: Maximum k (100)
    times5 = []
    for i in range(1, 100):
        times5.append([i, i + 1, 1])

    result5 = solution.networkDelayTime(times5, 100, 100)
    assert isinstance(result5, int), f"Max k failed: {result5}"
    print(f"Maximum k: ✅")

    # Edge Case 6: No edges
    result6 = solution.networkDelayTime([], 3, 1)
    assert result6 == -1, f"No edges failed: {result6}"
    print(f"No edges: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Network Delay Time:")

    # Large dataset
    times = []
    for i in range(1, 50):
        times.append([i, i + 1, 1])
    for i in range(1, 20):
        times.append([1, i + 1, i])

    n, k = 50, 1

    start_time = time.time()
    result = solution.networkDelayTime(times, n, k)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (50 nodes, {len(times)} edges):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Network Delay Time Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the networkDelayTime method")
        print("- Aim for O(E * log V) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(E * log V)")
        print("- Consider using Dijkstra's algorithm with priority queue")
