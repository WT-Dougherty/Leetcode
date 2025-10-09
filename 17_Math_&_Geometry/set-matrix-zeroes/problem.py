"""
Set Matrix Zeroes - LeetCode Problem 73

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in-place.
"""

import time


class Solution:
    def setZeroes(self, matrix):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution.setZeroes(matrix1)
    assert (
        matrix1 == expected1
    ), f"Failed for matrix1, expected {expected1}, got {matrix1}"

    # Test Case 2: Complex case
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected2 = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    solution.setZeroes(matrix2)
    assert (
        matrix2 == expected2
    ), f"Failed for matrix2, expected {expected2}, got {matrix2}"

    # Test Case 3: Single element
    matrix3 = [[0]]
    expected3 = [[0]]
    solution.setZeroes(matrix3)
    assert (
        matrix3 == expected3
    ), f"Failed for matrix3, expected {expected3}, got {matrix3}"

    # Test Case 4: No zeros
    matrix4 = [[1, 2], [3, 4]]
    expected4 = [[1, 2], [3, 4]]
    solution.setZeroes(matrix4)
    assert (
        matrix4 == expected4
    ), f"Failed for matrix4, expected {expected4}, got {matrix4}"

    # Test Case 5: All zeros
    matrix5 = [[0, 0], [0, 0]]
    expected5 = [[0, 0], [0, 0]]
    solution.setZeroes(matrix5)
    assert (
        matrix5 == expected5
    ), f"Failed for matrix5, expected {expected5}, got {matrix5}"

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
        matrix = [
            [1 if (i + j) % 2 == 0 else 0 for j in range(size)] for i in range(size)
        ]

        start_time = time.time()
        solution.setZeroes(matrix)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {size}x{size} matrix")

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
    matrix = [[0]]
    solution.setZeroes(matrix)
    print(f"Single element: {matrix} ✅")

    # Edge Case 2: Single row
    matrix = [[1, 0, 1]]
    solution.setZeroes(matrix)
    print(f"Single row: {matrix} ✅")

    # Edge Case 3: Single column
    matrix = [[1], [0], [1]]
    solution.setZeroes(matrix)
    print(f"Single column: {matrix} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large matrix
    size = 1000
    matrix = [[1 if (i + j) % 2 == 0 else 0 for j in range(size)] for i in range(size)]

    start_time = time.time()
    solution.setZeroes(matrix)
    elapsed_time = time.time() - start_time

    print(f"Large matrix ({size}x{size}):")
    print(f"Time: {elapsed_time:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Set Matrix Zeroes Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the setZeroes method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using marker approach")
