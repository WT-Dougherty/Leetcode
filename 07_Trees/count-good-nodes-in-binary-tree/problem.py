"""
Count Good Nodes In Binary Tree - LeetCode Problem 1448

Given a binary tree root, a node X in the tree is named good if in the path from root
to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, mv: int = -(10**5)) -> int:
        if not root:
            return 0
        elif root.val >= mv:
            return (
                1
                + self.goodNodes(root.left, root.val)
                + self.goodNodes(root.right, root.val)
            )
        else:
            return self.goodNodes(root.left, mv) + self.goodNodes(root.right, mv)


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
    root1 = create_binary_tree([3, 1, 4, 3, None, 1, 5])
    result1 = solution.goodNodes(root1)
    assert result1 == 4, f"Failed for [3,1,4,3,null,1,5], expected 4, got {result1}"

    # Test Case 2: Simple case
    root2 = create_binary_tree([3, 3, None, 4, 2])
    result2 = solution.goodNodes(root2)
    assert result2 == 3, f"Failed for [3,3,null,4,2], expected 3, got {result2}"

    # Test Case 3: Single node
    root3 = create_binary_tree([1])
    result3 = solution.goodNodes(root3)
    assert result3 == 1, f"Failed for [1], expected 1, got {result3}"

    # Test Case 4: All increasing
    root4 = create_binary_tree([1, 2, 3, 4, 5])
    result4 = solution.goodNodes(root4)
    assert result4 == 5, f"Failed for all increasing, expected 5, got {result4}"

    # Test Case 5: All decreasing
    root5 = create_binary_tree([5, 4, 3, 2, 1])
    result5 = solution.goodNodes(root5)
    assert result5 == 1, f"Failed for all decreasing, expected 1, got {result5}"

    # Test Case 6: Mixed values
    root6 = create_binary_tree([2, 1, 3, 0, 2])
    result6 = solution.goodNodes(root6)
    assert result6 == 3, f"Failed for mixed values, expected 3, got {result6}"

    # Test Case 7: Negative values
    root7 = create_binary_tree([-1, -2, -3, -4, -5])
    result7 = solution.goodNodes(root7)
    assert result7 == 1, f"Failed for negative values, expected 1, got {result7}"

    # Test Case 8: Zero values
    root8 = create_binary_tree([0, 0, 0, 0, 0])
    result8 = solution.goodNodes(root8)
    assert result8 == 5, f"Failed for zero values, expected 5, got {result8}"

    # Test Case 9: Complex case
    root9 = create_binary_tree([5, 1, 4, 3, None, 1, 5])
    result9 = solution.goodNodes(root9)
    assert result9 == 2, f"Failed for complex case, expected 2, got {result9}"

    # Test Case 10: Maximum constraint
    values = list(range(1, 100001))
    root10 = create_binary_tree(values)
    result10 = solution.goodNodes(root10)
    assert result10 == 100000, f"Failed for max constraint"

    # Test Case 11: Another LeetCode Case
    root11 = create_binary_tree([9, None, 3, 6])
    result11 = solution.goodNodes(root11)
    assert result11 == 1, f"Failed for LeetCode case, expected 1, got {result11}"

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
        result = solution.goodNodes(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result == size, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tGood nodes: {result}")

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
    values = list(range(1, 100001))
    root = create_binary_tree(values)
    result = solution.goodNodes(root)
    assert result == 100000
    print(f"Maximum length (100k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [10000] * 1000
    root = create_binary_tree(values)
    result = solution.goodNodes(root)
    assert result == 1000
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Alternating values
    values = [i if i % 2 == 0 else -i for i in range(100)]
    root = create_binary_tree(values)
    result = solution.goodNodes(root)
    assert result >= 1
    print(f"Alternating values: ✅")

    # Edge Case 4: Single path tree
    values = list(range(100))
    root = create_binary_tree(values)
    result = solution.goodNodes(root)
    assert result == 100
    print(f"Single path tree (all good): ✅")

    print("✅ All edge case tests passed!")


if __name__ == "__main__":
    print("🧪 Testing Count Good Nodes In Binary Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the goodNodes method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use DFS with max value tracking")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using DFS with max value tracking")
