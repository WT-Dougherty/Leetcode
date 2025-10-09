"""
Rotate Image - LeetCode Problem 48

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

import time


class Solution:
    def rotate(self, matrix):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    solution.rotate(matrix1)
    assert (
        matrix1 == expected1
    ), f"Failed for matrix1, expected {expected1}, got {matrix1}"

    # Test Case 2: 4x4 matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    solution.rotate(matrix2)
    assert (
        matrix2 == expected2
    ), f"Failed for matrix2, expected {expected2}, got {matrix2}"

    # Test Case 3: Single element
    matrix3 = [[1]]
    expected3 = [[1]]
    solution.rotate(matrix3)
    assert (
        matrix3 == expected3
    ), f"Failed for matrix3, expected {expected3}, got {matrix3}"

    # Test Case 4: 2x2 matrix
    matrix4 = [[1, 2], [3, 4]]
    expected4 = [[3, 1], [4, 2]]
    solution.rotate(matrix4)
    assert (
        matrix4 == expected4
    ), f"Failed for matrix4, expected {expected4}, got {matrix4}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n^2)"""
    solution = Solution()

    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        matrix = [[i * size + j for j in range(size)] for i in range(size)]

        start_time = time.time()
        solution.rotate(matrix)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {size}x{size} matrix")

    # Verify O(n^2) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] * test_sizes[i]) / (
                test_sizes[i - 1] * test_sizes[i - 1]
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n^2): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n^2)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n^2), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n^2)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Single element
    matrix = [[42]]
    solution.rotate(matrix)
    print(f"Single element: {matrix} ✅")

    # Edge Case 2: 2x2 matrix
    matrix = [[1, 2], [3, 4]]
    solution.rotate(matrix)
    print(f"2x2 matrix: {matrix} ✅")

    # Edge Case 3: Large matrix
    matrix = [[i * 100 + j for j in range(100)] for i in range(100)]
    solution.rotate(matrix)
    print(f"Large matrix (100x100): rotated ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large matrix
    size = 1000
    matrix = [[i * size + j for j in range(size)] for i in range(size)]

    start_time = time.time()
    solution.rotate(matrix)
    elapsed_time = time.time() - start_time

    print(f"Large matrix ({size}x{size}):")
    print(f"Time: {elapsed_time:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Rotate Image Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the rotate method")
        print("- Aim for O(n^2) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n^2)")
        print("- Consider using transpose and reverse approach")
