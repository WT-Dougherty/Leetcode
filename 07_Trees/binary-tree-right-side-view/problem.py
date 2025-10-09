"""
Binary Tree Right Side View - LeetCode Problem 199

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""

import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
    root1 = create_binary_tree([1, 2, 3, None, 5, None, 4])
    result1 = solution.rightSideView(root1)
    expected1 = [1, 3, 4]
    assert (
        result1 == expected1
    ), f"Failed for [1,2,3,null,5,null,4], expected {expected1}, got {result1}"

    # Test Case 2: Simple case
    root2 = create_binary_tree([1, None, 3])
    result2 = solution.rightSideView(root2)
    expected2 = [1, 3]
    assert (
        result2 == expected2
    ), f"Failed for [1,null,3], expected {expected2}, got {result2}"

    # Test Case 3: Empty tree
    root3 = create_binary_tree([])
    result3 = solution.rightSideView(root3)
    expected3 = []
    assert result3 == expected3, f"Failed for [], expected {expected3}, got {result3}"

    # Test Case 4: Single node
    root4 = create_binary_tree([1])
    result4 = solution.rightSideView(root4)
    expected4 = [1]
    assert result4 == expected4, f"Failed for [1], expected {expected4}, got {result4}"

    # Test Case 5: Left skewed tree
    root5 = create_binary_tree([1, 2, None, 3, None, 4, None])
    result5 = solution.rightSideView(root5)
    expected5 = [1, 2, 3, 4]
    assert (
        result5 == expected5
    ), f"Failed for left skewed tree, expected {expected5}, got {result5}"

    # Test Case 6: Right skewed tree
    root6 = create_binary_tree([1, None, 2, None, 3, None, 4])
    result6 = solution.rightSideView(root6)
    expected6 = [1, 2, 3, 4]
    assert (
        result6 == expected6
    ), f"Failed for right skewed tree, expected {expected6}, got {result6}"

    # Test Case 7: Perfect binary tree
    root7 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    result7 = solution.rightSideView(root7)
    expected7 = [1, 3, 7]
    assert (
        result7 == expected7
    ), f"Failed for perfect binary tree, expected {expected7}, got {result7}"

    # Test Case 8: Two levels
    root8 = create_binary_tree([1, 2, 3])
    result8 = solution.rightSideView(root8)
    expected8 = [1, 3]
    assert (
        result8 == expected8
    ), f"Failed for two levels, expected {expected8}, got {result8}"

    # Test Case 9: Deep tree
    values = [i for i in range(1, 16)]  # 15 nodes
    root9 = create_binary_tree(values)
    result9 = solution.rightSideView(root9)
    assert (
        len(result9) == 4
    ), f"Failed for deep tree, expected 4 levels, got {len(result9)}"

    # Test Case 10: Maximum constraint
    values = list(range(100))
    root10 = create_binary_tree(values)
    result10 = solution.rightSideView(root10)
    assert len(result10) > 0, f"Failed for max constraint"

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
        result = solution.rightSideView(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result has reasonable length
        assert len(result) > 0, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tLevels: {len(result)}")

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
    result = solution.rightSideView(root)
    assert len(result) == 100  # Single path
    print(f"Maximum length (100 elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 100
    root = create_binary_tree(values)
    result = solution.rightSideView(root)
    assert len(result) == 100  # Single path
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-100] * 100
    root = create_binary_tree(values)
    result = solution.rightSideView(root)
    assert len(result) == 100  # Single path
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Complete binary tree
    values = list(range(15))  # 2^4 - 1 = 15 nodes
    root = create_binary_tree(values)
    result = solution.rightSideView(root)
    assert len(result) == 4  # 4 levels
    print(f"Complete binary tree (4 levels): ✅")

    # Edge Case 5: Single path tree
    values = list(range(50))
    root = create_binary_tree(values)
    result = solution.rightSideView(root)
    assert len(result) == 50  # 50 levels
    print(f"Single path tree (50 levels): ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(1000))
    root = create_binary_tree(values)

    start_time = time.time()
    result = solution.rightSideView(root)
    time1 = time.time() - start_time

    # Verify result
    assert len(result) > 0

    print(f"Large dataset (1k elements):")
    print(f"Time: {time1:.6f}s, Result: {len(result)} levels")


if __name__ == "__main__":
    print("🧪 Testing Binary Tree Right Side View Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the rightSideView method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use BFS with level tracking")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using BFS with level tracking")
