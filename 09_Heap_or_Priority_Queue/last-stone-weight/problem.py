"""
Last Stone Weight - LeetCode Problem 1046

You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones
and smash them together.
"""

import time
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    stones1 = [2, 7, 4, 1, 8, 1]
    result1 = solution.lastStoneWeight(stones1)
    assert result1 == 1, f"Failed for [2,7,4,1,8,1], expected 1, got {result1}"

    # Test Case 2: Single stone
    stones2 = [1]
    result2 = solution.lastStoneWeight(stones2)
    assert result2 == 1, f"Failed for [1], expected 1, got {result2}"

    # Test Case 3: Two stones, same weight
    stones3 = [1, 1]
    result3 = solution.lastStoneWeight(stones3)
    assert result3 == 0, f"Failed for [1,1], expected 0, got {result3}"

    # Test Case 4: Two stones, different weights
    stones4 = [1, 2]
    result4 = solution.lastStoneWeight(stones4)
    assert result4 == 1, f"Failed for [1,2], expected 1, got {result4}"

    # Test Case 5: All same weights
    stones5 = [5, 5, 5, 5]
    result5 = solution.lastStoneWeight(stones5)
    assert result5 == 0, f"Failed for [5,5,5,5], expected 0, got {result5}"

    # Test Case 6: Three stones
    stones6 = [3, 7, 2]
    result6 = solution.lastStoneWeight(stones6)
    assert result6 == 2, f"Failed for [3,7,2], expected 2, got {result6}"

    # Test Case 7: Large weights
    stones7 = [1000, 500, 300]
    result7 = solution.lastStoneWeight(stones7)
    assert result7 == 200, f"Failed for [1000,500,300], expected 200, got {result7}"

    # Test Case 8: All destroyed
    stones8 = [2, 2]
    result8 = solution.lastStoneWeight(stones8)
    assert result8 == 0, f"Failed for [2,2], expected 0, got {result8}"

    # Test Case 9: Sequential weights
    stones9 = [1, 2, 3, 4, 5]
    result9 = solution.lastStoneWeight(stones9)
    assert result9 == 1, f"Failed for [1,2,3,4,5], expected 1, got {result9}"

    # Test Case 10: Reverse sorted
    stones10 = [5, 4, 3, 2, 1]
    result10 = solution.lastStoneWeight(stones10)
    assert result10 == 1, f"Failed for [5,4,3,2,1], expected 1, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        stones = list(range(1, size + 1))

        # Test approach
        start_time = time.time()
        result = solution.lastStoneWeight(stones)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n log n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i] * test_sizes[i]) / (
                test_sizes[i - 1] * test_sizes[i - 1]
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance for log n factor
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n log n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 stone)
    stones1 = [1]
    result1 = solution.lastStoneWeight(stones1)
    assert result1 == 1, f"Single stone failed: {result1}"
    print(f"Single stone: ✅")

    # Edge Case 2: Maximum constraint values
    stones2 = [1000, 1000]
    result2 = solution.lastStoneWeight(stones2)
    assert result2 == 0, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All same weights
    stones3 = [5] * 30
    result3 = solution.lastStoneWeight(stones3)
    assert result3 == 0, f"All same weights failed: {result3}"
    print(f"All same weights: ✅")

    # Edge Case 4: Maximum constraint length
    stones4 = list(range(1, 31))
    result4 = solution.lastStoneWeight(stones4)
    assert result4 == 1, f"Max constraint length failed: {result4}"
    print(f"Maximum constraint length: ✅")

    # Edge Case 5: Alternating weights
    stones5 = [1, 2] * 15
    result5 = solution.lastStoneWeight(stones5)
    assert result5 == 0, f"Alternating weights failed: {result5}"
    print(f"Alternating weights: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Last Stone Weight:")

    # Large dataset
    stones = list(range(1, 31))  # Max constraint

    start_time = time.time()
    result = solution.lastStoneWeight(stones)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (30 stones):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Last Stone Weight Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the lastStoneWeight method")
        print("- Aim for O(n log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log n)")
        print("- Consider using a max heap")
