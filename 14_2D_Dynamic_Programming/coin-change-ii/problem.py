"""
Coin Change II - LeetCode Problem 518

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that
amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

import time
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    amount1 = 5
    coins1 = [1, 2, 5]
    result1 = solution.change(amount1, coins1)
    assert (
        result1 == 4
    ), f"Failed for amount={amount1}, coins={coins1}, expected 4, got {result1}"

    # Test Case 2: Impossible case
    amount2 = 3
    coins2 = [2]
    result2 = solution.change(amount2, coins2)
    assert (
        result2 == 0
    ), f"Failed for amount={amount2}, coins={coins2}, expected 0, got {result2}"

    # Test Case 3: Single coin
    amount3 = 10
    coins3 = [10]
    result3 = solution.change(amount3, coins3)
    assert (
        result3 == 1
    ), f"Failed for amount={amount3}, coins={coins3}, expected 1, got {result3}"

    # Test Case 4: Zero amount
    amount4 = 0
    coins4 = [1, 2, 5]
    result4 = solution.change(amount4, coins4)
    assert (
        result4 == 1
    ), f"Failed for amount={amount4}, coins={coins4}, expected 1, got {result4}"

    # Test Case 5: Multiple coins
    amount5 = 6
    coins5 = [1, 2, 3]
    result5 = solution.change(amount5, coins5)
    assert (
        result5 == 7
    ), f"Failed for amount={amount5}, coins={coins5}, expected 7, got {result5}"

    # Test Case 6: Large amount
    amount6 = 100
    coins6 = [1, 2, 5]
    result6 = solution.change(amount6, coins6)
    assert (
        result6 == 292
    ), f"Failed for amount={amount6}, coins={coins6}, expected 292, got {result6}"

    # Test Case 7: Complex case
    amount7 = 12
    coins7 = [2, 3, 7]
    result7 = solution.change(amount7, coins7)
    assert (
        result7 == 4
    ), f"Failed for amount={amount7}, coins={coins7}, expected 4, got {result7}"

    # Test Case 8: Edge case
    amount8 = 1
    coins8 = [1]
    result8 = solution.change(amount8, coins8)
    assert (
        result8 == 1
    ), f"Failed for amount={amount8}, coins={coins8}, expected 1, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_amounts = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Amount\tCoins\tTime\t\tResult")
    print("-" * 50)

    for amount in test_amounts:
        # Generate test data - use common coin denominations
        coins = [1, 2, 5, 10, 20, 50]

        # Test approach
        start_time = time.time()
        result = solution.change(amount, coins)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{amount}\t{len(coins)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(amount * coins.length) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(amount * coins.length) complexity
        expected_ratios = []
        for i in range(1, len(test_amounts)):
            prev_complexity = test_amounts[i - 1] * 6  # 6 coins
            curr_complexity = test_amounts[i] * 6
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(amount*coins): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(
                    f"\n❌ FAILED: Time complexity appears worse than O(amount * coins.length)"
                )
                print(
                    f"   Amount {test_amounts[i]} to {test_amounts[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(
                    f"   This suggests worse than O(amount * coins.length) complexity"
                )
                raise AssertionError(
                    f"Time complexity test failed: expected O(amount * coins.length), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(amount * coins.length)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 coin, amount 0)
    result1 = solution.change(0, [1])
    assert result1 == 1, f"Zero amount failed: {result1}"
    print(f"Zero amount: ✅")

    # Edge Case 2: Maximum constraint (300 coins, amount 5000)
    coins2 = [i % 5000 + 1 for i in range(300)]
    result2 = solution.change(5000, coins2)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum coin value (5000)
    result3 = solution.change(5000, [5000])
    assert result3 == 1, f"Max coin value failed: {result3}"
    print(f"Maximum coin value: ✅")

    # Edge Case 4: Single coin denomination
    result4 = solution.change(5, [5])
    assert result4 == 1, f"Single denomination failed: {result4}"
    print(f"Single denomination: ✅")

    # Edge Case 5: All same coins
    result5 = solution.change(10, [1, 1, 1, 1, 1])
    assert result5 == 1, f"All same coins failed: {result5}"
    print(f"All same coins: ✅")

    # Edge Case 6: No matching coins
    result6 = solution.change(1, [2, 3, 4])
    assert result6 == 0, f"No matching coins failed: {result6}"
    print(f"No matching coins: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Coin Change II:")

    # Large dataset
    amount = 1000
    coins = [1, 2, 5, 10, 20, 50]

    start_time = time.time()
    result = solution.change(amount, coins)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (amount=1000, {len(coins)} coins):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Coin Change II Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the change method")
        print("- Aim for O(amount * coins.length) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(amount * coins.length)")
        print("- Consider using dynamic programming")
