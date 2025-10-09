"""
K Closest Points to Origin - LeetCode Problem 973

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).
"""

import time
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    points1 = [[1, 1], [2, 2], [3, 3]]
    k1 = 1
    result1 = solution.kClosest(points1, k1)
    expected1 = [[1, 1]]
    assert (
        result1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {result1}"

    # Test Case 2: Multiple closest points
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    result2 = solution.kClosest(points2, k2)
    expected2 = [[3, 3], [-2, 4]]
    assert set(tuple(p) for p in result2) == set(
        tuple(p) for p in expected2
    ), f"Failed for multiple points, expected {expected2}, got {result2}"

    # Test Case 3: All points
    points3 = [[1, 1], [2, 2], [3, 3]]
    k3 = 3
    result3 = solution.kClosest(points3, k3)
    expected3 = [[1, 1], [2, 2], [3, 3]]
    assert set(tuple(p) for p in result3) == set(
        tuple(p) for p in expected3
    ), f"Failed for all points, expected {expected3}, got {result3}"

    # Test Case 4: Single point
    points4 = [[1, 1]]
    k4 = 1
    result4 = solution.kClosest(points4, k4)
    expected4 = [[1, 1]]
    assert (
        result4 == expected4
    ), f"Failed for single point, expected {expected4}, got {result4}"

    # Test Case 5: Negative coordinates
    points5 = [[-1, -1], [-2, -2], [1, 1]]
    k5 = 2
    result5 = solution.kClosest(points5, k5)
    expected5 = [[-1, -1], [1, 1]]
    assert set(tuple(p) for p in result5) == set(
        tuple(p) for p in expected5
    ), f"Failed for negative coordinates, expected {expected5}, got {result5}"

    # Test Case 6: Zero coordinates
    points6 = [[0, 0], [1, 1], [2, 2]]
    k6 = 1
    result6 = solution.kClosest(points6, k6)
    expected6 = [[0, 0]]
    assert (
        result6 == expected6
    ), f"Failed for zero coordinates, expected {expected6}, got {result6}"

    # Test Case 7: Large coordinates
    points7 = [[10000, 10000], [1, 1], [2, 2]]
    k7 = 2
    result7 = solution.kClosest(points7, k7)
    expected7 = [[1, 1], [2, 2]]
    assert set(tuple(p) for p in result7) == set(
        tuple(p) for p in expected7
    ), f"Failed for large coordinates, expected {expected7}, got {result7}"

    # Test Case 8: Duplicate distances
    points8 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    k8 = 2
    result8 = solution.kClosest(points8, k8)
    assert (
        len(result8) == 2
    ), f"Failed for duplicate distances, expected 2 points, got {len(result8)}"
    for point in result8:
        assert point in [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ], f"Invalid point in result: {point}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tK\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data
        points = [[i, i] for i in range(size)]
        k = min(100, size // 10)  # Keep k reasonable

        # Test approach
        start_time = time.time()
        result = solution.kClosest(points, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{k}\t{elapsed_time:.6f}s\t{len(result)} points")

    # Verify O(n log k) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log k) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log k): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log k)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n log k) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n log k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n log k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 point, k=1)
    points1 = [[42, 42]]
    result1 = solution.kClosest(points1, 1)
    assert result1 == [[42, 42]], f"Single point failed: {result1}"
    print(f"Single point: ✅")

    # Edge Case 2: Maximum constraint values
    points2 = [[10000, 10000], [-10000, -10000], [0, 0]]
    result2 = solution.kClosest(points2, 2)
    assert len(result2) == 2, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All points at origin
    points3 = [[0, 0], [0, 0], [0, 0]]
    result3 = solution.kClosest(points3, 2)
    assert len(result3) == 2, f"All points at origin failed: {result3}"
    print(f"All points at origin: ✅")

    # Edge Case 4: k equals number of points
    points4 = [[1, 1], [2, 2], [3, 3]]
    result4 = solution.kClosest(points4, 3)
    assert len(result4) == 3, f"k equals n failed: {result4}"
    print(f"k equals number of points: ✅")

    # Edge Case 5: Large k
    points5 = [[i, i] for i in range(100)]
    result5 = solution.kClosest(points5, 50)
    assert len(result5) == 50, f"Large k failed: {result5}"
    print(f"Large k: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking K Closest Points:")

    # Large dataset
    points = [[i, i] for i in range(10000)]
    k = 100

    start_time = time.time()
    result = solution.kClosest(points, k)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10,000 points, k=100):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} points")


if __name__ == "__main__":
    print("🧪 Testing K Closest Points to Origin Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the kClosest method")
        print("- Aim for O(n log k) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log k)")
        print("- Consider using a max heap of size k")
