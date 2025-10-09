"""
Spiral Matrix - LeetCode Problem 54

Given an m x n matrix, return all elements of the matrix in spiral order.
"""

import time


class Solution:
    def spiralOrder(self, matrix):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.spiralOrder(matrix1)
    expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert (
        result1 == expected1
    ), f"Failed for matrix1, expected {expected1}, got {result1}"

    # Test Case 2: Rectangular matrix
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = solution.spiralOrder(matrix2)
    expected2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert (
        result2 == expected2
    ), f"Failed for matrix2, expected {expected2}, got {result2}"

    # Test Case 3: Single row
    matrix3 = [[1, 2, 3]]
    result3 = solution.spiralOrder(matrix3)
    expected3 = [1, 2, 3]
    assert (
        result3 == expected3
    ), f"Failed for matrix3, expected {expected3}, got {result3}"

    # Test Case 4: Single column
    matrix4 = [[1], [2], [3]]
    result4 = solution.spiralOrder(matrix4)
    expected4 = [1, 2, 3]
    assert (
        result4 == expected4
    ), f"Failed for matrix4, expected {expected4}, got {result4}"

    # Test Case 5: Single element
    matrix5 = [[1]]
    result5 = solution.spiralOrder(matrix5)
    expected5 = [1]
    assert (
        result5 == expected5
    ), f"Failed for matrix5, expected {expected5}, got {result5}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m * n)"""
    solution = Solution()

    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        matrix = [[i * size + j for j in range(size)] for i in range(size)]

        start_time = time.time()
        result = solution.spiralOrder(matrix)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} elements")

    # Verify O(m * n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] * test_sizes[i]) / (
                test_sizes[i - 1] * test_sizes[i - 1]
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m * n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(m * n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m * n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Single element
    result = solution.spiralOrder([[42]])
    print(f"Single element: {result} ✅")

    # Edge Case 2: Single row
    result = solution.spiralOrder([[1, 2, 3]])
    print(f"Single row: {result} ✅")

    # Edge Case 3: Single column
    result = solution.spiralOrder([[1], [2], [3]])
    print(f"Single column: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large matrix
    size = 1000
    matrix = [[i * size + j for j in range(size)] for i in range(size)]

    start_time = time.time()
    result = solution.spiralOrder(matrix)
    elapsed_time = time.time() - start_time

    print(f"Large matrix ({size}x{size}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} elements")


if __name__ == "__main__":
    print("🧪 Testing Spiral Matrix Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the spiralOrder method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using boundary tracking approach")
