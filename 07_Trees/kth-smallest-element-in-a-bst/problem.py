"""
Kth Smallest Element In a BST - LeetCode Problem 230

Given the root of a binary search tree, and an integer k, return the kth smallest
value (1-indexed) of all the values of the nodes in the tree.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
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


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    root1 = create_bst([3, 1, 4, None, 2])
    result1 = solution.kthSmallest(root1, 1)
    assert result1 == 1, f"Failed for k=1, expected 1, got {result1}"

    # Test Case 2: Second smallest
    root2 = create_bst([5, 3, 6, 2, 4, None, None, 1])
    result2 = solution.kthSmallest(root2, 3)
    assert result2 == 3, f"Failed for k=3, expected 3, got {result2}"

    # Test Case 3: Single node
    root3 = create_bst([1])
    result3 = solution.kthSmallest(root3, 1)
    assert result3 == 1, f"Failed for single node k=1, expected 1, got {result3}"

    # Test Case 4: Left skewed tree
    root4 = create_bst([5, 4, None, 3, None, 2, None, 1])
    result4 = solution.kthSmallest(root4, 2)
    assert result4 == 2, f"Failed for left skewed k=2, expected 2, got {result4}"

    # Test Case 5: Right skewed tree
    root5 = create_bst([1, None, 2, None, 3, None, 4, None, 5])
    result5 = solution.kthSmallest(root5, 3)
    assert result5 == 3, f"Failed for right skewed k=3, expected 3, got {result5}"

    # Test Case 6: Perfect BST
    root6 = create_bst([4, 2, 6, 1, 3, 5, 7])
    result6 = solution.kthSmallest(root6, 4)
    assert result6 == 4, f"Failed for perfect BST k=4, expected 4, got {result6}"

    # Test Case 7: Large k
    root7 = create_bst([5, 3, 6, 2, 4, None, None, 1])
    result7 = solution.kthSmallest(root7, 6)
    assert result7 == 6, f"Failed for k=6, expected 6, got {result7}"

    # Test Case 8: Negative values
    root8 = create_bst([0, -1, 1])
    result8 = solution.kthSmallest(root8, 2)
    assert result8 == 0, f"Failed for negative values k=2, expected 0, got {result8}"

    # Test Case 9: Duplicate values (not possible in BST, but test structure)
    root9 = create_bst([2, 1, 3])
    result9 = solution.kthSmallest(root9, 2)
    assert result9 == 2, f"Failed for k=2, expected 2, got {result9}"

    # Test Case 10: Maximum constraint
    values = list(range(1, 10001))
    root10 = create_bst(values)
    result10 = solution.kthSmallest(root10, 5000)
    assert result10 == 5000, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(h + k)"""
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
        k = size // 2  # Test middle element

        # Test approach
        start_time = time.time()
        result = solution.kthSmallest(root, k)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result == k, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\tkth: {result}")

    # For O(h + k) complexity, time should grow with height and k
    # Since k is proportional to size, this should be approximately O(log n + n) = O(n)
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(h + k) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(h + k): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(h + k)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(h + k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(h + k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    values = list(range(1, 10001))
    root = create_bst(values)
    result = solution.kthSmallest(root, 1)
    assert result == 1
    print(f"Maximum length (10k elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = list(range(1, 1001))
    root = create_bst(values)
    result = solution.kthSmallest(root, 1000)
    assert result == 1000
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = list(range(1, 1001))
    root = create_bst(values)
    result = solution.kthSmallest(root, 1)
    assert result == 1
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: k = 1
    values = list(range(1, 1001))
    root = create_bst(values)
    result = solution.kthSmallest(root, 1)
    assert result == 1
    print(f"k = 1: ✅")

    # Edge Case 5: k = n
    values = list(range(1, 1001))
    root = create_bst(values)
    result = solution.kthSmallest(root, 1000)
    assert result == 1000
    print(f"k = n: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(1, 10001))
    root = create_bst(values)

    start_time = time.time()
    result = solution.kthSmallest(root, 5000)
    time1 = time.time() - start_time

    assert result == 5000

    print(f"Large dataset (10k elements, k=5000):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Kth Smallest Element In a BST Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the kthSmallest method")
        print("- Aim for O(h + k) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use inorder traversal or iterative approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(h + k)")
        print("- Consider using inorder traversal or iterative approach")
