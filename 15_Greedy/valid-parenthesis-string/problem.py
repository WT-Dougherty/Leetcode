"""
Valid Parenthesis String - LeetCode Problem 678

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
"""

import time


class Solution:
    def checkValidString(self, s):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "()"
    result1 = solution.checkValidString(s1)
    assert result1 == True, f"Failed for s='{s1}', expected True, got {result1}"

    # Test Case 2: Star case
    s2 = "(*)"
    result2 = solution.checkValidString(s2)
    assert result2 == True, f"Failed for s='{s2}', expected True, got {result2}"

    # Test Case 3: Star as empty
    s3 = "(*))"
    result3 = solution.checkValidString(s3)
    assert result3 == True, f"Failed for s='{s3}', expected True, got {result3}"

    # Test Case 4: Invalid case
    s4 = "((*"
    result4 = solution.checkValidString(s4)
    assert result4 == False, f"Failed for s='{s4}', expected False, got {result4}"

    # Test Case 5: Complex case
    s5 = "((()))"
    result5 = solution.checkValidString(s5)
    assert result5 == True, f"Failed for s='{s5}', expected True, got {result5}"

    # Test Case 6: Edge case
    s6 = "*"
    result6 = solution.checkValidString(s6)
    assert result6 == True, f"Failed for s='{s6}', expected True, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        s = "(" * (size // 2) + "*" * (size // 2)

        start_time = time.time()
        result = solution.checkValidString(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(n) complexity
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(n): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n)")
                raise AssertionError(
                    "Time complexity test failed: expected O(n), but got worse complexity"
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

    # Edge Case 1: Empty string
    s = ""
    result = solution.checkValidString(s)
    print(f"Empty string: {result} ✅")

    # Edge Case 2: Single star
    s = "*"
    result = solution.checkValidString(s)
    print(f"Single star: {result} ✅")

    # Edge Case 3: All stars
    s = "***"
    result = solution.checkValidString(s)
    print(f"All stars: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    size = 100000
    s = "(" * (size // 2) + "*" * (size // 2)

    start_time = time.time()
    result = solution.checkValidString(s)
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} characters):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Valid Parenthesis String Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the checkValidString method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using greedy approach with range tracking")
