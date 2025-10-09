"""
Gas Station - LeetCode Problem 134

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel
around the circuit once in the clockwise direction, otherwise return -1. If there exists a
solution, it is guaranteed to be unique.
"""

import time


class Solution:
    def canCompleteCircuit(self, gas, cost):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    result1 = solution.canCompleteCircuit(gas1, cost1)
    assert (
        result1 == 3
    ), f"Failed for gas={gas1}, cost={cost1}, expected 3, got {result1}"

    # Test Case 2: Impossible case
    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    result2 = solution.canCompleteCircuit(gas2, cost2)
    assert (
        result2 == -1
    ), f"Failed for gas={gas2}, cost={cost2}, expected -1, got {result2}"

    # Test Case 3: Single station
    gas3 = [4]
    cost3 = [5]
    result3 = solution.canCompleteCircuit(gas3, cost3)
    assert (
        result3 == -1
    ), f"Failed for gas={gas3}, cost={cost3}, expected -1, got {result3}"

    # Test Case 4: Single station success
    gas4 = [5]
    cost4 = [4]
    result4 = solution.canCompleteCircuit(gas4, cost4)
    assert (
        result4 == 0
    ), f"Failed for gas={gas4}, cost={cost4}, expected 0, got {result4}"

    # Test Case 5: Two stations
    gas5 = [1, 2]
    cost5 = [2, 1]
    result5 = solution.canCompleteCircuit(gas5, cost5)
    assert (
        result5 == 1
    ), f"Failed for gas={gas5}, cost={cost5}, expected 1, got {result5}"

    # Test Case 6: All same values
    gas6 = [3, 3, 3]
    cost6 = [3, 3, 3]
    result6 = solution.canCompleteCircuit(gas6, cost6)
    assert (
        result6 == 0
    ), f"Failed for gas={gas6}, cost={cost6}, expected 0, got {result6}"

    # Test Case 7: Complex case
    gas7 = [5, 1, 2, 3, 4]
    cost7 = [4, 4, 1, 5, 1]
    result7 = solution.canCompleteCircuit(gas7, cost7)
    assert (
        result7 == 4
    ), f"Failed for gas={gas7}, cost={cost7}, expected 4, got {result7}"

    # Test Case 8: Edge case
    gas8 = [1, 2, 3, 4, 5]
    cost8 = [3, 4, 5, 1, 2]
    result8 = solution.canCompleteCircuit(gas8, cost8)
    assert (
        result8 == 3
    ), f"Failed for gas={gas8}, cost={cost8}, expected 3, got {result8}"

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
        # Generate test data
        gas = [i % 10 + 1 for i in range(size)]
        cost = [(i + 1) % 10 + 1 for i in range(size)]

        # Test approach
        start_time = time.time()
        result = solution.canCompleteCircuit(gas, cost)
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

    # Edge Case 1: Single station success
    gas = [10]
    cost = [5]
    result = solution.canCompleteCircuit(gas, cost)
    print(f"Single station success: {result} ✅")

    # Edge Case 2: Single station failure
    gas = [5]
    cost = [10]
    result = solution.canCompleteCircuit(gas, cost)
    print(f"Single station failure: {result} ✅")

    # Edge Case 3: All zeros
    gas = [0, 0, 0]
    cost = [0, 0, 0]
    result = solution.canCompleteCircuit(gas, cost)
    print(f"All zeros: {result} ✅")

    # Edge Case 4: Large values
    gas = [10000, 10000, 10000]
    cost = [10000, 10000, 10000]
    result = solution.canCompleteCircuit(gas, cost)
    print(f"Large values: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    size = 100000
    gas = [i % 10 + 1 for i in range(size)]
    cost = [(i + 1) % 10 + 1 for i in range(size)]

    start_time = time.time()
    result = solution.canCompleteCircuit(gas, cost)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} stations):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Gas Station Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the canCompleteCircuit method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using greedy approach with total gas tracking")
