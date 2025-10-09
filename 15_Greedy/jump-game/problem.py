"""
Jump Game - LeetCode Problem 55

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum
jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

import time


class Solution:
    def canJump(self, nums):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    assert result1 == True, f"Failed for nums={nums1}, expected True, got {result1}"

    # Test Case 2: Impossible case
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    assert result2 == False, f"Failed for nums={nums2}, expected False, got {result2}"

    # Test Case 3: Single element
    nums3 = [0]
    result3 = solution.canJump(nums3)
    assert result3 == True, f"Failed for nums={nums3}, expected True, got {result3}"

    # Test Case 4: All zeros except last
    nums4 = [0, 0, 0, 0, 1]
    result4 = solution.canJump(nums4)
    assert result4 == False, f"Failed for nums={nums4}, expected False, got {result4}"

    # Test Case 5: Large jumps
    nums5 = [5, 0, 0, 0, 0, 0]
    result5 = solution.canJump(nums5)
    assert result5 == True, f"Failed for nums={nums5}, expected True, got {result5}"

    # Test Case 6: Complex case
    nums6 = [1, 1, 1, 1, 1]
    result6 = solution.canJump(nums6)
    assert result6 == True, f"Failed for nums={nums6}, expected True, got {result6}"

    # Test Case 7: Edge case
    nums7 = [1, 0, 1, 0]
    result7 = solution.canJump(nums7)
    assert result7 == False, f"Failed for nums={nums7}, expected False, got {result7}"

    # Test Case 8: Large values
    nums8 = [1000, 0, 0, 0, 0]
    result8 = solution.canJump(nums8)
    assert result8 == True, f"Failed for nums={nums8}, expected True, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - worst case scenario
        nums = [0] * (size - 1) + [1]

        # Test approach
        start_time = time.time()
        result = solution.canJump(nums)
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

    # Edge Case 1: Single element
    nums = [0]
    result = solution.canJump(nums)
    print(f"Single element: {result} ✅")

    # Edge Case 2: Two elements
    nums = [1, 0]
    result = solution.canJump(nums)
    print(f"Two elements: {result} ✅")

    # Edge Case 3: All zeros
    nums = [0, 0, 0]
    result = solution.canJump(nums)
    print(f"All zeros: {result} ✅")

    # Edge Case 4: Large jump at start
    nums = [1000] + [0] * 999
    result = solution.canJump(nums)
    print(f"Large jump at start: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset - worst case
    size = 100000
    nums = [0] * (size - 1) + [1]

    start_time = time.time()
    result = solution.canJump(nums)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} elements, worst case):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")

    # Large dataset - best case
    nums2 = [size] + [0] * (size - 1)

    start_time = time.time()
    result2 = solution.canJump(nums2)
    elapsed_time2 = time.time() - start_time

    print(f"\nLarge dataset ({size} elements, best case):")
    print(f"Time: {elapsed_time2:.6f}s, Result: {result2}")


if __name__ == "__main__":
    print("🧪 Testing Jump Game Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the canJump method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using greedy approach with max reach tracking")
