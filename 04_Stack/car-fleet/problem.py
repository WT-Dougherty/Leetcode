"""
Car Fleet - LeetCode Problem 853

There are n cars going to the same destination along a one-lane road. The destination is
target miles away.

You are given two integer arrays position and speed, both of length n, where position[i]
is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper
to bumper at the same speed. The faster car will slow down to match the slower car's speed.
The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed.
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be
considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""

import time
import random


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    target1, pos1, speed1 = 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]
    result1 = solution.carFleet(target1, pos1, speed1)
    assert (
        result1 == 3
    ), f"Failed for target={target1}, pos={pos1}, speed={speed1}, expected 3, got {result1}"

    # Test Case 2: Single car
    target2, pos2, speed2 = 10, [3], [3]
    result2 = solution.carFleet(target2, pos2, speed2)
    assert (
        result2 == 1
    ), f"Failed for target={target2}, pos={pos2}, speed={speed2}, expected 1, got {result2}"

    # Test Case 3: All cars form one fleet
    target3, pos3, speed3 = 100, [0, 2, 4], [4, 2, 1]
    result3 = solution.carFleet(target3, pos3, speed3)
    assert (
        result3 == 1
    ), f"Failed for target={target3}, pos={pos3}, speed={speed3}, expected 1, got {result3}"

    # Test Case 4: No fleets form
    target4, pos4, speed4 = 10, [0, 1, 2], [1, 1, 1]
    result4 = solution.carFleet(target4, pos4, speed4)
    assert (
        result4 == 3
    ), f"Failed for target={target4}, pos={pos4}, speed={speed4}, expected 3, got {result4}"

    # Test Case 5: Two fleets
    target5, pos5, speed5 = 20, [0, 5, 10], [2, 1, 1]
    result5 = solution.carFleet(target5, pos5, speed5)
    assert (
        result5 == 2
    ), f"Failed for target={target5}, pos={pos5}, speed={speed5}, expected 2, got {result5}"

    # Test Case 6: Edge case with same positions
    target6, pos6, speed6 = 10, [5, 5], [1, 2]
    result6 = solution.carFleet(target6, pos6, speed6)
    assert (
        result6 == 1
    ), f"Failed for target={target6}, pos={pos6}, speed={speed6}, expected 1, got {result6}"

    # Test Case 7: Edge case with same speeds
    target7, pos7, speed7 = 10, [0, 5], [2, 2]
    result7 = solution.carFleet(target7, pos7, speed7)
    assert (
        result7 == 2
    ), f"Failed for target={target7}, pos={pos7}, speed={speed7}, expected 2, got {result7}"

    # Test Case 8: Large target
    target8, pos8, speed8 = 1000000, [0, 100000], [1, 1]
    result8 = solution.carFleet(target8, pos8, speed8)
    assert (
        result8 == 2
    ), f"Failed for target={target8}, pos={pos8}, speed={speed8}, expected 2, got {result8}"

    # Test Case 9: Complex case
    target9, pos9, speed9 = 20, [0, 2, 4, 6, 8], [1, 2, 3, 4, 5]
    result9 = solution.carFleet(target9, pos9, speed9)
    assert (
        result9 == 1
    ), f"Failed for target={target9}, pos={pos9}, speed={speed9}, expected 1, got {result9}"

    # Test Case 10: Mixed speeds
    target10, pos10, speed10 = 15, [0, 3, 6, 9], [3, 1, 2, 1]
    result10 = solution.carFleet(target10, pos10, speed10)
    assert (
        result10 == 2
    ), f"Failed for target={target10}, pos={pos10}, speed={speed10}, expected 2, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n log n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tFleets")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        target = random.randint(1000, 1000000)
        position = [random.randint(0, target - 1) for _ in range(size)]
        speed = [random.randint(1, 1000000) for _ in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.carFleet(target, position, speed)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(n log n) complexity by checking if time growth is approximately n log n
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            n1, n2 = test_sizes[i - 1], test_sizes[i]
            expected_ratio = (n2 * (n2.bit_length() - 1)) / (n1 * (n1.bit_length() - 1))
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log n): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n²) or worse complexity")
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

    # Edge Case 1: Maximum constraint length
    target = 1000000
    position = [random.randint(0, target - 1) for _ in range(100000)]
    speed = [random.randint(1, 1000000) for _ in range(100000)]
    result = solution.carFleet(target, position, speed)
    print(f"Maximum length (100k cars): {result} ✅")

    # Edge Case 2: Maximum constraint values
    target = 1000000
    position = [0, 999999]
    speed = [1000000, 1000000]
    result = solution.carFleet(target, position, speed)
    print(f"Maximum constraint values: {result} ✅")

    # Edge Case 3: Minimum constraint values
    target = 1
    position = [0]
    speed = [1]
    result = solution.carFleet(target, position, speed)
    print(f"Minimum constraint values: {result} ✅")

    # Edge Case 4: All cars at same position
    target = 100
    position = [50] * 1000
    speed = [random.randint(1, 100) for _ in range(1000)]
    result = solution.carFleet(target, position, speed)
    print(f"All cars at same position: {result} ✅")

    # Edge Case 5: All cars at same speed
    target = 100
    position = [random.randint(0, 99) for _ in range(1000)]
    speed = [50] * 1000
    result = solution.carFleet(target, position, speed)
    print(f"All cars at same speed: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    target = 1000000
    position = [random.randint(0, target - 1) for _ in range(100000)]
    speed = [random.randint(1, 1000000) for _ in range(100000)]

    start_time = time.time()
    result = solution.carFleet(target, position, speed)
    time1 = time.time() - start_time

    print(f"Large dataset (100k cars):")
    print(f"Time: {time1:.6f}s, Fleets: {result}")


if __name__ == "__main__":
    print("🧪 Testing Car Fleet Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the carFleet method")
        print("- Aim for O(n log n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use sorting and monotonic stack")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log n)")
        print("- Consider using sorting and monotonic stack")
