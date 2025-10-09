"""
Validate Binary Search Tree - LeetCode Problem 98

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Valid BST
    root1 = create_binary_tree([2, 1, 3])
    result1 = solution.isValidBST(root1)
    assert result1 == True, f"Failed for [2,1,3], expected True, got {result1}"

    # Test Case 2: Invalid BST
    root2 = create_binary_tree([5, 1, 4, None, None, 3, 6])
    result2 = solution.isValidBST(root2)
    assert (
        result2 == False
    ), f"Failed for [5,1,4,null,null,3,6], expected False, got {result2}"

    # Test Case 3: Invalid BST with equal values
    root3 = create_binary_tree([5, 4, 6, None, None, 3, 7])
    result3 = solution.isValidBST(root3)
    assert (
        result3 == False
    ), f"Failed for [5,4,6,null,null,3,7], expected False, got {result3}"

    # Test Case 4: Single node
    root4 = create_binary_tree([1])
    result4 = solution.isValidBST(root4)
    assert result4 == True, f"Failed for [1], expected True, got {result4}"

    # Test Case 5: Empty tree
    root5 = create_binary_tree([])
    result5 = solution.isValidBST(root5)
    assert result5 == True, f"Failed for [], expected True, got {result5}"

    # Test Case 6: Left skewed valid BST
    root6 = create_binary_tree([3, 2, None, 1, None])
    result6 = solution.isValidBST(root6)
    assert (
        result6 == True
    ), f"Failed for left skewed valid BST, expected True, got {result6}"

    # Test Case 7: Right skewed valid BST
    root7 = create_binary_tree([1, None, 2, None, 3])
    result7 = solution.isValidBST(root7)
    assert (
        result7 == True
    ), f"Failed for right skewed valid BST, expected True, got {result7}"

    # Test Case 8: Invalid BST with wrong left subtree
    root8 = create_binary_tree([10, 5, 15, None, None, 6, 20])
    result8 = solution.isValidBST(root8)
    assert result8 == False, f"Failed for invalid BST, expected False, got {result8}"

    # Test Case 9: Valid BST with negative values
    root9 = create_binary_tree([0, -1, None])
    result9 = solution.isValidBST(root9)
    assert (
        result9 == True
    ), f"Failed for valid BST with negative values, expected True, got {result9}"

    # Test Case 10: Maximum constraint
    values = list(range(10000))
    root10 = create_binary_tree(values)
    result10 = solution.isValidBST(root10)
    assert result10 == False, f"Failed for max constraint"

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
        # Generate test data - create a valid BST
        values = list(range(size))
        root = create_binary_tree(values)

        # Test approach
        start_time = time.time()
        result = solution.isValidBST(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is boolean
        assert isinstance(result, bool), f"Result verification failed for size {size}"

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
    values = list(range(10000))
    root = create_binary_tree(values)
    result = solution.isValidBST(root)
    assert isinstance(result, bool)
    print(f"Maximum length (10k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [2147483647] * 1000
    root = create_binary_tree(values)
    result = solution.isValidBST(root)
    assert isinstance(result, bool)
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-2147483648] * 1000
    root = create_binary_tree(values)
    result = solution.isValidBST(root)
    assert isinstance(result, bool)
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Single path tree
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.isValidBST(root)
    assert result == False  # Not a valid BST structure
    print(f"Single path tree: ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.isValidBST(root)
    assert isinstance(result, bool)
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
    result = solution.isValidBST(root)
    time1 = time.time() - start_time

    assert isinstance(result, bool)

    print(f"Large dataset (10k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Validate Binary Search Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isValidBST method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use DFS with min/max bounds")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using DFS with min/max bounds")
