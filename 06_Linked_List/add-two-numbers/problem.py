"""
Add Two Numbers - LeetCode Problem 2

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

import time
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = cur = end_node = ListNode()
        carry, sum = 0, 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                sum = l1.val + l2.val + carry
                if sum > 9:
                    carry = 1
                    sum -= 10
                else:
                    carry = 0
                l1 = l1.next
                l2 = l2.next
            elif l2 == None:
                sum = l1.val + carry
                if sum > 9:
                    carry = 1
                    sum -= 10
                else:
                    carry = 0
                l1 = l1.next
            else:
                sum = l2.val + carry
                if sum > 9:
                    carry = 1
                    sum -= 10
                else:
                    carry = 0
                l2 = l2.next
            cur.val = sum
            cur.next = ListNode(next=None)
            end_node = cur
            cur = cur.next
        if carry == 1:
            cur.val = 1
        else:
            end_node.next = None
        return ans


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
    l1_1 = create_linked_list([2, 4, 3])
    l2_1 = create_linked_list([5, 6, 4])
    result1 = solution.addTwoNumbers(l1_1, l2_1)
    expected1 = [7, 0, 8]
    actual1 = linked_list_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for [2,4,3] + [5,6,4], expected {expected1}, got {actual1}"

    # Test Case 2: Zeros
    l1_2 = create_linked_list([0])
    l2_2 = create_linked_list([0])
    result2 = solution.addTwoNumbers(l1_2, l2_2)
    expected2 = [0]
    actual2 = linked_list_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for [0] + [0], expected {expected2}, got {actual2}"

    # Test Case 3: Carry over
    l1_3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2_3 = create_linked_list([9, 9, 9, 9])
    result3 = solution.addTwoNumbers(l1_3, l2_3)
    expected3 = [8, 9, 9, 9, 0, 0, 0, 1]
    actual3 = linked_list_to_list(result3)
    assert (
        actual3 == expected3
    ), f"Failed for carry case, expected {expected3}, got {actual3}"

    # Test Case 4: Different lengths
    l1_4 = create_linked_list([1, 2, 3])
    l2_4 = create_linked_list([4, 5])
    result4 = solution.addTwoNumbers(l1_4, l2_4)
    expected4 = [5, 7, 3]
    actual4 = linked_list_to_list(result4)
    assert (
        actual4 == expected4
    ), f"Failed for different lengths, expected {expected4}, got {actual4}"

    # Test Case 5: Single digits
    l1_5 = create_linked_list([5])
    l2_5 = create_linked_list([5])
    result5 = solution.addTwoNumbers(l1_5, l2_5)
    expected5 = [0, 1]
    actual5 = linked_list_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for single digits, expected {expected5}, got {actual5}"

    # Test Case 6: One empty (should not happen per constraints)
    l1_6 = create_linked_list([1, 2])
    l2_6 = create_linked_list([])
    result6 = solution.addTwoNumbers(l1_6, l2_6)
    expected6 = [1, 2]
    actual6 = linked_list_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for one empty, expected {expected6}, got {actual6}"

    # Test Case 7: Large numbers
    l1_7 = create_linked_list([9, 9, 9])
    l2_7 = create_linked_list([1])
    result7 = solution.addTwoNumbers(l1_7, l2_7)
    expected7 = [0, 0, 0, 1]
    actual7 = linked_list_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for large numbers, expected {expected7}, got {actual7}"

    # Test Case 8: Maximum constraint
    l1_8 = create_linked_list([9] * 100)
    l2_8 = create_linked_list([1])
    result8 = solution.addTwoNumbers(l1_8, l2_8)
    expected8 = [0] * 100 + [1]
    actual8 = linked_list_to_list(result8)
    assert actual8 == expected8, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(max(m, n))"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(50, 50), (100, 100), (200, 200)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for m, n in test_sizes:
        # Generate test data
        l1_values = [random.randint(0, 9) for _ in range(m)]
        l2_values = [random.randint(0, 9) for _ in range(n)]
        l1 = create_linked_list(l1_values)
        l2 = create_linked_list(l2_values)

        # Test approach
        start_time = time.time()
        result = solution.addTwoNumbers(l1, l2)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has reasonable length
        actual = linked_list_to_list(result)
        max_len = max(m, n) + 1  # Maximum possible length
        assert (
            len(actual) <= max_len
        ), f"Result length verification failed for size ({m}, {n})"

        print(f"{m}+{n}\t{elapsed_time:.6f}s\tAdded")

    # Verify O(max(m, n)) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(max(m, n)) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            expected_ratio = max(m2, n2) / max(m1, n1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(max(m, n)): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(max(m, n))")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m * n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(max(m, n)), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(max(m, n))")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    l1_values = [9] * 100
    l2_values = [9] * 100
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    actual = linked_list_to_list(result)
    assert len(actual) == 101  # 100 + 100 with carry
    print(f"Maximum length (100+100 elements): ✅")

    # Edge Case 2: Maximum constraint values
    l1_values = [9] * 50
    l2_values = [9] * 50
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    actual = linked_list_to_list(result)
    assert len(actual) == 51
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    l1_values = [0] * 50
    l2_values = [0] * 50
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    actual = linked_list_to_list(result)
    assert actual == [0] * 50
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: One much longer
    l1_values = [9] * 100
    l2_values = [1]
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    actual = linked_list_to_list(result)
    assert len(actual) == 101
    print(f"One much longer: ✅")

    # Edge Case 5: All nines
    l1_values = [9, 9, 9]
    l2_values = [9, 9, 9]
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    actual = linked_list_to_list(result)
    expected = [8, 9, 9, 1]
    assert actual == expected
    print(f"All nines: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    l1_values = [random.randint(0, 9) for _ in range(100)]
    l2_values = [random.randint(0, 9) for _ in range(100)]
    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)

    start_time = time.time()
    result = solution.addTwoNumbers(l1, l2)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list(result)
    assert len(actual) <= 101

    print(f"Large dataset (100+100 elements):")
    print(f"Time: {time1:.6f}s, Result: Added correctly")


if __name__ == "__main__":
    print("🧪 Testing Add Two Numbers Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the addTwoNumbers method")
        print("- Aim for O(max(m, n)) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use carry variable and dummy head")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(max(m, n))")
        print("- Consider using iterative approach with carry handling")
