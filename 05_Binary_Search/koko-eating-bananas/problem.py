"""
Koko Eating Bananas - LeetCode Problem 875

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of
bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats
all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards
come back.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import time
import random
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def AcceptableSpeed(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            return hours <= h

        large_pile = max(piles)
        l, r = 1, large_pile
        while l < r:
            mid = (l + r) // 2
            if AcceptableSpeed(mid):
                r = mid
            else:
                l = mid + 1
        return r


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    piles1, h1 = [3, 6, 7, 11], 8
    result1 = solution.minEatingSpeed(piles1, h1)
    assert result1 == 4, f"Failed for piles={piles1}, h={h1}, expected 4, got {result1}"

    # Test Case 2: Minimum speed needed
    piles2, h2 = [30, 11, 23, 4, 20], 5
    result2 = solution.minEatingSpeed(piles2, h2)
    assert (
        result2 == 30
    ), f"Failed for piles={piles2}, h={h2}, expected 30, got {result2}"

    # Test Case 3: More time available
    piles3, h3 = [30, 11, 23, 4, 20], 6
    result3 = solution.minEatingSpeed(piles3, h3)
    assert (
        result3 == 23
    ), f"Failed for piles={piles3}, h={h3}, expected 23, got {result3}"

    # Test Case 4: Single pile
    piles4, h4 = [5], 1
    result4 = solution.minEatingSpeed(piles4, h4)
    assert result4 == 5, f"Failed for piles={piles4}, h={h4}, expected 5, got {result4}"

    # Test Case 5: Single pile with more time
    piles5, h5 = [5], 3
    result5 = solution.minEatingSpeed(piles5, h5)
    assert result5 == 2, f"Failed for piles={piles5}, h={h5}, expected 2, got {result5}"

    # Test Case 6: All piles same size
    piles6, h6 = [10, 10, 10], 3
    result6 = solution.minEatingSpeed(piles6, h6)
    assert (
        result6 == 10
    ), f"Failed for piles={piles6}, h={h6}, expected 10, got {result6}"

    # Test Case 7: All piles same size with more time
    piles7, h7 = [10, 10, 10], 6
    result7 = solution.minEatingSpeed(piles7, h7)
    assert result7 == 5, f"Failed for piles={piles7}, h={h7}, expected 5, got {result7}"

    # Test Case 8: Large numbers
    piles8, h8 = [1000000000], 1
    result8 = solution.minEatingSpeed(piles8, h8)
    assert (
        result8 == 1000000000
    ), f"Failed for piles={piles8}, h={h8}, expected 1000000000, got {result8}"

    # Test Case 9: Edge case with minimum constraint
    piles9, h9 = [1], 1
    result9 = solution.minEatingSpeed(piles9, h9)
    assert result9 == 1, f"Failed for piles={piles9}, h={h9}, expected 1, got {result9}"

    # Test Case 10: Complex case
    piles10, h10 = [1, 2, 3, 4, 5], 5
    result10 = solution.minEatingSpeed(piles10, h10)
    assert (
        result10 == 5
    ), f"Failed for piles={piles10}, h={h10}, expected 3, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n * log(max(piles)))"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 5000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tMax Pile\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data
        max_pile = random.randint(1000, 10000)
        piles = [random.randint(1, max_pile) for _ in range(size)]
        h = random.randint(size, size * 2)

        # Test approach
        start_time = time.time()
        result = solution.minEatingSpeed(piles, h)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{max_pile}\t\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n * log(max(piles))) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n * log(max(piles))) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            n1, n2 = test_sizes[i - 1], test_sizes[i]
            max1, max2 = 10000, 10000  # Approximate max values
            expected_ratio = (n2 * (max2.bit_length() - 1)) / (
                n1 * (max1.bit_length() - 1)
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n * log(max(piles))): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(
                    f"\n❌ FAILED: Time complexity appears worse than O(n * log(max(piles)))"
                )
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n * max(piles)) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n * log(max(piles))), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * log(max(piles)))")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    piles = [random.randint(1, 1000) for _ in range(10000)]
    h = random.randint(10000, 20000)
    result = solution.minEatingSpeed(piles, h)
    print(f"Maximum length (10k piles): {result} ✅")

    # Edge Case 2: Maximum constraint values
    piles = [10**9]
    h = 1
    result = solution.minEatingSpeed(piles, h)
    assert result == 10**9
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    piles = [1]
    h = 1
    result = solution.minEatingSpeed(piles, h)
    assert result == 1
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All piles same size
    piles = [100] * 1000
    h = 1000
    result = solution.minEatingSpeed(piles, h)
    assert result == 100
    print(f"All piles same size: {result} ✅")

    # Edge Case 5: Very large piles
    piles = [10**8, 10**8, 10**8]
    h = 3
    result = solution.minEatingSpeed(piles, h)
    assert result == 10**8
    print(f"Very large piles: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    piles = [random.randint(1, 10000) for _ in range(5000)]
    h = random.randint(5000, 10000)

    start_time = time.time()
    result = solution.minEatingSpeed(piles, h)
    time1 = time.time() - start_time

    print(f"Large dataset (5k piles):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Koko Eating Bananas Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the minEatingSpeed method")
        print("- Aim for O(n * log(max(piles))) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use binary search on the answer")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log(max(piles)))")
        print("- Consider using binary search on the answer")
