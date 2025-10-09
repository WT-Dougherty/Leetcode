"""
Binary Tree Maximum Path Sum - LeetCode Problem 124

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
sequence has an edge connecting them. A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
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

    # Test Case 1: Basic case
    root1 = create_binary_tree([1, 2, 3])
    result1 = solution.maxPathSum(root1)
    assert result1 == 6, f"Failed for [1,2,3], expected 6, got {result1}"

    # Test Case 2: Negative values
    root2 = create_binary_tree([-10, 9, 20, None, None, 15, 7])
    result2 = solution.maxPathSum(root2)
    assert (
        result2 == 42
    ), f"Failed for [-10,9,20,null,null,15,7], expected 42, got {result2}"

    # Test Case 3: Single node
    root3 = create_binary_tree([1])
    result3 = solution.maxPathSum(root3)
    assert result3 == 1, f"Failed for [1], expected 1, got {result3}"

    # Test Case 4: Negative single node
    root4 = create_binary_tree([-1])
    result4 = solution.maxPathSum(root4)
    assert result4 == -1, f"Failed for [-1], expected -1, got {result4}"

    # Test Case 5: All negative
    root5 = create_binary_tree([-1, -2, -3])
    result5 = solution.maxPathSum(root5)
    assert result5 == -1, f"Failed for [-1,-2,-3], expected -1, got {result5}"

    # Test Case 6: Left skewed
    root6 = create_binary_tree([1, 2, None, 3, None, 4, None])
    result6 = solution.maxPathSum(root6)
    assert result6 == 10, f"Failed for left skewed, expected 10, got {result6}"

    # Test Case 7: Right skewed
    root7 = create_binary_tree([1, None, 2, None, 3, None, 4])
    result7 = solution.maxPathSum(root7)
    assert result7 == 10, f"Failed for right skewed, expected 10, got {result7}"

    # Test Case 8: Mixed positive and negative
    root8 = create_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    result8 = solution.maxPathSum(root8)
    assert result8 == 48, f"Failed for mixed values, expected 48, got {result8}"

    # Test Case 9: Zero values
    root9 = create_binary_tree([0, 1, 1])
    result9 = solution.maxPathSum(root9)
    assert result9 == 2, f"Failed for zero values, expected 2, got {result9}"

    # Test Case 10: Maximum constraint
    values = [1000] * 3000
    root10 = create_binary_tree(values)
    result10 = solution.maxPathSum(root10)
    assert result10 > 0, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 3000]
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
        result = solution.maxPathSum(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is reasonable
        assert isinstance(result, int), f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tMax sum: {result}")

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
    values = list(range(3000))
    root = create_binary_tree(values)
    result = solution.maxPathSum(root)
    assert isinstance(result, int)
    print(f"Maximum length (3k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [1000] * 1000
    root = create_binary_tree(values)
    result = solution.maxPathSum(root)
    assert result > 0
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-1000] * 1000
    root = create_binary_tree(values)
    result = solution.maxPathSum(root)
    assert result == -1000  # Single node path
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Single path tree
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.maxPathSum(root)
    assert result > 0
    print(f"Single path tree: ✅")

    # Edge Case 5: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.maxPathSum(root)
    assert result > 0
    print(f"Complete binary tree: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(3000))
    root = create_binary_tree(values)

    start_time = time.time()
    result = solution.maxPathSum(root)
    time1 = time.time() - start_time

    assert isinstance(result, int)

    print(f"Large dataset (3k elements):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Binary Tree Maximum Path Sum Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the maxPathSum method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use DFS with path sum calculation")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using DFS with path sum calculation")
