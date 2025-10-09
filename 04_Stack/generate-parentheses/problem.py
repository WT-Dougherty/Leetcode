"""
Generate Parentheses - LeetCode Problem 22

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.
"""

import time
import random


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: n = 3
    n1 = 3
    result1 = solution.generateParenthesis(n1)
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert len(result1) == len(expected1), f"Failed for n={n1}, expected {len(expected1)} combinations, got {len(result1)}"
    for combo in expected1:
        assert combo in result1, f"Failed for n={n1}, missing combination '{combo}'"

    # Test Case 2: n = 1
    n2 = 1
    result2 = solution.generateParenthesis(n2)
    expected2 = ["()"]
    assert result2 == expected2, f"Failed for n={n2}, expected {expected2}, got {result2}"

    # Test Case 3: n = 2
    n3 = 2
    result3 = solution.generateParenthesis(n3)
    expected3 = ["(())", "()()"]
    assert len(result3) == len(expected3), f"Failed for n={n3}, expected {len(expected3)} combinations, got {len(result3)}"
    for combo in expected3:
        assert combo in result3, f"Failed for n={n3}, missing combination '{combo}'"

    # Test Case 4: n = 4
    n4 = 4
    result4 = solution.generateParenthesis(n4)
    expected_count4 = 14  # Catalan number C(4) = 14
    assert len(result4) == expected_count4, f"Failed for n={n4}, expected {expected_count4} combinations, got {len(result4)}"

    # Test Case 5: n = 5
    n5 = 5
    result5 = solution.generateParenthesis(n5)
    expected_count5 = 42  # Catalan number C(5) = 42
    assert len(result5) == expected_count5, f"Failed for n={n5}, expected {expected_count5} combinations, got {len(result5)}"

    # Test Case 6: n = 6
    n6 = 6
    result6 = solution.generateParenthesis(n6)
    expected_count6 = 132  # Catalan number C(6) = 132
    assert len(result6) == expected_count6, f"Failed for n={n6}, expected {expected_count6} combinations, got {len(result6)}"

    # Test Case 7: n = 7
    n7 = 7
    result7 = solution.generateParenthesis(n7)
    expected_count7 = 429  # Catalan number C(7) = 429
    assert len(result7) == expected_count7, f"Failed for n={n7}, expected {expected_count7} combinations, got {len(result7)}"

    # Test Case 8: n = 8
    n8 = 8
    result8 = solution.generateParenthesis(n8)
    expected_count8 = 1430  # Catalan number C(8) = 1430
    assert len(result8) == expected_count8, f"Failed for n={n8}, expected {expected_count8} combinations, got {len(result8)}"

    # Test Case 9: Verify all combinations are valid
    for n in [1, 2, 3, 4]:
        result = solution.generateParenthesis(n)
        for combo in result:
            # Verify each combination is valid parentheses
            balance = 0
            for char in combo:
                if char == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    assert False, f"Invalid parentheses: '{combo}'"
            assert balance == 0, f"Invalid parentheses: '{combo}'"

    # Test Case 10: Verify no duplicates
    for n in [1, 2, 3, 4]:
        result = solution.generateParenthesis(n)
        assert len(result) == len(set(result)), f"Duplicates found for n={n}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(4^n / √n)"""
    solution = Solution()

    # Test different input sizes (smaller range due to exponential growth)
    test_sizes = [4, 5, 6, 7]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tCombinations")
    print("-" * 40)

    for size in test_sizes:
        # Test approach
        start_time = time.time()
        result = solution.generateParenthesis(size)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)}")

    # Verify exponential complexity by checking if time growth is exponential
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Expected ratios for exponential growth (approximately 4x)
        expected_ratios = [4.0, 4.0, 4.0]  # Roughly 4^n growth

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(4^n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance for exponential
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(4^n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than exponential complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(4^n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(4^n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint
    n = 1
    result = solution.generateParenthesis(n)
    assert len(result) == 1
    print(f"Minimum constraint (n=1): {len(result)} combinations ✅")

    # Edge Case 2: Maximum constraint
    n = 8
    result = solution.generateParenthesis(n)
    assert len(result) == 1430
    print(f"Maximum constraint (n=8): {len(result)} combinations ✅")

    # Edge Case 3: Verify all combinations are unique
    for n in range(1, 6):
        result = solution.generateParenthesis(n)
        unique_count = len(set(result))
        assert unique_count == len(result), f"Duplicates found for n={n}"
    print(f"All combinations unique: ✅")

    # Edge Case 4: Verify all combinations are valid
    for n in range(1, 6):
        result = solution.generateParenthesis(n)
        for combo in result:
            balance = 0
            for char in combo:
                balance += 1 if char == '(' else -1
                assert balance >= 0, f"Invalid: '{combo}'"
            assert balance == 0, f"Invalid: '{combo}'"
    print(f"All combinations valid: ✅")

    # Edge Case 5: Check specific patterns
    n = 3
    result = solution.generateParenthesis(n)
    assert "((()))" in result  # All nested
    assert "()()()" in result  # All separate
    print(f"Expected patterns present: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Test with maximum constraint
    n = 8

    start_time = time.time()
    result = solution.generateParenthesis(n)
    time1 = time.time() - start_time

    print(f"Maximum constraint (n=8):")
    print(f"Time: {time1:.6f}s, Combinations: {len(result)}")


if __name__ == "__main__":
    print("🧪 Testing Generate Parentheses Problem")
    print("=" * 60)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the generateParenthesis method")
        print("- Aim for O(4^n / √n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use backtracking or recursive approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(4^n)")
        print("- Consider using backtracking approach")
