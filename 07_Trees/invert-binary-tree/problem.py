"""
Invert Binary Tree - LeetCode Problem 226

Given the root of a binary tree, invert the tree, and return its root.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
    solution = Solution()

    # Test Case 1: Basic case
    root1 = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
    result1 = solution.invertTree(root1)
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    actual1 = tree_to_list(result1)
    assert (
        actual1 == expected1
    ), f"Failed for [4,2,7,1,3,6,9], expected {expected1}, got {actual1}"

    # Test Case 2: Simple case
    root2 = create_binary_tree([2, 1, 3])
    result2 = solution.invertTree(root2)
    expected2 = [2, 3, 1]
    actual2 = tree_to_list(result2)
    assert (
        actual2 == expected2
    ), f"Failed for [2,1,3], expected {expected2}, got {actual2}"

    # Test Case 3: Empty tree
    root3 = create_binary_tree([])
    result3 = solution.invertTree(root3)
    expected3 = []
    actual3 = tree_to_list(result3)
    assert actual3 == expected3, f"Failed for [], expected {expected3}, got {actual3}"

    # Test Case 4: Single node
    root4 = create_binary_tree([1])
    result4 = solution.invertTree(root4)
    expected4 = [1]
    actual4 = tree_to_list(result4)
    assert actual4 == expected4, f"Failed for [1], expected {expected4}, got {actual4}"

    # Test Case 5: Left skewed tree
    root5 = create_binary_tree([1, 2, None, 3, None, 4, None])
    result5 = solution.invertTree(root5)
    expected5 = [1, None, 2, None, 3, None, 4]
    actual5 = tree_to_list(result5)
    assert (
        actual5 == expected5
    ), f"Failed for left skewed tree, expected {expected5}, got {actual5}"

    # Test Case 6: Right skewed tree
    root6 = create_binary_tree([1, None, 2, None, 3, None, 4])
    result6 = solution.invertTree(root6)
    expected6 = [1, 2, None, 3, None, 4, None]
    actual6 = tree_to_list(result6)
    assert (
        actual6 == expected6
    ), f"Failed for right skewed tree, expected {expected6}, got {actual6}"

    # Test Case 7: Two nodes
    root7 = create_binary_tree([1, 2])
    result7 = solution.invertTree(root7)
    expected7 = [1, None, 2]
    actual7 = tree_to_list(result7)
    assert (
        actual7 == expected7
    ), f"Failed for [1,2], expected {expected7}, got {actual7}"

    # Test Case 8: Maximum constraint
    values = list(range(100))
    root8 = create_binary_tree(values)
    result8 = solution.invertTree(root8)
    actual8 = tree_to_list(result8)
    assert len(actual8) == 100, f"Failed for max constraint"

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
        values = list(range(size))
        root = create_binary_tree(values)

        # Test approach
        start_time = time.time()
        result = solution.invertTree(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has correct length
        actual = tree_to_list(result)
        assert len(actual) == size, f"Result length verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tInverted")

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
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.invertTree(root)
    actual = tree_to_list(result)
    assert len(actual) == 100
    print(f"Maximum length (100 elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 50
    root = create_binary_tree(values)
    result = solution.invertTree(root)
    actual = tree_to_list(result)
    assert actual == [100] * 50
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-100] * 50
    root = create_binary_tree(values)
    result = solution.invertTree(root)
    actual = tree_to_list(result)
    assert actual == [-100] * 50
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Alternating values
    values = [i if i % 2 == 0 else -i for i in range(50)]
    root = create_binary_tree(values)
    result = solution.invertTree(root)
    actual = tree_to_list(result)
    assert len(actual) == 50
    print(f"Alternating values: ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.invertTree(root)
    actual = tree_to_list(result)
    assert len(actual) == 15
    print(f"Complete binary tree: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(10000))
    root = create_binary_tree(values)

    start_time = time.time()
    result = solution.invertTree(root)
    time1 = time.time() - start_time

    # Verify result
    actual = tree_to_list(result)
    assert len(actual) == 10000

    print(f"Large dataset (10k elements):")
    print(f"Time: {time1:.6f}s, Result: Inverted correctly")


if __name__ == "__main__":
    print("🧪 Testing Invert Binary Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the invertTree method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use recursive or iterative approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using recursive approach")
