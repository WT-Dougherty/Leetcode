"""
Task Scheduler - LeetCode Problem 621

Given a characters array tasks, representing the tasks CPU needs to do, where each letter
represents a different task. Tasks could be done in any order. Each task is done in one
unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between
two same tasks (the same letter in the array), that is that there must be at least n
units of time between any two same tasks.
"""

import time
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    tasks1 = ["A", "A", "A", "B", "B", "B"]
    n1 = 2
    result1 = solution.leastInterval(tasks1, n1)
    assert (
        result1 == 8
    ), f"Failed for ['A','A','A','B','B','B'], n=2, expected 8, got {result1}"

    # Test Case 2: No cooldown
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    n2 = 0
    result2 = solution.leastInterval(tasks2, n2)
    assert (
        result2 == 6
    ), f"Failed for ['A','A','A','B','B','B'], n=0, expected 6, got {result2}"

    # Test Case 3: Complex case
    tasks3 = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n3 = 2
    result3 = solution.leastInterval(tasks3, n3)
    assert result3 == 16, f"Failed for complex case, expected 16, got {result3}"

    # Test Case 4: Single task
    tasks4 = ["A"]
    n4 = 2
    result4 = solution.leastInterval(tasks4, n4)
    assert result4 == 1, f"Failed for ['A'], n=2, expected 1, got {result4}"

    # Test Case 5: Two different tasks
    tasks5 = ["A", "B"]
    n5 = 2
    result5 = solution.leastInterval(tasks5, n5)
    assert result5 == 2, f"Failed for ['A','B'], n=2, expected 2, got {result5}"

    # Test Case 6: All same tasks
    tasks6 = ["A", "A", "A", "A"]
    n6 = 2
    result6 = solution.leastInterval(tasks6, n6)
    assert (
        result6 == 10
    ), f"Failed for ['A','A','A','A'], n=2, expected 10, got {result6}"

    # Test Case 7: Many different tasks
    tasks7 = ["A", "B", "C", "D", "E", "F", "G", "H"]
    n7 = 2
    result7 = solution.leastInterval(tasks7, n7)
    assert result7 == 8, f"Failed for many different tasks, expected 8, got {result7}"

    # Test Case 8: Large cooldown
    tasks8 = ["A", "A", "A", "B", "B", "B"]
    n8 = 10
    result8 = solution.leastInterval(tasks8, n8)
    assert result8 == 22, f"Failed for large cooldown, expected 22, got {result8}"

    # Test Case 9: Mixed frequencies
    tasks9 = ["A", "A", "A", "B", "B", "C"]
    n9 = 2
    result9 = solution.leastInterval(tasks9, n9)
    assert result9 == 7, f"Failed for mixed frequencies, expected 7, got {result9}"

    # Test Case 10: Single task repeated
    tasks10 = ["A", "A", "A", "A", "A"]
    n10 = 1
    result10 = solution.leastInterval(tasks10, n10)
    assert result10 == 9, f"Failed for single task repeated, expected 9, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tN\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data
        tasks = ["A"] * (size // 2) + ["B"] * (size // 2)
        n = 2

        # Test approach
        start_time = time.time()
        result = solution.leastInterval(tasks, n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{n}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n) complexity
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

        # Check if ratios are within acceptable range
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n) complexity")
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

    # Edge Case 1: Minimum constraint (1 task)
    tasks1 = ["A"]
    result1 = solution.leastInterval(tasks1, 0)
    assert result1 == 1, f"Single task failed: {result1}"
    print(f"Single task: ✅")

    # Edge Case 2: Maximum constraint values
    tasks2 = ["A"] * 10000
    result2 = solution.leastInterval(tasks2, 100)
    assert result2 > 10000, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All same tasks
    tasks3 = ["A"] * 1000
    result3 = solution.leastInterval(tasks3, 2)
    assert result3 == 2998, f"All same tasks failed: {result3}"
    print(f"All same tasks: ✅")

    # Edge Case 4: Maximum cooldown
    tasks4 = ["A", "B"]
    result4 = solution.leastInterval(tasks4, 100)
    assert result4 == 2, f"Max cooldown failed: {result4}"
    print(f"Maximum cooldown: ✅")

    # Edge Case 5: All different tasks
    tasks5 = [chr(ord("A") + i) for i in range(26)]
    result5 = solution.leastInterval(tasks5, 2)
    assert result5 == 26, f"All different tasks failed: {result5}"
    print(f"All different tasks: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Task Scheduler:")

    # Large dataset
    tasks = ["A"] * 5000 + ["B"] * 5000
    n = 2

    start_time = time.time()
    result = solution.leastInterval(tasks, n)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (10,000 tasks, n=2):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Task Scheduler Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the leastInterval method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using frequency counting approach")
