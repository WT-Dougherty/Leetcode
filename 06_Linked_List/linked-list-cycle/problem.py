"""
Linked List Cycle - LeetCode Problem 141

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

import time
import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


def create_linked_list_with_cycle(values, cycle_pos):
    """Helper function to create a linked list with optional cycle"""
    if not values:
        return None

    # Create all nodes
    nodes = []
    for val in values:
        node = ListNode(val)
        nodes.append(node)

    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Set cycle if specified
    if cycle_pos >= 0 and cycle_pos < len(nodes):
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0] if nodes else None


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Cycle exists
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    result1 = solution.hasCycle(head1)
    assert result1 == True, f"Failed for cycle at pos 1, expected True, got {result1}"

    # Test Case 2: Cycle at beginning
    head2 = create_linked_list_with_cycle([1, 2], 0)
    result2 = solution.hasCycle(head2)
    assert result2 == True, f"Failed for cycle at pos 0, expected True, got {result2}"

    # Test Case 3: No cycle
    head3 = create_linked_list_with_cycle([1], -1)
    result3 = solution.hasCycle(head3)
    assert result3 == False, f"Failed for no cycle, expected False, got {result3}"

    # Test Case 4: Single node no cycle
    head4 = create_linked_list_with_cycle([1], -1)
    result4 = solution.hasCycle(head4)
    assert (
        result4 == False
    ), f"Failed for single node no cycle, expected False, got {result4}"

    # Test Case 5: Two nodes no cycle
    head5 = create_linked_list_with_cycle([1, 2], -1)
    result5 = solution.hasCycle(head5)
    assert (
        result5 == False
    ), f"Failed for two nodes no cycle, expected False, got {result5}"

    # Test Case 6: Two nodes with cycle
    head6 = create_linked_list_with_cycle([1, 2], 0)
    result6 = solution.hasCycle(head6)
    assert (
        result6 == True
    ), f"Failed for two nodes with cycle, expected True, got {result6}"

    # Test Case 7: Large cycle
    head7 = create_linked_list_with_cycle(list(range(10)), 5)
    result7 = solution.hasCycle(head7)
    assert result7 == True, f"Failed for large cycle, expected True, got {result7}"

    # Test Case 8: Self cycle
    head8 = create_linked_list_with_cycle([1], 0)
    result8 = solution.hasCycle(head8)
    assert result8 == True, f"Failed for self cycle, expected True, got {result8}"

    # Test Case 9: Empty list
    head9 = create_linked_list_with_cycle([], -1)
    result9 = solution.hasCycle(head9)
    assert result9 == False, f"Failed for empty list, expected False, got {result9}"

    # Test Case 10: Long list no cycle
    head10 = create_linked_list_with_cycle(list(range(100)), -1)
    result10 = solution.hasCycle(head10)
    assert (
        result10 == False
    ), f"Failed for long list no cycle, expected False, got {result10}"

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
        # Generate test data - no cycle (worst case for cycle detection)
        values = list(range(size))
        head = create_linked_list_with_cycle(values, -1)

        # Test approach
        start_time = time.time()
        result = solution.hasCycle(head)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result == False, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

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
    values = list(range(10000))
    head = create_linked_list_with_cycle(values, -1)
    result = solution.hasCycle(head)
    assert result == False
    print(f"Maximum length (10k elements, no cycle): ✅")

    # Edge Case 2: Maximum constraint length with cycle
    values = list(range(10000))
    head = create_linked_list_with_cycle(values, 5000)
    result = solution.hasCycle(head)
    assert result == True
    print(f"Maximum length (10k elements, with cycle): ✅")

    # Edge Case 3: Maximum constraint values
    values = [100000] * 1000
    head = create_linked_list_with_cycle(values, 500)
    result = solution.hasCycle(head)
    assert result == True
    print(f"Maximum constraint values: ✅")

    # Edge Case 4: Minimum constraint values
    values = [-100000] * 1000
    head = create_linked_list_with_cycle(values, -1)
    result = solution.hasCycle(head)
    assert result == False
    print(f"Minimum constraint values: ✅")

    # Edge Case 5: Cycle at different positions
    for cycle_pos in [0, 100, 500, 999]:
        values = list(range(1000))
        head = create_linked_list_with_cycle(values, cycle_pos)
        result = solution.hasCycle(head)
        assert result == True
    print(f"Cycle at different positions: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset with cycle
    values = list(range(100000))
    head = create_linked_list_with_cycle(values, 50000)

    start_time = time.time()
    result = solution.hasCycle(head)
    time1 = time.time() - start_time

    assert result == True

    print(f"Large dataset (100k elements, with cycle):")
    print(f"Time: {time1:.6f}s, Result: {result}")

    # Large dataset without cycle
    head2 = create_linked_list_with_cycle(values, -1)

    start_time = time.time()
    result2 = solution.hasCycle(head2)
    time2 = time.time() - start_time

    assert result2 == False

    print(f"\nLarge dataset (100k elements, no cycle):")
    print(f"Time: {time2:.6f}s, Result: {result2}")


if __name__ == "__main__":
    print("🧪 Testing Linked List Cycle Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the hasCycle method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use Floyd's cycle detection algorithm (tortoise and hare)")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using Floyd's cycle detection algorithm")
