"""
Copy List With Random Pointer - LeetCode Problem 138

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node. Both
the next and random pointer of the new nodes should point to new nodes in the copied list such
that the pointers in the original list and copied list represent the same list state.
"""

import time
import random
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        pass


def create_linked_list_with_random(values_and_randoms):
    """Helper function to create a linked list with random pointers"""
    if not values_and_randoms:
        return None

    # First pass: create all nodes
    nodes = []
    for val, _ in values_and_randoms:
        node = Node(val)
        nodes.append(node)

    # Second pass: set next and random pointers
    for i, (_, random_idx) in enumerate(values_and_randoms):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]

    return nodes[0] if nodes else None


def linked_list_to_list_with_random(head):
    """Helper function to convert linked list with random pointers to Python list"""
    if not head:
        return []

    # Create mapping from node to index
    node_to_index = {}
    current = head
    index = 0
    while current:
        node_to_index[current] = index
        current = current.next
        index += 1

    # Convert to list format
    result = []
    current = head
    while current:
        random_idx = node_to_index.get(current.random) if current.random else None
        result.append([current.val, random_idx])
        current = current.next

    return result


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    values_and_randoms1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head1 = create_linked_list_with_random(values_and_randoms1)
    result1 = solution.copyRandomList(head1)
    actual1 = linked_list_to_list_with_random(result1)
    expected1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    assert (
        actual1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {actual1}"

    # Test Case 2: Simple case
    values_and_randoms2 = [[1, 1], [2, 1]]
    head2 = create_linked_list_with_random(values_and_randoms2)
    result2 = solution.copyRandomList(head2)
    actual2 = linked_list_to_list_with_random(result2)
    expected2 = [[1, 1], [2, 1]]
    assert (
        actual2 == expected2
    ), f"Failed for simple case, expected {expected2}, got {actual2}"

    # Test Case 3: All null random pointers
    values_and_randoms3 = [[3, None], [3, 0], [3, None]]
    head3 = create_linked_list_with_random(values_and_randoms3)
    result3 = solution.copyRandomList(head3)
    actual3 = linked_list_to_list_with_random(result3)
    expected3 = [[3, None], [3, 0], [3, None]]
    assert (
        actual3 == expected3
    ), f"Failed for null random case, expected {expected3}, got {actual3}"

    # Test Case 4: Single node
    values_and_randoms4 = [[1, None]]
    head4 = create_linked_list_with_random(values_and_randoms4)
    result4 = solution.copyRandomList(head4)
    actual4 = linked_list_to_list_with_random(result4)
    expected4 = [[1, None]]
    assert (
        actual4 == expected4
    ), f"Failed for single node, expected {expected4}, got {actual4}"

    # Test Case 5: Single node with self reference
    values_and_randoms5 = [[1, 0]]
    head5 = create_linked_list_with_random(values_and_randoms5)
    result5 = solution.copyRandomList(head5)
    actual5 = linked_list_to_list_with_random(result5)
    expected5 = [[1, 0]]
    assert (
        actual5 == expected5
    ), f"Failed for self reference, expected {expected5}, got {actual5}"

    # Test Case 6: Empty list
    head6 = create_linked_list_with_random([])
    result6 = solution.copyRandomList(head6)
    actual6 = linked_list_to_list_with_random(result6)
    expected6 = []
    assert (
        actual6 == expected6
    ), f"Failed for empty list, expected {expected6}, got {actual6}"

    # Test Case 7: Two nodes
    values_and_randoms7 = [[1, None], [2, None]]
    head7 = create_linked_list_with_random(values_and_randoms7)
    result7 = solution.copyRandomList(head7)
    actual7 = linked_list_to_list_with_random(result7)
    expected7 = [[1, None], [2, None]]
    assert (
        actual7 == expected7
    ), f"Failed for two nodes, expected {expected7}, got {actual7}"

    # Test Case 8: Complex case
    values_and_randoms8 = [[1, 2], [2, 0], [3, 1], [4, None]]
    head8 = create_linked_list_with_random(values_and_randoms8)
    result8 = solution.copyRandomList(head8)
    actual8 = linked_list_to_list_with_random(result8)
    expected8 = [[1, 2], [2, 0], [3, 1], [4, None]]
    assert (
        actual8 == expected8
    ), f"Failed for complex case, expected {expected8}, got {actual8}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        values_and_randoms = []
        for i in range(size):
            val = random.randint(-10000, 10000)
            random_idx = random.randint(0, size - 1) if random.random() > 0.5 else None
            values_and_randoms.append([val, random_idx])

        head = create_linked_list_with_random(values_and_randoms)

        # Test approach
        start_time = time.time()
        result = solution.copyRandomList(head)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has correct length
        actual = linked_list_to_list_with_random(result)
        assert len(actual) == size, f"Result length verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tCopied")

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
    values_and_randoms = []
    for i in range(1000):
        val = random.randint(-10000, 10000)
        random_idx = random.randint(0, 999) if random.random() > 0.5 else None
        values_and_randoms.append([val, random_idx])

    head = create_linked_list_with_random(values_and_randoms)
    result = solution.copyRandomList(head)
    actual = linked_list_to_list_with_random(result)
    assert len(actual) == 1000
    print(f"Maximum length (1000 elements): ✅")

    # Edge Case 2: Maximum constraint values
    values_and_randoms = [[10000, None], [10000, 0], [10000, 1]]
    head = create_linked_list_with_random(values_and_randoms)
    result = solution.copyRandomList(head)
    actual = linked_list_to_list_with_random(result)
    expected = [[10000, None], [10000, 0], [10000, 1]]
    assert actual == expected
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values_and_randoms = [[-10000, None], [-10000, 0], [-10000, 1]]
    head = create_linked_list_with_random(values_and_randoms)
    result = solution.copyRandomList(head)
    actual = linked_list_to_list_with_random(result)
    expected = [[-10000, None], [-10000, 0], [-10000, 1]]
    assert actual == expected
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: All self-referencing
    values_and_randoms = [[i, i] for i in range(100)]
    head = create_linked_list_with_random(values_and_randoms)
    result = solution.copyRandomList(head)
    actual = linked_list_to_list_with_random(result)
    expected = [[i, i] for i in range(100)]
    assert actual == expected
    print(f"All self-referencing: ✅")

    # Edge Case 5: All null random pointers
    values_and_randoms = [[i, None] for i in range(100)]
    head = create_linked_list_with_random(values_and_randoms)
    result = solution.copyRandomList(head)
    actual = linked_list_to_list_with_random(result)
    expected = [[i, None] for i in range(100)]
    assert actual == expected
    print(f"All null random pointers: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values_and_randoms = []
    for i in range(10000):
        val = random.randint(-10000, 10000)
        random_idx = random.randint(0, 9999) if random.random() > 0.5 else None
        values_and_randoms.append([val, random_idx])

    head = create_linked_list_with_random(values_and_randoms)

    start_time = time.time()
    result = solution.copyRandomList(head)
    time1 = time.time() - start_time

    # Verify result
    actual = linked_list_to_list_with_random(result)
    assert len(actual) == 10000

    print(f"Large dataset (10k elements):")
    print(f"Time: {time1:.6f}s, Result: Copied correctly")


if __name__ == "__main__":
    print("🧪 Testing Copy List With Random Pointer Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the copyRandomList method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use hash map or iterative approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash map to store node mappings")
