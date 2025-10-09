"""
Lowest Common Ancestor of a Binary Search Tree - LeetCode Problem 235

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow
a node to be a descendant of itself)."
"""

import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pass


def create_bst(values):
    """Helper function to create a BST from a list of values"""
    if not values:
        return None

    root = TreeNode(values[0])
    for val in values[1:]:
        insert_into_bst(root, val)

    return root


def insert_into_bst(root, val):
    """Helper function to insert a value into BST"""
    if val < root.val:
        if root.left is None:
            root.left = TreeNode(val)
        else:
            insert_into_bst(root.left, val)
    else:
        if root.right is None:
            root.right = TreeNode(val)
        else:
            insert_into_bst(root.right, val)


def find_node(root, val):
    """Helper function to find a node with given value in BST"""
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return find_node(root.left, val)
    else:
        return find_node(root.right, val)


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    root1 = create_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1 = find_node(root1, 2)
    q1 = find_node(root1, 8)
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    assert result1.val == 6, f"Failed for basic case, expected 6, got {result1.val}"

    # Test Case 2: LCA is one of the nodes
    root2 = create_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p2 = find_node(root2, 2)
    q2 = find_node(root2, 4)
    result2 = solution.lowestCommonAncestor(root2, p2, q2)
    assert (
        result2.val == 2
    ), f"Failed for LCA is one node, expected 2, got {result2.val}"

    # Test Case 3: Simple case
    root3 = create_bst([2, 1])
    p3 = find_node(root3, 2)
    q3 = find_node(root3, 1)
    result3 = solution.lowestCommonAncestor(root3, p3, q3)
    assert result3.val == 2, f"Failed for simple case, expected 2, got {result3.val}"

    # Test Case 4: Single node
    root4 = create_bst([1])
    p4 = find_node(root4, 1)
    q4 = find_node(root4, 1)
    result4 = solution.lowestCommonAncestor(root4, p4, q4)
    assert result4.val == 1, f"Failed for single node, expected 1, got {result4.val}"

    # Test Case 5: Left subtree
    root5 = create_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p5 = find_node(root5, 0)
    q5 = find_node(root5, 5)
    result5 = solution.lowestCommonAncestor(root5, p5, q5)
    assert result5.val == 2, f"Failed for left subtree, expected 2, got {result5.val}"

    # Test Case 6: Right subtree
    root6 = create_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p6 = find_node(root6, 7)
    q6 = find_node(root6, 9)
    result6 = solution.lowestCommonAncestor(root6, p6, q6)
    assert result6.val == 8, f"Failed for right subtree, expected 8, got {result6.val}"

    # Test Case 7: Deep tree
    root7 = create_bst([10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, 16, 20])
    p7 = find_node(root7, 1)
    q7 = find_node(root7, 8)
    result7 = solution.lowestCommonAncestor(root7, p7, q7)
    assert result7.val == 5, f"Failed for deep tree, expected 5, got {result7.val}"

    # Test Case 8: Maximum constraint
    values = list(range(1, 100001))
    root8 = create_bst(values)
    p8 = find_node(root8, 1)
    q8 = find_node(root8, 100000)
    result8 = solution.lowestCommonAncestor(root8, p8, q8)
    assert result8.val == 50000, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(h)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        values = list(range(1, size + 1))
        root = create_bst(values)
        p = find_node(root, 1)
        q = find_node(root, size)

        # Test approach
        start_time = time.time()
        result = solution.lowestCommonAncestor(root, p, q)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result is not None, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tLCA: {result.val}")

    # For O(h) complexity, time should grow logarithmically with size
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(h) complexity (logarithmic growth)
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = (test_sizes[i].bit_length() - 1) / (
                test_sizes[i - 1].bit_length() - 1
            )
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(h): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(h)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(h), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(h)")
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
    root = create_bst(values)
    p = find_node(root, 1)
    q = find_node(root, 100000)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result is not None
    print(f"Maximum length (100k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [1000000000] * 1000
    root = create_bst(values)
    p = find_node(root, 1000000000)
    q = find_node(root, 1000000000)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 1000000000
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-1000000000] * 1000
    root = create_bst(values)
    p = find_node(root, -1000000000)
    q = find_node(root, -1000000000)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == -1000000000
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Same nodes
    values = list(range(1, 1001))
    root = create_bst(values)
    p = find_node(root, 500)
    q = find_node(root, 500)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 500
    print(f"Same nodes: ✅")

    # Edge Case 5: Root and leaf
    values = list(range(1, 1001))
    root = create_bst(values)
    p = find_node(root, 1)
    q = find_node(root, 1000)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 500
    print(f"Root and leaf: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(1, 100001))
    root = create_bst(values)
    p = find_node(root, 1)
    q = find_node(root, 100000)

    start_time = time.time()
    result = solution.lowestCommonAncestor(root, p, q)
    time1 = time.time() - start_time

    assert result is not None

    print(f"Large dataset (100k elements):")
    print(f"Time: {time1:.6f}s, Result: LCA {result.val}")


if __name__ == "__main__":
    print("🧪 Testing Lowest Common Ancestor of a Binary Search Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the lowestCommonAncestor method")
        print("- Aim for O(h) time complexity where h is the height")
        print("- Handle all edge cases correctly")
        print("- Use BST property: LCA is first node where p and q diverge")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(h)")
        print("- Consider using BST property to find divergence point")
