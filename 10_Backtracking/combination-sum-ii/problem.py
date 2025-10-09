"""
Combination Sum II - LeetCode Problem 40

Given a collection of candidate numbers (candidates) and a target number (target), find all
unique combinations in candidates where the candidate numbers sum to target.
"""

import time
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case with duplicates
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = solution.combinationSum2(candidates1, target1)
    expected1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert len(result1) == len(
        expected1
    ), f"Failed for basic case, expected {len(expected1)} combinations, got {len(result1)}"
    for combo in expected1:
        assert combo in result1, f"Missing combination {combo} in result {result1}"

    # Test Case 2: Multiple duplicates
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = solution.combinationSum2(candidates2, target2)
    expected2 = [[1, 2, 2], [5]]
    assert len(result2) == len(
        expected2
    ), f"Failed for multiple duplicates, expected {len(expected2)} combinations, got {len(result2)}"
    for combo in expected2:
        assert combo in result2, f"Missing combination {combo} in result {result2}"

    # Test Case 3: No solution
    candidates3 = [2, 3]
    target3 = 1
    result3 = solution.combinationSum2(candidates3, target3)
    assert result3 == [], f"Failed for no solution, expected [], got {result3}"

    # Test Case 4: Single element
    candidates4 = [1]
    target4 = 1
    result4 = solution.combinationSum2(candidates4, target4)
    assert result4 == [[1]], f"Failed for single element, expected [[1]], got {result4}"

    # Test Case 5: All same elements
    candidates5 = [1, 1, 1]
    target5 = 2
    result5 = solution.combinationSum2(candidates5, target5)
    assert result5 == [
        [1, 1]
    ], f"Failed for all same elements, expected [[1,1]], got {result5}"

    # Test Case 6: Large target
    candidates6 = [1, 2, 3, 4, 5]
    target6 = 10
    result6 = solution.combinationSum2(candidates6, target6)
    # Verify all combinations sum to target
    for combo in result6:
        assert sum(combo) == target6, f"Combination {combo} doesn't sum to {target6}"

    # Test Case 7: Duplicates at different positions
    candidates7 = [1, 1, 2, 2, 3]
    target7 = 4
    result7 = solution.combinationSum2(candidates7, target7)
    # Verify all combinations sum to target
    for combo in result7:
        assert sum(combo) == target7, f"Combination {combo} doesn't sum to {target7}"

    # Test Case 8: Edge case with zero
    candidates8 = [1, 2]
    target8 = 0
    result8 = solution.combinationSum2(candidates8, target8)
    assert result8 == [[]], f"Failed for target 0, expected [[]], got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [5, 10, 15]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTarget\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data with duplicates
        candidates = [
            i for i in range(1, size + 1) for _ in range(2)
        ]  # Each number appears twice
        target = size

        # Test approach
        start_time = time.time()
        result = solution.combinationSum2(candidates, target)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{target}\t{elapsed_time:.6f}s\t{len(result)} combinations")

    # Verify O(2^N) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(2^N) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = 2 ** (test_sizes[i] - test_sizes[i - 1])
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(2^N): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance for exponential complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(2^N)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(2^N) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(2^N), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(2^N)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 candidate, target 1)
    candidates1 = [1]
    result1 = solution.combinationSum2(candidates1, 1)
    assert result1 == [[1]], f"Min constraint failed: {result1}"
    print(f"Minimum constraint: ✅")

    # Edge Case 2: Maximum constraint values
    candidates2 = [50] * 100
    result2 = solution.combinationSum2(candidates2, 50)
    assert result2 == [[50]], f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All candidates same
    candidates3 = [2] * 20
    result3 = solution.combinationSum2(candidates3, 8)
    assert result3 == [[2, 2, 2, 2]], f"All candidates same failed: {result3}"
    print(f"All candidates same: ✅")

    # Edge Case 4: Large target
    candidates4 = [1, 2, 3, 4, 5]
    result4 = solution.combinationSum2(candidates4, 30)
    assert len(result4) > 0, f"Large target failed: {result4}"
    print(f"Large target: ✅")

    # Edge Case 5: Many duplicates
    candidates5 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    result5 = solution.combinationSum2(candidates5, 5)
    assert len(result5) > 0, f"Many duplicates failed: {result5}"
    print(f"Many duplicates: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Combination Sum II:")

    # Large dataset
    candidates = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target = 10

    start_time = time.time()
    result = solution.combinationSum2(candidates, target)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10 candidates with duplicates, target=10):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} combinations")


if __name__ == "__main__":
    print("🧪 Testing Combination Sum II Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the combinationSum2 method")
        print("- Aim for O(2^N) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(2^N)")
        print("- Consider using backtracking with duplicate handling")
