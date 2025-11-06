"""
Balanced Binary Tree - LeetCode Problem 110

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(root: Optional[TreeNode], depth: int = 0) -> int:
            if not root:
                return depth
            l, r = maxDepth(root.left, depth + 1), maxDepth(root.right, depth + 1)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r)

        return maxDepth(root) != -1


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

    # Test Case 1: Balanced tree
    root1 = create_binary_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.isBalanced(root1)
    assert (
        result1 == True
    ), f"Failed for [3,9,20,null,null,15,7], expected True, got {result1}"

    # Test Case 2: Unbalanced tree
    root2 = create_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = solution.isBalanced(root2)
    assert (
        result2 == False
    ), f"Failed for [1,2,2,3,3,null,null,4,4], expected False, got {result2}"

    # Test Case 3: Empty tree
    root3 = create_binary_tree([])
    result3 = solution.isBalanced(root3)
    assert result3 == True, f"Failed for [], expected True, got {result3}"

    # Test Case 4: Single node
    root4 = create_binary_tree([1])
    result4 = solution.isBalanced(root4)
    assert result4 == True, f"Failed for [1], expected True, got {result4}"

    # Test Case 5: Left skewed tree
    root5 = create_binary_tree([1, 2, None, 3, None, 4, None])
    result5 = solution.isBalanced(root5)
    assert (
        result5 == False
    ), f"Failed for left skewed tree, expected False, got {result5}"

    # Test Case 6: Right skewed tree
    root6 = create_binary_tree([1, None, 2, None, 3, None, 4])
    result6 = solution.isBalanced(root6)
    assert (
        result6 == False
    ), f"Failed for right skewed tree, expected False, got {result6}"

    # Test Case 7: Two nodes
    root7 = create_binary_tree([1, 2])
    result7 = solution.isBalanced(root7)
    assert result7 == True, f"Failed for [1,2], expected True, got {result7}"

    # Test Case 8: Perfect binary tree
    root8 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    result8 = solution.isBalanced(root8)
    assert (
        result8 == True
    ), f"Failed for perfect binary tree, expected True, got {result8}"

    # Test Case 9: Slightly unbalanced
    root9 = create_binary_tree([1, 2, 3, 4, 5, None, None, 6, None])
    result9 = solution.isBalanced(root9)
    assert (
        result9 == False
    ), f"Failed for slightly unbalanced tree, expected False, got {result9}"

    # Test Case 10: Maximum constraint
    values = list(range(5000))
    root10 = create_binary_tree(values)
    result10 = solution.isBalanced(root10)
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
        # Generate test data
        values = list(range(size))
        root = create_binary_tree(values)

        # Test approach
        start_time = time.time()
        result = solution.isBalanced(root)
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
    values = list(range(5000))
    root = create_binary_tree(values)
    result = solution.isBalanced(root)
    assert isinstance(result, bool)
    print(f"Maximum length (5k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 1000
    root = create_binary_tree(values)
    result = solution.isBalanced(root)
    assert isinstance(result, bool)
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-100] * 1000
    root = create_binary_tree(values)
    result = solution.isBalanced(root)
    assert isinstance(result, bool)
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Single path tree
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.isBalanced(root)
    assert result == False  # Single path is unbalanced
    print(f"Single path tree (unbalanced): ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.isBalanced(root)
    assert result == True
    print(f"Complete binary tree (balanced): ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(5000))
    root = create_binary_tree(values)

    start_time = time.time()
    result = solution.isBalanced(root)
    time1 = time.time() - start_time

    assert isinstance(result, bool)

    print(f"Large dataset (5k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Balanced Binary Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isBalanced method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use DFS with height calculation")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using DFS with height calculation")
