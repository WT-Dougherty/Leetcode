"""
Counting Bits - LeetCode Problem 338

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""

import time


class Solution:
    def countBits(self, n):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    n1 = 2
    result1 = solution.countBits(n1)
    expected1 = [0, 1, 1]
    assert (
        result1 == expected1
    ), f"Failed for n={n1}, expected {expected1}, got {result1}"

    # Test Case 2: Larger case
    n2 = 5
    result2 = solution.countBits(n2)
    expected2 = [0, 1, 1, 2, 1, 2]
    assert (
        result2 == expected2
    ), f"Failed for n={n2}, expected {expected2}, got {result2}"

    # Test Case 3: Single element
    n3 = 0
    result3 = solution.countBits(n3)
    expected3 = [0]
    assert (
        result3 == expected3
    ), f"Failed for n={n3}, expected {expected3}, got {result3}"

    # Test Case 4: Power of 2
    n4 = 8
    result4 = solution.countBits(n4)
    expected4 = [0, 1, 1, 2, 1, 2, 2, 3, 1]
    assert (
        result4 == expected4
    ), f"Failed for n={n4}, expected {expected4}, got {result4}"

    # Test Case 5: Edge case
    n5 = 1
    result5 = solution.countBits(n5)
    expected5 = [0, 1]
    assert (
        result5 == expected5
    ), f"Failed for n={n5}, expected {expected5}, got {result5}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        start_time = time.time()
        result = solution.countBits(size)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {len(result)} elements")

    # Verify O(n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Zero
    result = solution.countBits(0)
    print(f"Zero: {result} ✅")

    # Edge Case 2: Single element
    result = solution.countBits(1)
    print(f"Single element: {result} ✅")

    # Edge Case 3: Large number
    result = solution.countBits(1000)
    print(f"Large number: {len(result)} elements ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    n = 100000

    start_time = time.time()
    result = solution.countBits(n)
    elapsed_time = time.time() - start_time

    print(f"Large number (n={n}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} elements")


if __name__ == "__main__":
    print("🧪 Testing Counting Bits Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the countBits method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using dynamic programming approach")
