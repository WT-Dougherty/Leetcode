"""
Coin Change - LeetCode Problem 322

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    coins1 = [1, 3, 4]
    amount1 = 6
    result1 = solution.coinChange(coins1, amount1)
    assert (
        result1 == 2
    ), f"Failed for coins={coins1}, amount={amount1}, expected 2, got {result1}"

    # Test Case 2: Impossible case
    coins2 = [2]
    amount2 = 3
    result2 = solution.coinChange(coins2, amount2)
    assert (
        result2 == -1
    ), f"Failed for coins={coins2}, amount={amount2}, expected -1, got {result2}"

    # Test Case 3: Zero amount
    coins3 = [1]
    amount3 = 0
    result3 = solution.coinChange(coins3, amount3)
    assert (
        result3 == 0
    ), f"Failed for coins={coins3}, amount={amount3}, expected 0, got {result3}"

    # Test Case 4: Single coin
    coins4 = [1]
    amount4 = 1
    result4 = solution.coinChange(coins4, amount4)
    assert (
        result4 == 1
    ), f"Failed for coins={coins4}, amount={amount4}, expected 1, got {result4}"

    # Test Case 5: Multiple coins
    coins5 = [1, 2, 5]
    amount5 = 11
    result5 = solution.coinChange(coins5, amount5)
    assert (
        result5 == 3
    ), f"Failed for coins={coins5}, amount={amount5}, expected 3, got {result5}"

    # Test Case 6: Large amount
    coins6 = [1, 2, 5]
    amount6 = 100
    result6 = solution.coinChange(coins6, amount6)
    assert (
        result6 == 20
    ), f"Failed for coins={coins6}, amount={amount6}, expected 20, got {result6}"

    # Test Case 7: Complex case
    coins7 = [2, 3, 7]
    amount7 = 12
    result7 = solution.coinChange(coins7, amount7)
    assert (
        result7 == 3
    ), f"Failed for coins={coins7}, amount={amount7}, expected 3, got {result7}"

    # Test Case 8: Edge case with large coins
    coins8 = [1, 2, 5, 10, 20, 50]
    amount8 = 99
    result8 = solution.coinChange(coins8, amount8)
    assert (
        result8 == 6
    ), f"Failed for coins={coins8}, amount={amount8}, expected 6, got {result8}"

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
        result = solution.coinChange(coins, amount)
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
    result1 = solution.coinChange([1], 0)
    assert result1 == 0, f"Zero amount failed: {result1}"
    print(f"Zero amount: ✅")

    # Edge Case 2: Maximum constraint (12 coins, amount 10000)
    coins2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result2 = solution.coinChange(coins2, 10000)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum coin value (2^31 - 1)
    coins3 = [2147483647]
    result3 = solution.coinChange(coins3, 1)
    assert result3 == -1, f"Max coin value failed: {result3}"
    print(f"Maximum coin value: ✅")

    # Edge Case 4: Single coin denomination
    coins4 = [5]
    result4 = solution.coinChange(coins4, 10)
    assert result4 == 2, f"Single denomination failed: {result4}"
    print(f"Single denomination: ✅")

    # Edge Case 5: All same coins
    coins5 = [1, 1, 1, 1, 1]
    result5 = solution.coinChange(coins5, 5)
    assert result5 == 5, f"All same coins failed: {result5}"
    print(f"All same coins: ✅")

    # Edge Case 6: Impossible case
    coins6 = [2, 4, 6]
    result6 = solution.coinChange(coins6, 1)
    assert result6 == -1, f"Impossible case failed: {result6}"
    print(f"Impossible case: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Coin Change:")

    # Large dataset
    coins = [1, 2, 5, 10, 20, 50]
    amount = 1000

    start_time = time.time()
    result = solution.coinChange(coins, amount)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (amount=1000, {len(coins)} coins):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Coin Change Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the coinChange method")
        print("- Aim for O(amount * coins.length) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(amount * coins.length)")
        print("- Consider using dynamic programming")
