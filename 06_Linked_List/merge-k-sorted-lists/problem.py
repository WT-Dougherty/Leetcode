"""
Merge K Sorted Lists - LeetCode Problem 23

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""

import time
import random
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
    ]
    result1 = solution.mergeKLists(lists1)
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    actual1 = linked_list_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {actual1}"

    # Test Case 2: Empty lists
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    expected2 = []
    actual2 = linked_list_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for empty lists, expected {expected2}, got {actual2}"

    # Test Case 3: Single empty list
    lists3 = [create_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    expected3 = []
    actual3 = linked_list_to_list(result3)
    assert (
        actual3 == expected3
    ), f"Failed for single empty list, expected {expected3}, got {actual3}"

    # Test Case 4: Single list
    lists4 = [create_linked_list([1, 2, 3])]
    result4 = solution.mergeKLists(lists4)
    expected4 = [1, 2, 3]
    actual4 = linked_list_to_list(result4)
    assert (
        actual4 == expected4
    ), f"Failed for single list, expected {expected4}, got {actual4}"

    # Test Case 5: Two lists
    lists5 = [create_linked_list([1, 3, 5]), create_linked_list([2, 4, 6])]
    result5 = solution.mergeKLists(lists5)
    expected5 = [1, 2, 3, 4, 5, 6]
    actual5 = linked_list_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for two lists, expected {expected5}, got {actual5}"

    # Test Case 6: Negative numbers
    lists6 = [
        create_linked_list([-1, 0, 1]),
        create_linked_list([-2, 2]),
        create_linked_list([-3, -1, 3]),
    ]
    result6 = solution.mergeKLists(lists6)
    expected6 = [-3, -2, -1, -1, 0, 1, 2, 3]
    actual6 = linked_list_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for negative numbers, expected {expected6}, got {actual6}"

    # Test Case 7: Different lengths
    lists7 = [
        create_linked_list([1]),
        create_linked_list([2, 3, 4]),
        create_linked_list([5, 6]),
    ]
    result7 = solution.mergeKLists(lists7)
    expected7 = [1, 2, 3, 4, 5, 6]
    actual7 = linked_list_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for different lengths, expected {expected7}, got {actual7}"

    # Test Case 8: Maximum constraint
    lists8 = []
    for i in range(10000):
        lists8.append(create_linked_list([i]))
    result8 = solution.mergeKLists(lists8)
    expected8 = list(range(10000))
    actual8 = linked_list_to_list(result8)
    assert actual8 == expected8, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n log k)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(10, 100), (20, 200), (40, 400)]
    times = []

    print("\nTime Complexity Analysis:")
    print("K\tN\tTime\t\tResult")
    print("-" * 50)

    for k, n in test_sizes:
        # Generate test data
        lists = []
        for i in range(k):
            values = sorted([random.randint(-10000, 10000) for _ in range(n // k)])
            lists.append(create_linked_list(values))

        # Test approach
        start_time = time.time()
        result = solution.mergeKLists(lists)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is sorted
        actual = linked_list_to_list(result)
        expected = sorted([val for lst in lists for val in linked_list_to_list(lst)])
        assert actual == expected, f"Result verification failed for k={k}, n={n}"

        print(f"{k}\t{n}\t{elapsed_time:.6f}s\tMerged")

    # Verify O(n log k) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log k) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            k1, n1 = test_sizes[i - 1]
            k2, n2 = test_sizes[i]
            expected_ratio = (n2 * (k2.bit_length() - 1)) / (n1 * (k1.bit_length() - 1))
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log k): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (min_expected <= actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log k)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n * k) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n log k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n log k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint k
    lists = []
    for i in range(10000):
        lists.append(create_linked_list([i]))
    result = solution.mergeKLists(lists)
    actual = linked_list_to_list(result)
    expected = list(range(10000))
    assert actual == expected
    print(f"Maximum k (10k lists): ✅")

    # Edge Case 2: Maximum constraint n
    lists = []
    for i in range(100):
        values = list(range(i * 100, (i + 1) * 100))
        lists.append(create_linked_list(values))
    result = solution.mergeKLists(lists)
    actual = linked_list_to_list(result)
    expected = list(range(10000))
    assert actual == expected
    print(f"Maximum n (10k total nodes): ✅")

    # Edge Case 3: Maximum constraint values
    lists = []
    for i in range(100):
        lists.append(create_linked_list([10000] * 10))
    result = solution.mergeKLists(lists)
    actual = linked_list_to_list(result)
    expected = [10000] * 1000
    assert actual == expected
    print(f"Maximum constraint values: ✅")

    # Edge Case 4: Minimum constraint values
    lists = []
    for i in range(100):
        lists.append(create_linked_list([-10000] * 10))
    result = solution.mergeKLists(lists)
    actual = linked_list_to_list(result)
    expected = [-10000] * 1000
    assert actual == expected
    print(f"Minimum constraint values: ✅")

    # Edge Case 5: Mixed empty and non-empty lists
    lists = []
    for i in range(100):
        if i % 2 == 0:
            lists.append(create_linked_list([i]))
        else:
            lists.append(create_linked_list([]))
    result = solution.mergeKLists(lists)
    actual = linked_list_to_list(result)
    expected = list(range(0, 100, 2))
    assert actual == expected
    print(f"Mixed empty and non-empty lists: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    lists = []
    for i in range(1000):
        values = sorted([random.randint(-10000, 10000) for _ in range(10)])
        lists.append(create_linked_list(values))

    start_time = time.time()
    result = solution.mergeKLists(lists)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(result)
    assert len(actual) == 10000

    print(f"Large dataset (1k lists, 10k total nodes):")
    print(f"Time: {time1:.6f}s, Result: Merged correctly")


if __name__ == "__main__":
    print("🧪 Testing Merge K Sorted Lists Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the mergeKLists method")
        print("- Aim for O(n log k) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use divide and conquer or min heap approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log k)")
        print("- Consider using divide and conquer or min heap")
