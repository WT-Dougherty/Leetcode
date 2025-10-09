"""
Reverse Nodes In K Group - LeetCode Problem 25

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number
of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

import time
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.reverseKGroup(head1, 2)
    expected1 = [2, 1, 4, 3, 5]
    actual1 = linked_list_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for [1,2,3,4,5] k=2, expected {expected1}, got {actual1}"

    # Test Case 2: k=3
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = solution.reverseKGroup(head2, 3)
    expected2 = [3, 2, 1, 4, 5]
    actual2 = linked_list_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for [1,2,3,4,5] k=3, expected {expected2}, got {actual2}"

    # Test Case 3: k=1
    head3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = solution.reverseKGroup(head3, 1)
    expected3 = [1, 2, 3, 4, 5]
    actual3 = linked_list_to_list(result3)
    assert (
        actual3 == expected3
    ), f"Failed for [1,2,3,4,5] k=1, expected {expected3}, got {actual3}"

    # Test Case 4: k equals list length
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.reverseKGroup(head4, 5)
    expected4 = [5, 4, 3, 2, 1]
    actual4 = linked_list_to_list(result4)
    assert (
        actual4 == expected4
    ), f"Failed for [1,2,3,4,5] k=5, expected {expected4}, got {actual4}"

    # Test Case 5: Single element
    head5 = create_linked_list([1])
    result5 = solution.reverseKGroup(head5, 1)
    expected5 = [1]
    actual5 = linked_list_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for [1] k=1, expected {expected5}, got {actual5}"

    # Test Case 6: Two elements
    head6 = create_linked_list([1, 2])
    result6 = solution.reverseKGroup(head6, 2)
    expected6 = [2, 1]
    actual6 = linked_list_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for [1,2] k=2, expected {expected6}, got {actual6}"

    # Test Case 7: Empty list
    head7 = create_linked_list([])
    result7 = solution.reverseKGroup(head7, 1)
    expected7 = []
    actual7 = linked_list_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for [] k=1, expected {expected7}, got {actual7}"

    # Test Case 8: Large k
    head8 = create_linked_list([1, 2, 3, 4, 5, 6])
    result8 = solution.reverseKGroup(head8, 4)
    expected8 = [4, 3, 2, 1, 5, 6]
    actual8 = linked_list_to_list(result8)
    assert (
        actual8 == expected8
    ), f"Failed for [1,2,3,4,5,6] k=4, expected {expected8}, got {actual8}"

    # Test Case 9: Negative numbers
    head9 = create_linked_list([-1, -2, -3, -4, -5])
    result9 = solution.reverseKGroup(head9, 2)
    expected9 = [-2, -1, -4, -3, -5]
    actual9 = linked_list_to_list(result9)
    assert (
        actual9 == expected9
    ), f"Failed for negative numbers, expected {expected9}, got {actual9}"

    # Test Case 10: Maximum constraint
    head10 = create_linked_list(list(range(1, 5001)))
    result10 = solution.reverseKGroup(head10, 1000)
    # First 1000 elements should be reversed, rest unchanged
    expected10 = list(range(1000, 0, -1)) + list(range(1001, 5001))
    actual10 = linked_list_to_list(result10)
    assert actual10 == expected10, f"Failed for max constraint"

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
        values = list(range(size))
        head = create_linked_list(values)
        k = size // 10  # Use reasonable k value

        # Test approach
        start_time = time.time()
        result = solution.reverseKGroup(head, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has correct length
        actual = linked_list_to_list(result)
        assert len(actual) == size, f"Result length verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tReversed")

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

    # Edge Case 1: Maximum constraint length
    values = list(range(5000))
    head = create_linked_list(values)
    result = solution.reverseKGroup(head, 1000)
    actual = linked_list_to_list(result)
    assert len(actual) == 5000
    print(f"Maximum length (5k elements): ✅")

    # Edge Case 2: Maximum constraint k
    values = list(range(5000))
    head = create_linked_list(values)
    result = solution.reverseKGroup(head, 5000)
    actual = linked_list_to_list(result)
    expected = list(range(4999, -1, -1))
    assert actual == expected
    print(f"Maximum k (5k): ✅")

    # Edge Case 3: Maximum constraint values
    values = [1000] * 1000
    head = create_linked_list(values)
    result = solution.reverseKGroup(head, 100)
    actual = linked_list_to_list(result)
    expected = [1000] * 1000
    assert actual == expected
    print(f"Maximum constraint values: ✅")

    # Edge Case 4: Minimum constraint values
    values = [0] * 1000
    head = create_linked_list(values)
    result = solution.reverseKGroup(head, 100)
    actual = linked_list_to_list(result)
    expected = [0] * 1000
    assert actual == expected
    print(f"Minimum constraint values: ✅")

    # Edge Case 5: Different k values
    values = list(range(1000))
    for k in [1, 2, 5, 10, 100, 500]:
        head = create_linked_list(values)
        result = solution.reverseKGroup(head, k)
        actual = linked_list_to_list(result)
        assert len(actual) == 1000
    print(f"Different k values: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(100000))
    head = create_linked_list(values)

    start_time = time.time()
    result = solution.reverseKGroup(head, 10000)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(result)
    assert len(actual) == 100000

    print(f"Large dataset (100k elements, k=10k):")
    print(f"Time: {time1:.6f}s, Result: Reversed correctly")


if __name__ == "__main__":
    print("🧪 Testing Reverse Nodes In K Group Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the reverseKGroup method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use iterative approach with helper functions")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using iterative approach with helper functions")
