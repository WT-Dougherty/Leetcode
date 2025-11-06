"""
Diameter of Binary Tree - LeetCode Problem 543

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def findDiameter(root: Optional[TreeNode], depth: int = 0) -> int:
            nonlocal diameter
            if not root:
                return -1
            l, r = 1 + findDiameter(root.left), 1 + findDiameter(root.right)
            if l + r > diameter:
                diameter = l + r
            return max(l, r)

        findDiameter(root)
        return diameter


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

    # Test Case 1: Basic case
    root1 = create_binary_tree([1, 2, 3, 4, 5])
    result1 = solution.diameterOfBinaryTree(root1)
    assert result1 == 3, f"Failed for [1,2,3,4,5], expected 3, got {result1}"

    # Test Case 2: Simple case
    root2 = create_binary_tree([1, 2])
    result2 = solution.diameterOfBinaryTree(root2)
    assert result2 == 1, f"Failed for [1,2], expected 1, got {result2}"

    # Test Case 3: Single node
    root3 = create_binary_tree([1])
    result3 = solution.diameterOfBinaryTree(root3)
    assert result3 == 0, f"Failed for [1], expected 0, got {result3}"

    # Test Case 4: Empty tree
    root4 = create_binary_tree([])
    result4 = solution.diameterOfBinaryTree(root4)
    assert result4 == 0, f"Failed for [], expected 0, got {result4}"

    # Test Case 5: Left skewed tree
    root5 = create_binary_tree([1, 2, None, 3, None, 4, None])
    result5 = solution.diameterOfBinaryTree(root5)
    assert result5 == 3, f"Failed for left skewed tree, expected 3, got {result5}"

    # Test Case 6: Right skewed tree
    root6 = create_binary_tree([1, None, 2, None, 3, None, 4])
    result6 = solution.diameterOfBinaryTree(root6)
    assert result6 == 3, f"Failed for right skewed tree, expected 3, got {result6}"

    # Test Case 7: Balanced tree
    root7 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    result7 = solution.diameterOfBinaryTree(root7)
    assert result7 == 4, f"Failed for balanced tree, expected 4, got {result7}"

    # Test Case 8: Deep tree
    values = [i for i in range(1, 16)]  # 15 nodes
    root8 = create_binary_tree(values)
    result8 = solution.diameterOfBinaryTree(root8)
    assert result8 >= 6, f"Failed for deep tree, expected >= 6, got {result8}"

    # Test Case 9: Maximum constraint
    values = list(range(10000))
    root9 = create_binary_tree(values)
    result9 = solution.diameterOfBinaryTree(root9)
    assert result9 >= 0, f"Failed for max constraint"

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
        result = solution.diameterOfBinaryTree(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is reasonable
        assert result >= 0, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tDiameter: {result}")

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
    result = solution.diameterOfBinaryTree(root)
    assert result >= 0
    print(f"Maximum length (10k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 1000
    root = create_binary_tree(values)
    result = solution.diameterOfBinaryTree(root)
    assert result >= 0
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-100] * 1000
    root = create_binary_tree(values)
    result = solution.diameterOfBinaryTree(root)
    assert result >= 0
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Large Tree
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.diameterOfBinaryTree(root)
    assert result == 12  # 100 nodes, 99 edges
    print(f"Large Tree: ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.diameterOfBinaryTree(root)
    assert result >= 4
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
    result = solution.diameterOfBinaryTree(root)
    time1 = time.time() - start_time

    assert result >= 0

    print(f"Large dataset (10k elements):")
    print(f"Time: {time1:.6f}s, Result: Diameter {result}")


if __name__ == "__main__":
    print("🧪 Testing Diameter of Binary Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the diameterOfBinaryTree method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use DFS with height calculation")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using DFS with height calculation")
