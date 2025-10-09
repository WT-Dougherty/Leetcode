"""
Min Cost to Connect All Points - LeetCode Problem 1584

You are given an array of points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].
"""

import time
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    result1 = solution.minCostConnectPoints(points1)
    assert result1 == 20, f"Failed for basic case, expected 20, got {result1}"

    # Test Case 2: Three points
    points2 = [[3, 12], [-2, 5], [-4, 1]]
    result2 = solution.minCostConnectPoints(points2)
    assert result2 == 18, f"Failed for three points, expected 18, got {result2}"

    # Test Case 3: Four points
    points3 = [[0, 0], [1, 1], [1, 0], [-1, 1]]
    result3 = solution.minCostConnectPoints(points3)
    assert result3 == 4, f"Failed for four points, expected 4, got {result3}"

    # Test Case 4: Two points
    points4 = [[0, 0], [1, 1]]
    result4 = solution.minCostConnectPoints(points4)
    assert result4 == 2, f"Failed for two points, expected 2, got {result4}"

    # Test Case 5: Single point
    points5 = [[0, 0]]
    result5 = solution.minCostConnectPoints(points5)
    assert result5 == 0, f"Failed for single point, expected 0, got {result5}"

    # Test Case 6: Linear points
    points6 = [[0, 0], [1, 0], [2, 0], [3, 0]]
    result6 = solution.minCostConnectPoints(points6)
    assert result6 == 3, f"Failed for linear points, expected 3, got {result6}"

    # Test Case 7: Square points
    points7 = [[0, 0], [0, 1], [1, 0], [1, 1]]
    result7 = solution.minCostConnectPoints(points7)
    assert result7 == 3, f"Failed for square points, expected 3, got {result7}"

    # Test Case 8: Complex case
    points8 = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1]]
    result8 = solution.minCostConnectPoints(points8)
    assert result8 == 5, f"Failed for complex case, expected 5, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Points\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create points in a grid pattern
        points = []
        for i in range(size):
            x = i % 10
            y = i // 10
            points.append([x, y])

        # Test approach
        start_time = time.time()
        result = solution.minCostConnectPoints(points)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n^2 * log n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n^2 * log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = (test_sizes[i - 1] ** 2) * (
                test_sizes[i - 1].bit_length()
            )
            curr_complexity = (test_sizes[i] ** 2) * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n^2*log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 3.0  # Allow 300% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^2 * log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n^2 * log n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n^2 * log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^2 * log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 point)
    points1 = [[0, 0]]
    result1 = solution.minCostConnectPoints(points1)
    assert result1 == 0, f"Single point failed: {result1}"
    print(f"Single point: ✅")

    # Edge Case 2: Maximum constraint (1000 points)
    points2 = []
    for i in range(1000):
        x = i % 100
        y = i // 100
        points2.append([x, y])

    result2 = solution.minCostConnectPoints(points2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum coordinate values
    points3 = [[-10**6, -10**6], [10**6, 10**6]]
    result3 = solution.minCostConnectPoints(points3)
    assert result3 == 4 * 10**6, f"Max coordinates failed: {result3}"
    print(f"Maximum coordinates: ✅")

    # Edge Case 4: Minimum coordinate values
    points4 = [[-10**6, -10**6], [-10**6, -10**6]]
    result4 = solution.minCostConnectPoints(points4)
    assert result4 == 0, f"Min coordinates failed: {result4}"
    print(f"Minimum coordinates: ✅")

    # Edge Case 5: All same points
    points5 = [[0, 0], [0, 0], [0, 0]]
    result5 = solution.minCostConnectPoints(points5)
    assert result5 == 0, f"All same points failed: {result5}"
    print(f"All same points: ✅")

    # Edge Case 6: Large distances
    points6 = [[0, 0], [1000, 1000], [2000, 2000]]
    result6 = solution.minCostConnectPoints(points6)
    assert result6 == 4000, f"Large distances failed: {result6}"
    print(f"Large distances: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Min Cost to Connect All Points:")

    # Large dataset
    points = []
    for i in range(100):
        x = i % 10
        y = i // 10
        points.append([x, y])

    start_time = time.time()
    result = solution.minCostConnectPoints(points)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100 points):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Min Cost to Connect All Points Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minCostConnectPoints method")
        print("- Aim for O(n^2 * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^2 * log n)")
        print("- Consider using Kruskal's or Prim's algorithm")
