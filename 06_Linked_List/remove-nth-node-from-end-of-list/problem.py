"""
Remove Nth Node From End of List - LeetCode Problem 19

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
    result1 = solution.removeNthFromEnd(head1, 2)
    expected1 = [1, 2, 3, 5]
    actual1 = linked_list_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for [1,2,3,4,5] n=2, expected {expected1}, got {actual1}"

    # Test Case 2: Remove first element
    head2 = create_linked_list([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    expected2 = []
    actual2 = linked_list_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for [1] n=1, expected {expected2}, got {actual2}"

    # Test Case 3: Remove last element
    head3 = create_linked_list([1, 2])
    result3 = solution.removeNthFromEnd(head3, 1)
    expected3 = [1]
    actual3 = linked_list_to_list(result3)
    assert (
        actual3 == expected3
    ), f"Failed for [1,2] n=1, expected {expected3}, got {actual3}"

    # Test Case 4: Remove second to last
    head4 = create_linked_list([1, 2, 3, 4])
    result4 = solution.removeNthFromEnd(head4, 2)
    expected4 = [1, 2, 4]
    actual4 = linked_list_to_list(result4)
    assert (
        actual4 == expected4
    ), f"Failed for [1,2,3,4] n=2, expected {expected4}, got {actual4}"

    # Test Case 5: Remove first element from longer list
    head5 = create_linked_list([1, 2, 3, 4, 5])
    result5 = solution.removeNthFromEnd(head5, 5)
    expected5 = [2, 3, 4, 5]
    actual5 = linked_list_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for [1,2,3,4,5] n=5, expected {expected5}, got {actual5}"

    # Test Case 6: Remove last element from longer list
    head6 = create_linked_list([1, 2, 3, 4, 5])
    result6 = solution.removeNthFromEnd(head6, 1)
    expected6 = [1, 2, 3, 4]
    actual6 = linked_list_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for [1,2,3,4,5] n=1, expected {expected6}, got {actual6}"

    # Test Case 7: Negative numbers
    head7 = create_linked_list([-1, -2, -3, -4])
    result7 = solution.removeNthFromEnd(head7, 2)
    expected7 = [-1, -2, -4]
    actual7 = linked_list_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for [-1,-2,-3,-4] n=2, expected {expected7}, got {actual7}"

    # Test Case 8: Maximum constraint
    head8 = create_linked_list(list(range(1, 31)))
    result8 = solution.removeNthFromEnd(head8, 15)
    expected8 = list(range(1, 16)) + list(range(17, 31))
    actual8 = linked_list_to_list(result8)
    assert actual8 == expected8, f"Failed for max constraint list"

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
        n = size // 2  # Remove middle element

        # Test approach
        start_time = time.time()
        result = solution.removeNthFromEnd(head, n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has correct length
        actual = linked_list_to_list(result)
        assert (
            len(actual) == size - 1
        ), f"Result length verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tRemoved")

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

            if not (min_expected <= actual <= max_expected):
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
    values = list(range(1, 31))
    head = create_linked_list(values)
    result = solution.removeNthFromEnd(head, 1)
    actual = linked_list_to_list(result)
    assert len(actual) == 29
    print(f"Maximum length (30 elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 30
    head = create_linked_list(values)
    result = solution.removeNthFromEnd(head, 15)
    actual = linked_list_to_list(result)
    assert len(actual) == 29
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [0] * 30
    head = create_linked_list(values)
    result = solution.removeNthFromEnd(head, 1)
    actual = linked_list_to_list(result)
    assert len(actual) == 29
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Remove first element
    values = list(range(1, 31))
    head = create_linked_list(values)
    result = solution.removeNthFromEnd(head, 30)
    actual = linked_list_to_list(result)
    expected = list(range(2, 31))
    assert actual == expected
    print(f"Remove first element: ✅")

    # Edge Case 5: Remove last element
    values = list(range(1, 31))
    head = create_linked_list(values)
    result = solution.removeNthFromEnd(head, 1)
    actual = linked_list_to_list(result)
    expected = list(range(1, 30))
    assert actual == expected
    print(f"Remove last element: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(100000))
    head = create_linked_list(values)

    start_time = time.time()
    result = solution.removeNthFromEnd(head, 50000)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(result)
    assert len(actual) == 99999

    print(f"Large dataset (100k elements, remove middle):")
    print(f"Time: {time1:.6f}s, Result: Removed correctly")


if __name__ == "__main__":
    print("🧪 Testing Remove Nth Node From End of List Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the removeNthFromEnd method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two-pointer technique")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using two-pointer technique with dummy node")
