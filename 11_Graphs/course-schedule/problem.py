"""
Course Schedule - LeetCode Problem 207

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.
"""

import time
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case - possible
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    result1 = solution.canFinish(numCourses1, prerequisites1)
    assert result1 == True, f"Failed for basic case, expected True, got {result1}"

    # Test Case 2: Basic case - impossible (cycle)
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = solution.canFinish(numCourses2, prerequisites2)
    assert result2 == False, f"Failed for cycle case, expected False, got {result2}"

    # Test Case 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    result3 = solution.canFinish(numCourses3, prerequisites3)
    assert result3 == True, f"Failed for no prerequisites, expected True, got {result3}"

    # Test Case 4: Complex case - possible
    numCourses4 = 4
    prerequisites4 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result4 = solution.canFinish(numCourses4, prerequisites4)
    assert result4 == True, f"Failed for complex case, expected True, got {result4}"

    # Test Case 5: Complex case - impossible
    numCourses5 = 4
    prerequisites5 = [[1, 0], [2, 1], [3, 2], [0, 3]]
    result5 = solution.canFinish(numCourses5, prerequisites5)
    assert result5 == False, f"Failed for complex cycle, expected False, got {result5}"

    # Test Case 6: Single course
    numCourses6 = 1
    prerequisites6 = []
    result6 = solution.canFinish(numCourses6, prerequisites6)
    assert result6 == True, f"Failed for single course, expected True, got {result6}"

    # Test Case 7: Multiple cycles
    numCourses7 = 3
    prerequisites7 = [[0, 1], [1, 2], [2, 0]]
    result7 = solution.canFinish(numCourses7, prerequisites7)
    assert (
        result7 == False
    ), f"Failed for multiple cycles, expected False, got {result7}"

    # Test Case 8: Disconnected components
    numCourses8 = 4
    prerequisites8 = [[1, 0], [3, 2]]
    result8 = solution.canFinish(numCourses8, prerequisites8)
    assert (
        result8 == True
    ), f"Failed for disconnected components, expected True, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Courses\tPrereqs\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create a valid DAG
        prerequisites = []
        for i in range(size - 1):
            prerequisites.append([i + 1, i])

        # Test approach
        start_time = time.time()
        result = solution.canFinish(size, prerequisites)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(prerequisites)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(V + E) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(V + E) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] + (test_sizes[i - 1] - 1)
            curr_complexity = test_sizes[i] + (test_sizes[i] - 1)
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(V+E): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(V + E)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(V + E) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(V + E), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(V + E)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 course)
    result1 = solution.canFinish(1, [])
    assert result1 == True, f"Single course failed: {result1}"
    print(f"Single course: ✅")

    # Edge Case 2: Maximum constraint (2000 courses)
    prerequisites2 = []
    for i in range(1999):
        prerequisites2.append([i + 1, i])

    result2 = solution.canFinish(2000, prerequisites2)
    assert result2 == True, f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum prerequisites (5000)
    prerequisites3 = []
    for i in range(5000):
        prerequisites3.append([i % 2000, (i + 1) % 2000])

    result3 = solution.canFinish(2000, prerequisites3)
    assert isinstance(result3, bool), f"Max prerequisites failed: {result3}"
    print(f"Maximum prerequisites: ✅")

    # Edge Case 4: Self-loop (should be impossible)
    result4 = solution.canFinish(2, [[0, 0]])
    assert result4 == False, f"Self-loop failed: {result4}"
    print(f"Self-loop: ✅")

    # Edge Case 5: Large cycle
    prerequisites5 = []
    for i in range(100):
        prerequisites5.append([i, (i + 1) % 100])

    result5 = solution.canFinish(100, prerequisites5)
    assert result5 == False, f"Large cycle failed: {result5}"
    print(f"Large cycle: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Course Schedule:")

    # Large dataset
    numCourses = 1000
    prerequisites = []
    for i in range(999):
        prerequisites.append([i + 1, i])

    start_time = time.time()
    result = solution.canFinish(numCourses, prerequisites)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (1000 courses, 999 prerequisites):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Course Schedule Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the canFinish method")
        print("- Aim for O(V + E) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(V + E)")
        print("- Consider using DFS or BFS with cycle detection")
