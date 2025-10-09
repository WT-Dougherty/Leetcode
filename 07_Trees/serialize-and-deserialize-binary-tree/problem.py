"""
Serialize And Deserialize Binary Tree - LeetCode Problem 297

Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized
to the original tree structure.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        pass


def create_binary_tree(values):
    """Helper function to create a binary tree from a list of values"""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    """Helper function to convert binary tree to list representation"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


def test_accuracy():
    """Test accuracy with various test cases"""
    codec = Codec()

    # Test Case 1: Basic case
    root1 = create_binary_tree([1, 2, 3, None, None, 4, 5])
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    actual1 = tree_to_list(deserialized1)
    expected1 = [1, 2, 3, None, None, 4, 5]
    assert (
        actual1 == expected1
    ), f"Failed for basic case, expected {expected1}, got {actual1}"

    # Test Case 2: Empty tree
    root2 = create_binary_tree([])
    serialized2 = codec.serialize(root2)
    deserialized2 = codec.deserialize(serialized2)
    actual2 = tree_to_list(deserialized2)
    expected2 = []
    assert (
        actual2 == expected2
    ), f"Failed for empty tree, expected {expected2}, got {actual2}"

    # Test Case 3: Single node
    root3 = create_binary_tree([1])
    serialized3 = codec.serialize(root3)
    deserialized3 = codec.deserialize(serialized3)
    actual3 = tree_to_list(deserialized3)
    expected3 = [1]
    assert (
        actual3 == expected3
    ), f"Failed for single node, expected {expected3}, got {actual3}"

    # Test Case 4: Two nodes
    root4 = create_binary_tree([1, 2])
    serialized4 = codec.serialize(root4)
    deserialized4 = codec.deserialize(serialized4)
    actual4 = tree_to_list(deserialized4)
    expected4 = [1, 2]
    assert (
        actual4 == expected4
    ), f"Failed for two nodes, expected {expected4}, got {actual4}"

    # Test Case 5: Left skewed tree
    root5 = create_binary_tree([1, 2, None, 3, None, 4, None])
    serialized5 = codec.serialize(root5)
    deserialized5 = codec.deserialize(serialized5)
    actual5 = tree_to_list(deserialized5)
    expected5 = [1, 2, None, 3, None, 4, None]
    assert (
        actual5 == expected5
    ), f"Failed for left skewed tree, expected {expected5}, got {actual5}"

    # Test Case 6: Right skewed tree
    root6 = create_binary_tree([1, None, 2, None, 3, None, 4])
    serialized6 = codec.serialize(root6)
    deserialized6 = codec.deserialize(serialized6)
    actual6 = tree_to_list(deserialized6)
    expected6 = [1, None, 2, None, 3, None, 4]
    assert (
        actual6 == expected6
    ), f"Failed for right skewed tree, expected {expected6}, got {actual6}"

    # Test Case 7: Perfect binary tree
    root7 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    serialized7 = codec.serialize(root7)
    deserialized7 = codec.deserialize(serialized7)
    actual7 = tree_to_list(deserialized7)
    expected7 = [1, 2, 3, 4, 5, 6, 7]
    assert (
        actual7 == expected7
    ), f"Failed for perfect binary tree, expected {expected7}, got {actual7}"

    # Test Case 8: Negative values
    root8 = create_binary_tree([-1, -2, -3])
    serialized8 = codec.serialize(root8)
    deserialized8 = codec.deserialize(serialized8)
    actual8 = tree_to_list(deserialized8)
    expected8 = [-1, -2, -3]
    assert (
        actual8 == expected8
    ), f"Failed for negative values, expected {expected8}, got {actual8}"

    # Test Case 9: Large values
    root9 = create_binary_tree([1000, 2000, 3000])
    serialized9 = codec.serialize(root9)
    deserialized9 = codec.deserialize(serialized9)
    actual9 = tree_to_list(deserialized9)
    expected9 = [1000, 2000, 3000]
    assert (
        actual9 == expected9
    ), f"Failed for large values, expected {expected9}, got {actual9}"

    # Test Case 10: Maximum constraint
    values = list(range(10000))
    root10 = create_binary_tree(values)
    serialized10 = codec.serialize(root10)
    deserialized10 = codec.deserialize(serialized10)
    actual10 = tree_to_list(deserialized10)
    expected10 = values
    assert actual10 == expected10, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    codec = Codec()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        values = list(range(size))
        root = create_binary_tree(values)

        # Test approach
        start_time = time.time()
        serialized = codec.serialize(root)
        deserialized = codec.deserialize(serialized)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        actual = tree_to_list(deserialized)
        assert actual == values, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tSerialized/Deserialized")

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
    codec = Codec()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    values = list(range(10000))
    root = create_binary_tree(values)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    actual = tree_to_list(deserialized)
    assert actual == values
    print(f"Maximum length (10k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [1000] * 1000
    root = create_binary_tree(values)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    actual = tree_to_list(deserialized)
    assert actual == values
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-1000] * 1000
    root = create_binary_tree(values)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    actual = tree_to_list(deserialized)
    assert actual == values
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Single path tree
    values = list(range(100))
    root = create_binary_tree(values)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    actual = tree_to_list(deserialized)
    assert actual == values
    print(f"Single path tree: ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    actual = tree_to_list(deserialized)
    assert actual == values
    print(f"Complete binary tree: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    codec = Codec()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(10000))
    root = create_binary_tree(values)

    start_time = time.time()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    time1 = time.time() - start_time

    # Verify result
    actual = tree_to_list(deserialized)
    assert actual == values

    print(f"Large dataset (10k elements):")
    print(f"Time: {time1:.6f}s, Result: Serialized/Deserialized correctly")


if __name__ == "__main__":
    print("🧪 Testing Serialize And Deserialize Binary Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the Codec class")
        print("- Aim for O(n) time complexity for both serialize and deserialize")
        print("- Handle all edge cases correctly")
        print("- Use preorder traversal with null markers")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using preorder traversal with null markers")
