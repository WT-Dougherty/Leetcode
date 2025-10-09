"""
Subtree of Another Tree - LeetCode Problem 572

Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of
this node's descendants. The tree tree could also be considered as a subtree of itself.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
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
    root1 = create_binary_tree([3, 4, 5, 1, 2])
    subRoot1 = create_binary_tree([4, 1, 2])
    result1 = solution.isSubtree(root1, subRoot1)
    assert result1 == True, f"Failed for basic case, expected True, got {result1}"

    # Test Case 2: Not a subtree
    root2 = create_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot2 = create_binary_tree([4, 1, 2])
    result2 = solution.isSubtree(root2, subRoot2)
    assert (
        result2 == False
    ), f"Failed for not subtree case, expected False, got {result2}"

    # Test Case 3: Empty subRoot
    root3 = create_binary_tree([1])
    subRoot3 = create_binary_tree([])
    result3 = solution.isSubtree(root3, subRoot3)
    assert result3 == True, f"Failed for empty subRoot, expected True, got {result3}"

    # Test Case 4: Empty root
    root4 = create_binary_tree([])
    subRoot4 = create_binary_tree([1])
    result4 = solution.isSubtree(root4, subRoot4)
    assert result4 == False, f"Failed for empty root, expected False, got {result4}"

    # Test Case 5: Both empty
    root5 = create_binary_tree([])
    subRoot5 = create_binary_tree([])
    result5 = solution.isSubtree(root5, subRoot5)
    assert result5 == True, f"Failed for both empty, expected True, got {result5}"

    # Test Case 6: Single nodes
    root6 = create_binary_tree([1])
    subRoot6 = create_binary_tree([1])
    result6 = solution.isSubtree(root6, subRoot6)
    assert result6 == True, f"Failed for single nodes, expected True, got {result6}"

    # Test Case 7: Different single nodes
    root7 = create_binary_tree([1])
    subRoot7 = create_binary_tree([2])
    result7 = solution.isSubtree(root7, subRoot7)
    assert (
        result7 == False
    ), f"Failed for different single nodes, expected False, got {result7}"

    # Test Case 8: Root is subtree of itself
    root8 = create_binary_tree([1, 2, 3])
    subRoot8 = create_binary_tree([1, 2, 3])
    result8 = solution.isSubtree(root8, subRoot8)
    assert (
        result8 == True
    ), f"Failed for root is subtree of itself, expected True, got {result8}"

    # Test Case 9: Complex case
    root9 = create_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    subRoot9 = create_binary_tree([2, 4, 5])
    result9 = solution.isSubtree(root9, subRoot9)
    assert result9 == True, f"Failed for complex case, expected True, got {result9}"

    # Test Case 10: Maximum constraint
    root_values = list(range(2000))
    subRoot_values = list(range(100, 200))
    root10 = create_binary_tree(root_values)
    subRoot10 = create_binary_tree(subRoot_values)
    result10 = solution.isSubtree(root10, subRoot10)
    assert result10 == False, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(m * n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [(50, 10), (100, 20), (200, 40)]
    times = []

    print("\nTime Complexity Analysis:")
    print("Root\tSub\tTime\t\tResult")
    print("-" * 50)

    for root_size, sub_size in test_sizes:
        # Generate test data
        root_values = list(range(root_size))
        subRoot_values = list(range(sub_size))
        root = create_binary_tree(root_values)
        subRoot = create_binary_tree(subRoot_values)

        # Test approach
        start_time = time.time()
        result = solution.isSubtree(root, subRoot)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result is boolean
        assert isinstance(
            result, bool
        ), f"Result verification failed for size ({root_size}, {sub_size})"

        print(f"{root_size}\t{sub_size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(m * n) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(m * n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            m1, n1 = test_sizes[i - 1]
            m2, n2 = test_sizes[i]
            expected_ratio = (m2 * n2) / (m1 * n1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(m * n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(m * n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m * n * log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(m * n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(m * n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint root length
    root_values = list(range(2000))
    subRoot_values = list(range(100))
    root = create_binary_tree(root_values)
    subRoot = create_binary_tree(subRoot_values)
    result = solution.isSubtree(root, subRoot)
    assert isinstance(result, bool)
    print(f"Maximum root length (2k elements): ✅")

    # Edge Case 2: Maximum constraint subRoot length
    root_values = list(range(1000))
    subRoot_values = list(range(1000))
    root = create_binary_tree(root_values)
    subRoot = create_binary_tree(subRoot_values)
    result = solution.isSubtree(root, subRoot)
    assert isinstance(result, bool)
    print(f"Maximum subRoot length (1k elements): ✅")

    # Edge Case 3: Maximum constraint values
    root_values = [10000] * 100
    subRoot_values = [10000] * 50
    root = create_binary_tree(root_values)
    subRoot = create_binary_tree(subRoot_values)
    result = solution.isSubtree(root, subRoot)
    assert isinstance(result, bool)
    print(f"Maximum constraint values: ✅")

    # Edge Case 4: Minimum constraint values
    root_values = [-10000] * 100
    subRoot_values = [-10000] * 50
    root = create_binary_tree(root_values)
    subRoot = create_binary_tree(subRoot_values)
    result = solution.isSubtree(root, subRoot)
    assert isinstance(result, bool)
    print(f"Minimum constraint values: ✅")

    # Edge Case 5: Identical trees
    values = list(range(100))
    root = create_binary_tree(values)
    subRoot = create_binary_tree(values)
    result = solution.isSubtree(root, subRoot)
    assert result == True
    print(f"Identical trees: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    root_values = list(range(1000))
    subRoot_values = list(range(100))
    root = create_binary_tree(root_values)
    subRoot = create_binary_tree(subRoot_values)

    start_time = time.time()
    result = solution.isSubtree(root, subRoot)
    time1 = time.time() - start_time

    assert isinstance(result, bool)

    print(f"Large dataset (1k root, 100 subRoot):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Subtree of Another Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isSubtree method")
        print("- Aim for O(m * n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use helper function to check if trees are identical")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(m * n)")
        print("- Consider using helper function to check if trees are identical")
