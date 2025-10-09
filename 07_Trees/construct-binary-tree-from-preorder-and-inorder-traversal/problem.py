"""
Construct Binary Tree From Preorder And Inorder Traversal - LeetCode Problem 105

Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and
return the binary tree.
"""

import time
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


def tree_to_preorder(root):
    """Helper function to convert tree to preorder traversal"""
    if not root:
        return []
    return [root.val] + tree_to_preorder(root.left) + tree_to_preorder(root.right)


def tree_to_inorder(root):
    """Helper function to convert tree to inorder traversal"""
    if not root:
        return []
    return tree_to_inorder(root.left) + [root.val] + tree_to_inorder(root.right)


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    result1 = solution.buildTree(preorder1, inorder1)
    actual_pre1 = tree_to_preorder(result1)
    actual_in1 = tree_to_inorder(result1)
    assert (
        actual_pre1 == preorder1
    ), f"Failed preorder for basic case, expected {preorder1}, got {actual_pre1}"
    assert (
        actual_in1 == inorder1
    ), f"Failed inorder for basic case, expected {inorder1}, got {actual_in1}"

    # Test Case 2: Single node
    preorder2 = [-1]
    inorder2 = [-1]
    result2 = solution.buildTree(preorder2, inorder2)
    actual_pre2 = tree_to_preorder(result2)
    actual_in2 = tree_to_inorder(result2)
    assert (
        actual_pre2 == preorder2
    ), f"Failed preorder for single node, expected {preorder2}, got {actual_pre2}"
    assert (
        actual_in2 == inorder2
    ), f"Failed inorder for single node, expected {inorder2}, got {actual_in2}"

    # Test Case 3: Left skewed tree
    preorder3 = [1, 2, 3, 4]
    inorder3 = [4, 3, 2, 1]
    result3 = solution.buildTree(preorder3, inorder3)
    actual_pre3 = tree_to_preorder(result3)
    actual_in3 = tree_to_inorder(result3)
    assert (
        actual_pre3 == preorder3
    ), f"Failed preorder for left skewed, expected {preorder3}, got {actual_pre3}"
    assert (
        actual_in3 == inorder3
    ), f"Failed inorder for left skewed, expected {inorder3}, got {actual_in3}"

    # Test Case 4: Right skewed tree
    preorder4 = [1, 2, 3, 4]
    inorder4 = [1, 2, 3, 4]
    result4 = solution.buildTree(preorder4, inorder4)
    actual_pre4 = tree_to_preorder(result4)
    actual_in4 = tree_to_inorder(result4)
    assert (
        actual_pre4 == preorder4
    ), f"Failed preorder for right skewed, expected {preorder4}, got {actual_pre4}"
    assert (
        actual_in4 == inorder4
    ), f"Failed inorder for right skewed, expected {inorder4}, got {actual_in4}"

    # Test Case 5: Perfect binary tree
    preorder5 = [1, 2, 4, 5, 3, 6, 7]
    inorder5 = [4, 2, 5, 1, 6, 3, 7]
    result5 = solution.buildTree(preorder5, inorder5)
    actual_pre5 = tree_to_preorder(result5)
    actual_in5 = tree_to_inorder(result5)
    assert (
        actual_pre5 == preorder5
    ), f"Failed preorder for perfect tree, expected {preorder5}, got {actual_pre5}"
    assert (
        actual_in5 == inorder5
    ), f"Failed inorder for perfect tree, expected {inorder5}, got {actual_in5}"

    # Test Case 6: Two nodes
    preorder6 = [1, 2]
    inorder6 = [2, 1]
    result6 = solution.buildTree(preorder6, inorder6)
    actual_pre6 = tree_to_preorder(result6)
    actual_in6 = tree_to_inorder(result6)
    assert (
        actual_pre6 == preorder6
    ), f"Failed preorder for two nodes, expected {preorder6}, got {actual_pre6}"
    assert (
        actual_in6 == inorder6
    ), f"Failed inorder for two nodes, expected {inorder6}, got {actual_in6}"

    # Test Case 7: Negative values
    preorder7 = [0, -1, 1]
    inorder7 = [-1, 0, 1]
    result7 = solution.buildTree(preorder7, inorder7)
    actual_pre7 = tree_to_preorder(result7)
    actual_in7 = tree_to_inorder(result7)
    assert (
        actual_pre7 == preorder7
    ), f"Failed preorder for negative values, expected {preorder7}, got {actual_pre7}"
    assert (
        actual_in7 == inorder7
    ), f"Failed inorder for negative values, expected {inorder7}, got {actual_in7}"

    # Test Case 8: Large values
    preorder8 = [1000, 500, 1500]
    inorder8 = [500, 1000, 1500]
    result8 = solution.buildTree(preorder8, inorder8)
    actual_pre8 = tree_to_preorder(result8)
    actual_in8 = tree_to_inorder(result8)
    assert (
        actual_pre8 == preorder8
    ), f"Failed preorder for large values, expected {preorder8}, got {actual_pre8}"
    assert (
        actual_in8 == inorder8
    ), f"Failed inorder for large values, expected {inorder8}, got {actual_in8}"

    # Test Case 9: Maximum constraint
    preorder9 = list(range(3000))
    inorder9 = list(range(3000))
    result9 = solution.buildTree(preorder9, inorder9)
    actual_pre9 = tree_to_preorder(result9)
    actual_in9 = tree_to_inorder(result9)
    assert actual_pre9 == preorder9, f"Failed preorder for max constraint"
    assert actual_in9 == inorder9, f"Failed inorder for max constraint"

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
        preorder = list(range(size))
        inorder = list(range(size))

        # Test approach
        start_time = time.time()
        result = solution.buildTree(preorder, inorder)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        actual_pre = tree_to_preorder(result)
        actual_in = tree_to_inorder(result)
        assert actual_pre == preorder, f"Result verification failed for size {size}"
        assert actual_in == inorder, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tBuilt")

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
    preorder = list(range(3000))
    inorder = list(range(3000))
    result = solution.buildTree(preorder, inorder)
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == preorder
    assert actual_in == inorder
    print(f"Maximum length (3k elements): ✅")

    # Edge Case 2: Maximum constraint values
    preorder = [3000] * 1000
    inorder = [3000] * 1000
    result = solution.buildTree(preorder, inorder)
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == preorder
    assert actual_in == inorder
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    preorder = [-3000] * 1000
    inorder = [-3000] * 1000
    result = solution.buildTree(preorder, inorder)
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == preorder
    assert actual_in == inorder
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Single element
    preorder = [42]
    inorder = [42]
    result = solution.buildTree(preorder, inorder)
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == [42]
    assert actual_in == [42]
    print(f"Single element: ✅")

    # Edge Case 5: Two elements
    preorder = [1, 2]
    inorder = [2, 1]
    result = solution.buildTree(preorder, inorder)
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == [1, 2]
    assert actual_in == [2, 1]
    print(f"Two elements: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    preorder = list(range(3000))
    inorder = list(range(3000))

    start_time = time.time()
    result = solution.buildTree(preorder, inorder)
    time1 = time.time() - start_time

    # Verify result
    actual_pre = tree_to_preorder(result)
    actual_in = tree_to_inorder(result)
    assert actual_pre == preorder
    assert actual_in == inorder

    print(f"Large dataset (3k elements):")
    print(f"Time: {time1:.6f}s, Result: Built correctly")


if __name__ == "__main__":
    print(
        "🧪 Testing Construct Binary Tree From Preorder And Inorder Traversal Problem"
    )
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the buildTree method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use hash map for inorder indices")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash map for inorder indices")
