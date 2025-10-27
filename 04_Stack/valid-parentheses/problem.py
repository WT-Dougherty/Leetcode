"""
Valid Parentheses - LeetCode Problem 20

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

import time
import random


class Solution:
    def isValid(self, s: str) -> bool:
        closers, openers = dict(), set()
        closers[")"], closers["}"], closers["]"] = "(", "{", "["
        openers.add("("), openers.add("{"), openers.add("[")
        stack = []

        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if stack and stack.pop() == closers[c]:
                    continue
                return False
            else:
                return False
        return len(stack) == 0


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic valid case
    s1 = "()"
    result1 = solution.isValid(s1)
    assert result1 == True, f"Failed for '{s1}', expected True, got {result1}"

    # Test Case 2: Multiple types
    s2 = "()[]{}"
    result2 = solution.isValid(s2)
    assert result2 == True, f"Failed for '{s2}', expected True, got {result2}"

    # Test Case 3: Invalid case
    s3 = "(]"
    result3 = solution.isValid(s3)
    assert result3 == False, f"Failed for '{s3}', expected False, got {result3}"

    # Test Case 4: Nested brackets
    s4 = "([{}])"
    result4 = solution.isValid(s4)
    assert result4 == True, f"Failed for '{s4}', expected True, got {result4}"

    # Test Case 5: Unmatched opening
    s5 = "([)]"
    result5 = solution.isValid(s5)
    assert result5 == False, f"Failed for '{s5}', expected False, got {result5}"

    # Test Case 6: Empty string
    s6 = ""
    result6 = solution.isValid(s6)
    assert result6 == True, f"Failed for '{s6}', expected True, got {result6}"

    # Test Case 7: Single character
    s7 = "("
    result7 = solution.isValid(s7)
    assert result7 == False, f"Failed for '{s7}', expected False, got {result7}"

    # Test Case 8: Only closing brackets
    s8 = ")]}"
    result8 = solution.isValid(s8)
    assert result8 == False, f"Failed for '{s8}', expected False, got {result8}"

    # Test Case 9: Complex valid case
    s9 = "{[()]}"
    result9 = solution.isValid(s9)
    assert result9 == True, f"Failed for '{s9}', expected True, got {result9}"

    # Test Case 10: Complex invalid case
    s10 = "{[()]"
    result10 = solution.isValid(s10)
    assert result10 == False, f"Failed for '{s10}', expected False, got {result10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - balanced parentheses
        brackets = ["(", ")", "[", "]", "{", "}"]
        s = "".join(random.choices(brackets, k=size))

        # Test approach
        start_time = time.time()
        result = solution.isValid(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

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
    s = "(" * 5000 + ")" * 5000
    result = solution.isValid(s)
    print(f"Maximum length (10k chars): {result} ✅")

    # Edge Case 2: All opening brackets
    s = "(" * 1000
    result = solution.isValid(s)
    print(f"All opening brackets: {result} ✅")

    # Edge Case 3: All closing brackets
    s = ")" * 1000
    result = solution.isValid(s)
    print(f"All closing brackets: {result} ✅")

    # Edge Case 4: Alternating brackets
    s = "()" * 500
    result = solution.isValid(s)
    print(f"Alternating brackets: {result} ✅")

    # Edge Case 5: Deep nesting
    s = "(" * 100 + ")" * 100
    result = solution.isValid(s)
    print(f"Deep nesting: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    brackets = ["(", ")", "[", "]", "{", "}"]
    s = "".join(random.choices(brackets, k=100000))

    start_time = time.time()
    result = solution.isValid(s)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 characters):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Valid Parentheses Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isValid method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use stack data structure")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using stack data structure")
