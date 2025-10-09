"""
Hand of Straights - LeetCode Problem 846

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""

import time
from collections import Counter


class Solution:
    def isNStraightHand(self, hand, groupSize):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize1 = 3
    result1 = solution.isNStraightHand(hand1, groupSize1)
    assert (
        result1 == True
    ), f"Failed for hand={hand1}, groupSize={groupSize1}, expected True, got {result1}"

    # Test Case 2: Impossible case
    hand2 = [1, 2, 3, 4, 5]
    groupSize2 = 4
    result2 = solution.isNStraightHand(hand2, groupSize2)
    assert (
        result2 == False
    ), f"Failed for hand={hand2}, groupSize={groupSize2}, expected False, got {result2}"

    # Test Case 3: Single group
    hand3 = [1, 2, 3, 4, 5, 6]
    groupSize3 = 2
    result3 = solution.isNStraightHand(hand3, groupSize3)
    assert (
        result3 == True
    ), f"Failed for hand={hand3}, groupSize={groupSize3}, expected True, got {result3}"

    # Test Case 4: Duplicates
    hand4 = [1, 1, 2, 2, 3, 3]
    groupSize4 = 3
    result4 = solution.isNStraightHand(hand4, groupSize4)
    assert (
        result4 == True
    ), f"Failed for hand={hand4}, groupSize={groupSize4}, expected True, got {result4}"

    # Test Case 5: Not enough cards
    hand5 = [1, 2, 3, 4, 5]
    groupSize5 = 3
    result5 = solution.isNStraightHand(hand5, groupSize5)
    assert (
        result5 == False
    ), f"Failed for hand={hand5}, groupSize={groupSize5}, expected False, got {result5}"

    # Test Case 6: Complex case
    hand6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    groupSize6 = 3
    result6 = solution.isNStraightHand(hand6, groupSize6)
    assert (
        result6 == True
    ), f"Failed for hand={hand6}, groupSize={groupSize6}, expected True, got {result6}"

    # Test Case 7: Edge case
    hand7 = [1]
    groupSize7 = 1
    result7 = solution.isNStraightHand(hand7, groupSize7)
    assert (
        result7 == True
    ), f"Failed for hand={hand7}, groupSize={groupSize7}, expected True, got {result7}"

    # Test Case 8: Gap in sequence
    hand8 = [1, 2, 3, 5, 6, 7]
    groupSize8 = 3
    result8 = solution.isNStraightHand(hand8, groupSize8)
    assert (
        result8 == False
    ), f"Failed for hand={hand8}, groupSize={groupSize8}, expected False, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n * log n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - consecutive numbers
        hand = list(range(1, size + 1))
        groupSize = 2

        # Test approach
        start_time = time.time()
        result = solution.isNStraightHand(hand, groupSize)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(n * log n) complexity by checking if time growth is approximately n*log(n)
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n * log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * (test_sizes[i - 1].bit_length())
            curr_complexity = test_sizes[i] * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n * log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n * log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n * log n) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n * log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n * log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Single card
    hand = [1]
    groupSize = 1
    result = solution.isNStraightHand(hand, groupSize)
    print(f"Single card: {result} ✅")

    # Edge Case 2: Large group size
    hand = [1, 2, 3, 4, 5]
    groupSize = 5
    result = solution.isNStraightHand(hand, groupSize)
    print(f"Large group size: {result} ✅")

    # Edge Case 3: All same cards
    hand = [5, 5, 5, 5]
    groupSize = 2
    result = solution.isNStraightHand(hand, groupSize)
    print(f"All same cards: {result} ✅")

    # Edge Case 4: Large values
    hand = [1000000000, 1000000001, 1000000002]
    groupSize = 3
    result = solution.isNStraightHand(hand, groupSize)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    size = 10000
    hand = list(range(1, size + 1))
    groupSize = 5

    start_time = time.time()
    result = solution.isNStraightHand(hand, groupSize)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} cards, groupSize={groupSize}):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Hand of Straights Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isNStraightHand method")
        print("- Aim for O(n * log n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n * log n)")
        print("- Consider using sorted approach with frequency counting")
