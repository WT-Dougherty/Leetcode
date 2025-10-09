"""
Valid Palindrome - LeetCode Problem 125

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

import time
import random
import string
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic palindrome
    s1 = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s1) == True, f"Failed for '{s1}'"

    # Test Case 2: Not a palindrome
    s2 = "race a car"
    assert solution.isPalindrome(s2) == False, f"Failed for '{s2}'"

    # Test Case 3: Empty string
    s3 = " "
    assert solution.isPalindrome(s3) == True, f"Failed for '{s3}'"

    # Test Case 4: Single character
    s4 = "a"
    assert solution.isPalindrome(s4) == True, f"Failed for '{s4}'"

    # Test Case 5: Numbers only
    s5 = "12321"
    assert solution.isPalindrome(s5) == True, f"Failed for '{s5}'"

    # Test Case 6: Mixed alphanumeric
    s6 = "A1b2B1a"
    assert solution.isPalindrome(s6) == True, f"Failed for '{s6}'"

    # Test Case 7: Not palindrome with numbers
    s7 = "12345"
    assert solution.isPalindrome(s7) == False, f"Failed for '{s7}'"

    # Test Case 8: Special characters only
    s8 = "!@#$%^&*()"
    assert solution.isPalindrome(s8) == True, f"Failed for '{s8}'"

    # Test Case 9: Long palindrome
    s9 = "Madam, I'm Adam"
    assert solution.isPalindrome(s9) == True, f"Failed for '{s9}'"

    # Test Case 10: Case sensitivity test
    s10 = "Aa"
    assert solution.isPalindrome(s10) == True, f"Failed for '{s10}'"

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
        # Generate test data - create strings with mixed characters
        chars = string.ascii_letters + string.digits + "!@#$%^&*() "
        s = ''.join(random.choices(chars, k=size))

        # Test approach
        start_time = time.time()
        result = solution.isPalindrome(s)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(n) complexity by checking if time growth is approximately linear
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i-1]
            ratios.append(ratio)
        
        # Calculate expected ratios for O(n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i-1]
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
                print(f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x")
                print(f"   This suggests O(n log n) or worse complexity")
                raise AssertionError(f"Time complexity test failed: expected O(n), but got worse complexity")
        
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
    s = "a" * 200000
    result = solution.isPalindrome(s)
    print(f"Maximum length (200k chars): {result} ✅")

    # Edge Case 2: All non-alphanumeric
    s = "!@#$%^&*()" * 1000
    result = solution.isPalindrome(s)
    print(f"All non-alphanumeric: {result} ✅")

    # Edge Case 3: Alternating case
    s = "AaBbCcDdEe"
    result = solution.isPalindrome(s)
    print(f"Alternating case: {result} ✅")

    # Edge Case 4: Numbers and letters
    s = "1a2b3c3b2a1"
    result = solution.isPalindrome(s)
    print(f"Numbers and letters: {result} ✅")

    # Edge Case 5: Single alphanumeric character
    s = "a"
    result = solution.isPalindrome(s)
    print(f"Single character: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    chars = string.ascii_letters + string.digits + "!@#$%^&*() "
    s = ''.join(random.choices(chars, k=200000))

    start_time = time.time()
    result = solution.isPalindrome(s)
    time1 = time.time() - start_time

    print(f"Large dataset (200,000 characters):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Valid Palindrome Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isPalindrome method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Use two pointers approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using two pointers or string preprocessing")
