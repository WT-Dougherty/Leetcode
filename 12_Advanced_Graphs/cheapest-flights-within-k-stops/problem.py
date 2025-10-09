"""
Cheapest Flights Within K Stops - LeetCode Problem 787

There are n cities connected by some number of flights. You are given an array flights
where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city
fromi to city toi with cost pricei.
"""

import time
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    n1 = 4
    flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src1, dst1, k1 = 0, 3, 1
    result1 = solution.findCheapestPrice(n1, flights1, src1, dst1, k1)
    assert result1 == 700, f"Failed for basic case, expected 700, got {result1}"

    # Test Case 2: Direct flight
    n2 = 3
    flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2, dst2, k2 = 0, 2, 1
    result2 = solution.findCheapestPrice(n2, flights2, src2, dst2, k2)
    assert result2 == 200, f"Failed for direct flight, expected 200, got {result2}"

    # Test Case 3: No stops
    n3 = 3
    flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src3, dst3, k3 = 0, 2, 0
    result3 = solution.findCheapestPrice(n3, flights3, src3, dst3, k3)
    assert result3 == 500, f"Failed for no stops, expected 500, got {result3}"

    # Test Case 4: No path
    n4 = 3
    flights4 = [[0, 1, 100]]
    src4, dst4, k4 = 0, 2, 1
    result4 = solution.findCheapestPrice(n4, flights4, src4, dst4, k4)
    assert result4 == -1, f"Failed for no path, expected -1, got {result4}"

    # Test Case 5: Same source and destination
    n5 = 2
    flights5 = [[0, 1, 100]]
    src5, dst5, k5 = 0, 0, 0
    result5 = solution.findCheapestPrice(n5, flights5, src5, dst5, k5)
    assert result5 == 0, f"Failed for same src/dst, expected 0, got {result5}"

    # Test Case 6: Multiple paths
    n6 = 4
    flights6 = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 3, 100],
        [0, 2, 300],
        [1, 3, 400],
    ]
    src6, dst6, k6 = 0, 3, 2
    result6 = solution.findCheapestPrice(n6, flights6, src6, dst6, k6)
    assert result6 == 300, f"Failed for multiple paths, expected 300, got {result6}"

    # Test Case 7: Complex case
    n7 = 5
    flights7 = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 3, 100],
        [3, 4, 100],
        [0, 2, 500],
        [1, 3, 600],
        [2, 4, 700],
    ]
    src7, dst7, k7 = 0, 4, 2
    result7 = solution.findCheapestPrice(n7, flights7, src7, dst7, k7)
    assert result7 == 400, f"Failed for complex case, expected 400, got {result7}"

    # Test Case 8: Single flight
    n8 = 2
    flights8 = [[0, 1, 100]]
    src8, dst8, k8 = 0, 1, 0
    result8 = solution.findCheapestPrice(n8, flights8, src8, dst8, k8)
    assert result8 == 100, f"Failed for single flight, expected 100, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Cities\tFlights\tTime\t\tResult")
    print("-" * 50)

    for size in test_sizes:
        # Generate test data - create a connected graph
        flights = []
        for i in range(size - 1):
            flights.append([i, i + 1, 100])
        # Add some additional flights
        for i in range(min(size // 2, 20)):
            flights.append([i, (i + 2) % size, 200])

        src, dst, k = 0, size - 1, size // 2

        # Test approach
        start_time = time.time()
        result = solution.findCheapestPrice(size, flights, src, dst, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{len(flights)}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(E + V * K) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(E + V * K) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] + test_sizes[i - 1] * (test_sizes[i - 1] // 2)
            curr_complexity = test_sizes[i] + test_sizes[i] * (test_sizes[i] // 2)
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(E+V*K): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(E + V * K)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(E + V * K) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(E + V * K), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(E + V * K)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 city)
    result1 = solution.findCheapestPrice(1, [], 0, 0, 0)
    assert result1 == 0, f"Single city failed: {result1}"
    print(f"Single city: ✅")

    # Edge Case 2: Maximum constraint (100 cities)
    flights2 = []
    for i in range(99):
        flights2.append([i, i + 1, 100])

    result2 = solution.findCheapestPrice(100, flights2, 0, 99, 50)
    assert isinstance(result2, int), f"Max constraint failed: {result2}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: Maximum flights (4950 flights for 100 cities)
    flights3 = []
    for i in range(100):
        for j in range(i + 1, 100):
            flights3.append([i, j, 100])

    result3 = solution.findCheapestPrice(100, flights3, 0, 99, 10)
    assert isinstance(result3, int), f"Max flights failed: {result3}"
    print(f"Maximum flights: ✅")

    # Edge Case 4: Maximum price (10^4)
    flights4 = [[0, 1, 10000]]
    result4 = solution.findCheapestPrice(2, flights4, 0, 1, 0)
    assert result4 == 10000, f"Max price failed: {result4}"
    print(f"Maximum price: ✅")

    # Edge Case 5: Maximum stops
    flights5 = []
    for i in range(99):
        flights5.append([i, i + 1, 100])

    result5 = solution.findCheapestPrice(100, flights5, 0, 99, 99)
    assert isinstance(result5, int), f"Max stops failed: {result5}"
    print(f"Maximum stops: ✅")

    # Edge Case 6: No flights
    result6 = solution.findCheapestPrice(3, [], 0, 2, 1)
    assert result6 == -1, f"No flights failed: {result6}"
    print(f"No flights: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Cheapest Flights:")

    # Large dataset
    n = 50
    flights = []
    for i in range(n - 1):
        flights.append([i, i + 1, 100])
    for i in range(min(n // 2, 20)):
        flights.append([i, (i + 2) % n, 200])

    src, dst, k = 0, n - 1, n // 2

    start_time = time.time()
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (50 cities, {len(flights)} flights):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Cheapest Flights Within K Stops Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findCheapestPrice method")
        print("- Aim for O(E + V * K) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(E + V * K)")
        print("- Consider using modified Dijkstra's algorithm")
