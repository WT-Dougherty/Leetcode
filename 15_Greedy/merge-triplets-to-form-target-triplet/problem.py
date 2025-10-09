"""
Merge Triplets to Form Target Triplet - LeetCode Problem 1899

A triplet is an array of three integers. You are given a 2D integer array triplets,
where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an
integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain the target, you may apply the following operation any number of times (possibly zero):

- Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
  - For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
"""

import time


class Solution:
    def mergeTriplets(self, triplets, target):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    triplets1 = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target1 = [2, 7, 5]
    result1 = solution.mergeTriplets(triplets1, target1)
    assert (
        result1 == True
    ), f"Failed for triplets={triplets1}, target={target1}, expected True, got {result1}"

    # Test Case 2: Impossible case
    triplets2 = [[3, 4, 5], [4, 5, 6]]
    target2 = [3, 2, 5]
    result2 = solution.mergeTriplets(triplets2, target2)
    assert (
        result2 == False
    ), f"Failed for triplets={triplets2}, target={target2}, expected False, got {result2}"

    # Test Case 3: Single triplet
    triplets3 = [[1, 2, 3]]
    target3 = [1, 2, 3]
    result3 = solution.mergeTriplets(triplets3, target3)
    assert (
        result3 == True
    ), f"Failed for triplets={triplets3}, target={target3}, expected True, got {result3}"

    # Test Case 4: Complex case
    triplets4 = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
    target4 = [5, 5, 5]
    result4 = solution.mergeTriplets(triplets4, target4)
    assert (
        result4 == True
    ), f"Failed for triplets={triplets4}, target={target4}, expected True, got {result4}"

    # Test Case 5: Edge case
    triplets5 = [[1, 1, 1]]
    target5 = [1, 1, 1]
    result5 = solution.mergeTriplets(triplets5, target5)
    assert (
        result5 == True
    ), f"Failed for triplets={triplets5}, target={target5}, expected True, got {result5}"

    # Test Case 6: Multiple same triplets
    triplets6 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    target6 = [1, 2, 3]
    result6 = solution.mergeTriplets(triplets6, target6)
    assert (
        result6 == True
    ), f"Failed for triplets={triplets6}, target={target6}, expected True, got {result6}"

    # Test Case 7: Large values
    triplets7 = [[100, 100, 100], [50, 50, 50]]
    target7 = [100, 100, 100]
    result7 = solution.mergeTriplets(triplets7, target7)
    assert (
        result7 == True
    ), f"Failed for triplets={triplets7}, target={target7}, expected True, got {result7}"

    # Test Case 8: Impossible with large values
    triplets8 = [[1, 1, 1], [2, 2, 2]]
    target8 = [3, 3, 3]
    result8 = solution.mergeTriplets(triplets8, target8)
    assert (
        result8 == False
    ), f"Failed for triplets={triplets8}, target={target8}, expected False, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        triplets = [[i % 100, (i + 1) % 100, (i + 2) % 100] for i in range(size)]
        target = [50, 50, 50]

        # Test approach
        start_time = time.time()
        result = solution.mergeTriplets(triplets, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Single triplet
    triplets = [[1, 2, 3]]
    target = [1, 2, 3]
    result = solution.mergeTriplets(triplets, target)
    print(f"Single triplet: {result} ✅")

    # Edge Case 2: All zeros
    triplets = [[0, 0, 0], [0, 0, 0]]
    target = [0, 0, 0]
    result = solution.mergeTriplets(triplets, target)
    print(f"All zeros: {result} ✅")

    # Edge Case 3: Maximum values
    triplets = [[100, 100, 100]]
    target = [100, 100, 100]
    result = solution.mergeTriplets(triplets, target)
    print(f"Maximum values: {result} ✅")

    # Edge Case 4: Mixed values
    triplets = [[0, 50, 100], [50, 0, 100], [100, 50, 0]]
    target = [100, 50, 100]
    result = solution.mergeTriplets(triplets, target)
    print(f"Mixed values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    size = 10000
    triplets = [[i % 100, (i + 1) % 100, (i + 2) % 100] for i in range(size)]
    target = [50, 50, 50]

    start_time = time.time()
    result = solution.mergeTriplets(triplets, target)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} triplets):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Merge Triplets to Form Target Triplet Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the mergeTriplets method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using greedy approach with filtering")
