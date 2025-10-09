"""
Reconstruct Itinerary - LeetCode Problem 332

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the
departure and the arrival airports of one flight.
"""

import time
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    result1 = solution.findItinerary(tickets1)
    expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert (
        result1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {result1}"

    # Test Case 2: Multiple paths
    tickets2 = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    result2 = solution.findItinerary(tickets2)
    expected2 = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert (
        result2 == expected2
    ), f"Failed for multiple paths, expected {expected2}, got {result2}"

    # Test Case 3: Single ticket
    tickets3 = [["JFK", "SFO"]]
    result3 = solution.findItinerary(tickets3)
    expected3 = ["JFK", "SFO"]
    assert (
        result3 == expected3
    ), f"Failed for single ticket, expected {expected3}, got {result3}"

    # Test Case 4: Two tickets
    tickets4 = [["JFK", "ATL"], ["ATL", "SFO"]]
    result4 = solution.findItinerary(tickets4)
    expected4 = ["JFK", "ATL", "SFO"]
    assert (
        result4 == expected4
    ), f"Failed for two tickets, expected {expected4}, got {result4}"

    # Test Case 5: Complex case
    tickets5 = [
        ["JFK", "KUL"],
        ["JFK", "NRT"],
        ["NRT", "JFK"],
    ]
    result5 = solution.findItinerary(tickets5)
    expected5 = ["JFK", "NRT", "JFK", "KUL"]
    assert (
        result5 == expected5
    ), f"Failed for complex case, expected {expected5}, got {result5}"

    # Test Case 6: Multiple destinations from JFK
    tickets6 = [
        ["JFK", "ATL"],
        ["JFK", "SFO"],
        ["ATL", "SFO"],
        ["SFO", "ATL"],
    ]
    result6 = solution.findItinerary(tickets6)
    expected6 = ["JFK", "ATL", "SFO", "ATL", "SFO"]
    assert (
        result6 == expected6
    ), f"Failed for multiple destinations, expected {expected6}, got {result6}"

    # Test Case 7: Single destination
    tickets7 = [["JFK", "LAX"]]
    result7 = solution.findItinerary(tickets7)
    expected7 = ["JFK", "LAX"]
    assert (
        result7 == expected7
    ), f"Failed for single destination, expected {expected7}, got {result7}"

    # Test Case 8: Empty tickets
    tickets8 = []
    result8 = solution.findItinerary(tickets8)
    expected8 = ["JFK"]
    assert (
        result8 == expected8
    ), f"Failed for empty tickets, expected {expected8}, got {result8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [10, 50, 100]
    times = []

    print("\nTime Complexity Analysis:")
    print("Tickets\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create a valid itinerary
        tickets = []
        airports = ["JFK", "ATL", "SFO", "LAX", "ORD", "DFW", "DEN", "SEA"]
        for i in range(size):
            from_airport = airports[i % len(airports)]
            to_airport = airports[(i + 1) % len(airports)]
            tickets.append([from_airport, to_airport])

        # Test approach
        start_time = time.time()
        result = solution.findItinerary(tickets)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} airports")

    # Verify O(E * log E) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(E * log E) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            prev_complexity = test_sizes[i - 1] * (test_sizes[i - 1].bit_length())
            curr_complexity = test_sizes[i] * (test_sizes[i].bit_length())
            expected_ratio = curr_complexity / prev_complexity
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(E*log E): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 2.0  # Allow 200% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(E * log E)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(E * log E) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(E * log E), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(E * log E)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 ticket)
    tickets1 = [["JFK", "SFO"]]
    result1 = solution.findItinerary(tickets1)
    assert result1 == ["JFK", "SFO"], f"Single ticket failed: {result1}"
    print(f"Single ticket: ✅")

    # Edge Case 2: Maximum constraint (300 tickets)
    tickets2 = []
    airports = ["JFK", "ATL", "SFO", "LAX", "ORD", "DFW", "DEN", "SEA"]
    for i in range(300):
        from_airport = airports[i % len(airports)]
        to_airport = airports[(i + 1) % len(airports)]
        tickets2.append([from_airport, to_airport])

    result2 = solution.findItinerary(tickets2)
    assert isinstance(result2, list), f"Max constraint failed: {type(result2)}"
    print(f"Maximum constraint: ✅")

    # Edge Case 3: All same tickets
    tickets3 = [["JFK", "SFO"]] * 10
    result3 = solution.findItinerary(tickets3)
    assert len(result3) == 11, f"All same tickets failed: {len(result3)}"
    print(f"All same tickets: ✅")

    # Edge Case 4: Single airport
    tickets4 = [["JFK", "JFK"]]
    result4 = solution.findItinerary(tickets4)
    assert result4 == ["JFK", "JFK"], f"Single airport failed: {result4}"
    print(f"Single airport: ✅")

    # Edge Case 5: Maximum airport codes
    tickets5 = [["AAA", "BBB"], ["BBB", "CCC"], ["CCC", "DDD"]]
    result5 = solution.findItinerary(tickets5)
    assert len(result5) == 4, f"Max airport codes failed: {len(result5)}"
    print(f"Maximum airport codes: ✅")

    # Edge Case 6: Empty tickets
    tickets6 = []
    result6 = solution.findItinerary(tickets6)
    assert result6 == ["JFK"], f"Empty tickets failed: {result6}"
    print(f"Empty tickets: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Reconstruct Itinerary:")

    # Large dataset
    tickets = []
    airports = ["JFK", "ATL", "SFO", "LAX", "ORD", "DFW", "DEN", "SEA"]
    for i in range(100):
        from_airport = airports[i % len(airports)]
        to_airport = airports[(i + 1) % len(airports)]
        tickets.append([from_airport, to_airport])

    start_time = time.time()
    result = solution.findItinerary(tickets)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (100 tickets):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} airports")


if __name__ == "__main__":
    print("🧪 Testing Reconstruct Itinerary Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the findItinerary method")
        print("- Aim for O(E * log E) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(E * log E)")
        print("- Consider using DFS with backtracking")
