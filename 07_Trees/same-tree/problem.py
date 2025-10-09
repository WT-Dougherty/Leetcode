"""
Same Tree - LeetCode Problem 100

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

import time
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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

    # Test Case 1: Same trees
    p1 = create_binary_tree([1, 2, 3])
    q1 = create_binary_tree([1, 2, 3])
    result1 = solution.isSameTree(p1, q1)
    assert result1 == True, f"Failed for same trees, expected True, got {result1}"

    # Test Case 2: Different structure
    p2 = create_binary_tree([1, 2])
    q2 = create_binary_tree([1, None, 2])
    result2 = solution.isSameTree(p2, q2)
    assert (
        result2 == False
    ), f"Failed for different structure, expected False, got {result2}"

    # Test Case 3: Different values
    p3 = create_binary_tree([1, 2, 1])
    q3 = create_binary_tree([1, 1, 2])
    result3 = solution.isSameTree(p3, q3)
    assert (
        result3 == False
    ), f"Failed for different values, expected False, got {result3}"

    # Test Case 4: Both empty
    p4 = create_binary_tree([])
    q4 = create_binary_tree([])
    result4 = solution.isSameTree(p4, q4)
    assert result4 == True, f"Failed for both empty, expected True, got {result4}"

    # Test Case 5: One empty
    p5 = create_binary_tree([1])
    q5 = create_binary_tree([])
    result5 = solution.isSameTree(p5, q5)
    assert result5 == False, f"Failed for one empty, expected False, got {result5}"

    # Test Case 6: Single nodes same
    p6 = create_binary_tree([1])
    q6 = create_binary_tree([1])
    result6 = solution.isSameTree(p6, q6)
    assert (
        result6 == True
    ), f"Failed for single nodes same, expected True, got {result6}"

    # Test Case 7: Single nodes different
    p7 = create_binary_tree([1])
    q7 = create_binary_tree([2])
    result7 = solution.isSameTree(p7, q7)
    assert (
        result7 == False
    ), f"Failed for single nodes different, expected False, got {result7}"

    # Test Case 8: Complex same trees
    p8 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    q8 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    result8 = solution.isSameTree(p8, q8)
    assert (
        result8 == True
    ), f"Failed for complex same trees, expected True, got {result8}"

    # Test Case 9: Complex different trees
    p9 = create_binary_tree([1, 2, 3, 4, 5, 6, 7])
    q9 = create_binary_tree([1, 2, 3, 4, 5, 6, 8])
    result9 = solution.isSameTree(p9, q9)
    assert (
        result9 == False
    ), f"Failed for complex different trees, expected False, got {result9}"

    # Test Case 10: Maximum constraint
    values = list(range(100))
    p10 = create_binary_tree(values)
    q10 = create_binary_tree(values)
    result10 = solution.isSameTree(p10, q10)
    assert result10 == True, f"Failed for max constraint"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(min(m, n))"""
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
        p = create_binary_tree(values)
        q = create_binary_tree(values)

        # Test approach
        start_time = time.time()
        result = solution.isSameTree(p, q)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        # Verify result
        assert result == True, f"Result verification failed for size {size}"

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(min(m, n)) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(min(m, n)) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(min(m, n)): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(min(m, n))")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(m * n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(min(m, n)), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(min(m, n))")
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
    p = create_binary_tree(values)
    q = create_binary_tree(values)
    result = solution.isSameTree(p, q)
    assert result == True
    print(f"Maximum length (100 elements): ✅")

    # Edge Case 2: Maximum constraint values
    values = [100] * 50
    p = create_binary_tree(values)
    q = create_binary_tree(values)
    result = solution.isSameTree(p, q)
    assert result == True
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Minimum constraint values
    values = [-100] * 50
    p = create_binary_tree(values)
    q = create_binary_tree(values)
    result = solution.isSameTree(p, q)
    assert result == True
    print(f"Minimum constraint values: ✅")

    # Edge Case 4: Different sizes
    p = create_binary_tree([1, 2, 3])
    q = create_binary_tree([1, 2])
    result = solution.isSameTree(p, q)
    assert result == False
    print(f"Different sizes: ✅")

    # Edge Case 5: One null, one not
    p = create_binary_tree([1])
    q = create_binary_tree([])
    result = solution.isSameTree(p, q)
    assert result == False
    print(f"One null, one not: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    values = list(range(1000))
    p = create_binary_tree(values)
    q = create_binary_tree(values)

    start_time = time.time()
    result = solution.isSameTree(p, q)
    time1 = time.time() - start_time

    assert result == True

    print(f"Large dataset (1k elements each):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Same Tree Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isSameTree method")
        print("- Aim for O(min(m, n)) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use recursive approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(min(m, n))")
        print("- Consider using recursive approach")
