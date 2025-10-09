"""
Valid Anagram - LeetCode Problem 242

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

import time
import random
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic anagram
    s1, t1 = "anagram", "nagaram"
    assert solution.isAnagram(s1, t1) == True, f"Failed for s='{s1}', t='{t1}'"

    # Test Case 2: Not an anagram
    s2, t2 = "rat", "car"
    assert solution.isAnagram(s2, t2) == False, f"Failed for s='{s2}', t='{t2}'"

    # Test Case 3: Single character
    s3, t3 = "a", "a"
    assert solution.isAnagram(s3, t3) == True, f"Failed for s='{s3}', t='{t3}'"

    # Test Case 4: Different lengths
    s4, t4 = "ab", "a"
    assert solution.isAnagram(s4, t4) == False, f"Failed for s='{s4}', t='{t4}'"

    # Test Case 5: Empty strings
    s5, t5 = "", ""
    assert solution.isAnagram(s5, t5) == True, f"Failed for s='{s5}', t='{t5}'"

    # Test Case 6: Same string
    s6, t6 = "listen", "listen"
    assert solution.isAnagram(s6, t6) == True, f"Failed for s='{s6}', t='{t6}'"

    # Test Case 7: Complex anagram
    s7, t7 = "silent", "listen"
    assert solution.isAnagram(s7, t7) == True, f"Failed for s='{s7}', t='{t7}'"

    # Test Case 8: Repeated characters
    s8, t8 = "aabbcc", "ccbbaa"
    assert solution.isAnagram(s8, t8) == True, f"Failed for s='{s8}', t='{t8}'"

    # Test Case 9: Not anagram with repeated chars
    s9, t9 = "aabbcc", "aabbcd"
    assert solution.isAnagram(s9, t9) == False, f"Failed for s='{s9}', t='{t9}'"

    # Test Case 10: Long strings
    s10, t10 = "abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"
    assert solution.isAnagram(s10, t10) == True, f"Failed for s='{s10}', t='{t10}'"

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
        # Generate test data - create anagram pairs
        chars = list("abcdefghijklmnopqrstuvwxyz")
        s = ''.join(random.choices(chars, k=size))
        t = list(s)
        random.shuffle(t)
        t = ''.join(t)

        # Test approach
        start_time = time.time()
        result = solution.isAnagram(s, t)
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

    # Edge Case 1: Single character
    result = solution.isAnagram("a", "a")
    print(f"Single character same: {result} ✅")

    # Edge Case 2: Single character different
    result = solution.isAnagram("a", "b")
    print(f"Single character different: {result} ✅")

    # Edge Case 3: Maximum constraint length
    s = "a" * 50000
    t = "a" * 50000
    result = solution.isAnagram(s, t)
    print(f"Maximum length (50k chars): {result} ✅")

    # Edge Case 4: All same characters
    s = "aaaaa"
    t = "aaaaa"
    result = solution.isAnagram(s, t)
    print(f"All same characters: {result} ✅")

    # Edge Case 5: One character difference
    s = "abcdef"
    t = "abcdeg"
    result = solution.isAnagram(s, t)
    print(f"One character difference: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset - anagrams
    chars = list("abcdefghijklmnopqrstuvwxyz")
    s = ''.join(random.choices(chars, k=100000))
    t = list(s)
    random.shuffle(t)
    t = ''.join(t)

    start_time = time.time()
    result1 = solution.isAnagram(s, t)
    time1 = time.time() - start_time

    print(f"Large dataset (100,000 chars, anagrams):")
    print(f"Time: {time1:.6f}s, Result: {result1}")

    # Large dataset - not anagrams
    s2 = ''.join(random.choices(chars, k=100000))
    t2 = ''.join(random.choices(chars, k=100000))

    start_time = time.time()
    result2 = solution.isAnagram(s2, t2)
    time2 = time.time() - start_time

    print(f"\nLarge dataset (100,000 chars, not anagrams):")
    print(f"Time: {time2:.6f}s, Result: {result2}")


if __name__ == "__main__":
    print("🧪 Testing Valid Anagram Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the isAnagram method")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using hash maps or other O(n) approaches")
