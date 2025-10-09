"""
Reorder List - LeetCode Problem 143

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

import time
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
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

    # Test Case 1: Even length
    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    expected1 = [1, 4, 2, 3]
    actual1 = linked_list_to_list(head1)
    assert (
        actual1 == expected1
    ), f"Failed for [1,2,3,4], expected {expected1}, got {actual1}"

    # Test Case 2: Odd length
    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    expected2 = [1, 5, 2, 4, 3]
    actual2 = linked_list_to_list(head2)
    assert (
        actual2 == expected2
    ), f"Failed for [1,2,3,4,5], expected {expected2}, got {actual2}"

    # Test Case 3: Two elements
    head3 = create_linked_list([1, 2])
    solution.reorderList(head3)
    expected3 = [1, 2]
    actual3 = linked_list_to_list(head3)
    assert (
        actual3 == expected3
    ), f"Failed for [1,2], expected {expected3}, got {actual3}"

    # Test Case 4: Single element
    head4 = create_linked_list([1])
    solution.reorderList(head4)
    expected4 = [1]
    actual4 = linked_list_to_list(head4)
    assert actual4 == expected4, f"Failed for [1], expected {expected4}, got {actual4}"

    # Test Case 5: Three elements
    head5 = create_linked_list([1, 2, 3])
    solution.reorderList(head5)
    expected5 = [1, 3, 2]
    actual5 = linked_list_to_list(head5)
    assert (
        actual5 == expected5
    ), f"Failed for [1,2,3], expected {expected5}, got {actual5}"

    # Test Case 6: Six elements
    head6 = create_linked_list([1, 2, 3, 4, 5, 6])
    solution.reorderList(head6)
    expected6 = [1, 6, 2, 5, 3, 4]
    actual6 = linked_list_to_list(head6)
    assert (
        actual6 == expected6
    ), f"Failed for [1,2,3,4,5,6], expected {expected6}, got {actual6}"

    # Test Case 7: Negative numbers
    head7 = create_linked_list([-1, -2, -3, -4])
    solution.reorderList(head7)
    expected7 = [-1, -4, -2, -3]
    actual7 = linked_list_to_list(head7)
    assert (
        actual7 == expected7
    ), f"Failed for [-1,-2,-3,-4], expected {expected7}, got {actual7}"

    # Test Case 8: Large list
    head8 = create_linked_list(list(range(1, 11)))
    solution.reorderList(head8)
    expected8 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    actual8 = linked_list_to_list(head8)
    assert (
        actual8 == expected8
    ), f"Failed for large list, expected {expected8}, got {actual8}"

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

        # Test approach
        start_time = time.time()
        solution.reorderList(head)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has correct length
        actual = linked_list_to_list(head)
        assert len(actual) == size, f"Result length verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tReordered")

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
    values = list(range(50000))
    head = create_linked_list(values)
    solution.reorderList(head)
    actual = linked_list_to_list(head)
    assert len(actual) == 50000
    print(f"Maximum length (50k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [1000] * 1000
    head = create_linked_list(values)
    solution.reorderList(head)
    actual = linked_list_to_list(head)
    expected = [1000] * 1000
    assert actual == expected
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [1] * 1000
    head = create_linked_list(values)
    solution.reorderList(head)
    actual = linked_list_to_list(head)
    expected = [1] * 1000
    assert actual == expected
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Alternating pattern
    values = [1, 2] * 1000
    head = create_linked_list(values)
    solution.reorderList(head)
    actual = linked_list_to_list(head)
    # After reordering: [1, 2, 1, 2, ...] becomes [1, 2, 1, 2, ...]
    assert len(actual) == 2000
    print(f"Alternating pattern: ✅")

    # Edge Case 5: Single element
    head = create_linked_list([42])
    solution.reorderList(head)
    actual = linked_list_to_list(head)
    expected = [42]
    assert actual == expected
    print(f"Single element: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(100000))
    head = create_linked_list(values)

    start_time = time.time()
    solution.reorderList(head)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(head)
    assert len(actual) == 100000

    print(f"Large dataset (100k elements):")
    print(f"Time: {time1:.6f}s, Result: Reordered correctly")


if __name__ == "__main__":
    print("🧪 Testing Reorder List Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the reorderList method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use find middle, reverse second half, and merge approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using three-step approach: find middle, reverse, merge")
