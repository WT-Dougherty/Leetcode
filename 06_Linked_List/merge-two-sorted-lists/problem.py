"""
Merge Two Sorted Lists - LeetCode Problem 21

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists.
Return the head of the merged linked list.
"""

import time
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
    list1_1 = create_linked_list([1, 2, 4])
    list2_1 = create_linked_list([1, 3, 4])
    result1 = solution.mergeTwoLists(list1_1, list2_1)
    expected1 = [1, 1, 2, 3, 4, 4]
    actual1 = linked_list_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for [1,2,4] and [1,3,4], expected {expected1}, got {actual1}"

    # Test Case 2: Empty lists
    list1_2 = create_linked_list([])
    list2_2 = create_linked_list([])
    result2 = solution.mergeTwoLists(list1_2, list2_2)
    expected2 = []
    actual2 = linked_list_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for [] and [], expected {expected2}, got {actual2}"

    # Test Case 3: One empty list
    list1_3 = create_linked_list([])
    list2_3 = create_linked_list([0])
    result3 = solution.mergeTwoLists(list1_3, list2_3)
    expected3 = [0]
    actual3 = linked_list_to_list(result3)
    assert (
        actual3 == expected3
    ), f"Failed for [] and [0], expected {expected3}, got {actual3}"

    # Test Case 4: Single elements
    list1_4 = create_linked_list([1])
    list2_4 = create_linked_list([2])
    result4 = solution.mergeTwoLists(list1_4, list2_4)
    expected4 = [1, 2]
    actual4 = linked_list_to_list(result4)
    assert (
        actual4 == expected4
    ), f"Failed for [1] and [2], expected {expected4}, got {actual4}"

    # Test Case 5: Negative numbers
    list1_5 = create_linked_list([-5, -3, -1])
    list2_5 = create_linked_list([-4, -2, 0])
    result5 = solution.mergeTwoLists(list1_5, list2_5)
    expected5 = [-5, -4, -3, -2, -1, 0]
    actual5 = linked_list_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for [-5,-3,-1] and [-4,-2,0], expected {expected5}, got {actual5}"

    # Test Case 6: One list much longer
    list1_6 = create_linked_list([1, 2, 3, 4, 5])
    list2_6 = create_linked_list([6])
    result6 = solution.mergeTwoLists(list1_6, list2_6)
    expected6 = [1, 2, 3, 4, 5, 6]
    actual6 = linked_list_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for [1,2,3,4,5] and [6], expected {expected6}, got {actual6}"

    # Test Case 7: All same values
    list1_7 = create_linked_list([1, 1, 1])
    list2_7 = create_linked_list([1, 1, 1])
    result7 = solution.mergeTwoLists(list1_7, list2_7)
    expected7 = [1, 1, 1, 1, 1, 1]
    actual7 = linked_list_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for [1,1,1] and [1,1,1], expected {expected7}, got {actual7}"

    # Test Case 8: Maximum constraint
    list1_8 = create_linked_list(list(range(0, 50, 2)))  # Even numbers
    list2_8 = create_linked_list(list(range(1, 50, 2)))  # Odd numbers
    result8 = solution.mergeTwoLists(list1_8, list2_8)
    expected8 = list(range(50))
    actual8 = linked_list_to_list(result8)
    assert actual8 == expected8, f"Failed for max constraint lists"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m + n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(25, 25), (50, 50), (100, 100)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for m, n in test_sizes:
        # Generate test data
        list1_values = sorted([random.randint(-100, 100) for _ in range(m)])
        list2_values = sorted([random.randint(-100, 100) for _ in range(n)])
        list1 = create_linked_list(list1_values)
        list2 = create_linked_list(list2_values)

        # Test approach
        start_time = time.time()
        result = solution.mergeTwoLists(list1, list2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is sorted
        actual = linked_list_to_list(result)
        expected = sorted(list1_values + list2_values)
        assert actual == expected, f"Result verification failed for size ({m}, {n})"

        print(f"{m}+{n}\t{elapsed_time:.6f}s\tMerged")

    # Verify O(m + n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m + n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            expected_ratio = (m2 + n2) / (m1 + n1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m + n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (min_expected <= actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m + n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m * n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m + n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m + n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    list1_values = list(range(0, 50, 2))
    list2_values = list(range(1, 50, 2))
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    result = solution.mergeTwoLists(list1, list2)
    actual = linked_list_to_list(result)
    expected = list(range(50))
    assert actual == expected
    print(f"Maximum length (50 elements each): ✅")

    # Edge Case 2: Maximum constraint values
    list1_values = [100] * 25
    list2_values = [100] * 25
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    result = solution.mergeTwoLists(list1, list2)
    actual = linked_list_to_list(result)
    expected = [100] * 50
    assert actual == expected
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    list1_values = [-100] * 25
    list2_values = [-100] * 25
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    result = solution.mergeTwoLists(list1, list2)
    actual = linked_list_to_list(result)
    expected = [-100] * 50
    assert actual == expected
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: One list empty
    list1_values = []
    list2_values = list(range(50))
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    result = solution.mergeTwoLists(list1, list2)
    actual = linked_list_to_list(result)
    expected = list(range(50))
    assert actual == expected
    print(f"One list empty: ✅")

    # Edge Case 5: Single elements
    list1_values = [42]
    list2_values = [43]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    result = solution.mergeTwoLists(list1, list2)
    actual = linked_list_to_list(result)
    expected = [42, 43]
    assert actual == expected
    print(f"Single elements: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    list1_values = sorted([random.randint(-100, 100) for _ in range(50)])
    list2_values = sorted([random.randint(-100, 100) for _ in range(50)])
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)

    start_time = time.time()
    result = solution.mergeTwoLists(list1, list2)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(result)
    expected = sorted(list1_values + list2_values)
    assert actual == expected

    print(f"Large dataset (50+50 elements):")
    print(f"Time: {time1:.6f}s, Result: Merged correctly")


if __name__ == "__main__":
    print("🧪 Testing Merge Two Sorted Lists Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the mergeTwoLists method")
        print("- Aim for O(m + n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two-pointer technique")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m + n)")
        print("- Consider using iterative approach with two pointers")
