"""
Bitwise AND of Numbers Range - LeetCode Problem 201

Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.
"""

import time


class Solution:
    def rangeBitwiseAnd(self, left, right):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    left1, right1 = 5, 7
    result1 = solution.rangeBitwiseAnd(left1, right1)
    assert (
        result1 == 4
    ), f"Failed for left={left1}, right={right1}, expected 4, got {result1}"

    # Test Case 2: Same number
    left2, right2 = 0, 0
    result2 = solution.rangeBitwiseAnd(left2, right2)
    assert (
        result2 == 0
    ), f"Failed for left={left2}, right={right2}, expected 0, got {result2}"

    # Test Case 3: Large range
    left3, right3 = 1, 2147483647
    result3 = solution.rangeBitwiseAnd(left3, right3)
    assert (
        result3 == 0
    ), f"Failed for left={left3}, right={right3}, expected 0, got {result3}"

    # Test Case 4: Small range
    left4, right4 = 1, 1
    result4 = solution.rangeBitwiseAnd(left4, right4)
    assert (
        result4 == 1
    ), f"Failed for left={left4}, right={right4}, expected 1, got {result4}"

    # Test Case 5: Edge case
    left5, right5 = 6, 7
    result5 = solution.rangeBitwiseAnd(left5, right5)
    assert (
        result5 == 6
    ), f"Failed for left={left5}, right={right5}, expected 6, got {result5}"

    # Test Case 6: Power of 2
    left6, right6 = 4, 7
    result6 = solution.rangeBitwiseAnd(left6, right6)
    assert (
        result6 == 4
    ), f"Failed for left={left6}, right={right6}, expected 4, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        left, right = 1, size

        start_time = time.time()
        result = solution.rangeBitwiseAnd(left, right)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(log n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i].bit_length()) / (
                test_sizes[i - 1].bit_length()
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Same number
    result = solution.rangeBitwiseAnd(5, 5)
    print(f"Same number: {result} ✅")

    # Edge Case 2: Consecutive numbers
    result = solution.rangeBitwiseAnd(6, 7)
    print(f"Consecutive numbers: {result} ✅")

    # Edge Case 3: Large range
    result = solution.rangeBitwiseAnd(0, 1000000)
    print(f"Large range: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large range
    left, right = 1, 1000000

    start_time = time.time()
    result = solution.rangeBitwiseAnd(left, right)
    elapsed_time = time.time() - start_time

    print(f"Large range ({left} to {right}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Bitwise AND of Numbers Range Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the rangeBitwiseAnd method")
        print("- Aim for O(log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using bit manipulation techniques")
