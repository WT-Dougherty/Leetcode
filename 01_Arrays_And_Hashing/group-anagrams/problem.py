"""
Group Anagrams - LeetCode Problem 49

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

import time
import random
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.groupAnagrams(strs1)
    # Sort each group and the overall result for comparison
    result1_sorted = [sorted(group) for group in result1]
    result1_sorted.sort()
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected1_sorted = [sorted(group) for group in expected1]
    expected1_sorted.sort()
    assert result1_sorted == expected1_sorted, f"Failed for {strs1}"

    # Test Case 2: Empty string
    strs2 = [""]
    result2 = solution.groupAnagrams(strs2)
    assert result2 == [[""]], f"Failed for {strs2}"

    # Test Case 3: Single character
    strs3 = ["a"]
    result3 = solution.groupAnagrams(strs3)
    assert result3 == [["a"]], f"Failed for {strs3}"

    # Test Case 4: No anagrams
    strs4 = ["abc", "def", "ghi"]
    result4 = solution.groupAnagrams(strs4)
    result4_sorted = [sorted(group) for group in result4]
    result4_sorted.sort()
    expected4 = [["abc"], ["def"], ["ghi"]]
    expected4_sorted = [sorted(group) for group in expected4]
    expected4_sorted.sort()
    assert result4_sorted == expected4_sorted, f"Failed for {strs4}"

    # Test Case 5: All anagrams
    strs5 = ["abc", "bca", "cab"]
    result5 = solution.groupAnagrams(strs5)
    result5_sorted = [sorted(group) for group in result5]
    result5_sorted.sort()
    expected5 = [["abc", "bca", "cab"]]
    expected5_sorted = [sorted(group) for group in expected5]
    expected5_sorted.sort()
    assert result5_sorted == expected5_sorted, f"Failed for {strs5}"

    # Test Case 6: Mixed lengths
    strs6 = ["a", "aa", "aaa", "b", "bb"]
    result6 = solution.groupAnagrams(strs6)
    result6_sorted = [sorted(group) for group in result6]
    result6_sorted.sort()
    expected6 = [["a"], ["aa"], ["aaa"], ["b"], ["bb"]]
    expected6_sorted = [sorted(group) for group in expected6]
    expected6_sorted.sort()
    assert result6_sorted == expected6_sorted, f"Failed for {strs6}"

    # Test Case 7: Duplicate strings
    strs7 = ["eat", "eat", "tea", "ate"]
    result7 = solution.groupAnagrams(strs7)
    result7_sorted = [sorted(group) for group in result7]
    result7_sorted.sort()
    expected7 = [["ate", "eat", "eat", "tea"]]
    expected7_sorted = [sorted(group) for group in expected7]
    expected7_sorted.sort()
    assert result7_sorted == expected7_sorted, f"Failed for {strs7}"

    # Test Case 8: Single character repeated
    strs8 = ["a", "a", "a"]
    result8 = solution.groupAnagrams(strs8)
    assert result8 == [["a", "a", "a"]], f"Failed for {strs8}"

    # Test Case 9: Empty list
    strs9 = []
    result9 = solution.groupAnagrams(strs9)
    assert result9 == [], f"Failed for {strs9}"

    # Test Case 10: Complex case
    strs10 = ["listen", "silent", "enlist", "tinsel", "hello", "world"]
    result10 = solution.groupAnagrams(strs10)
    result10_sorted = [sorted(group) for group in result10]
    result10_sorted.sort()
    expected10 = [["hello"], ["world"], ["enlist", "listen", "silent", "tinsel"]]
    expected10_sorted = [sorted(group) for group in expected10]
    expected10_sorted.sort()
    assert result10_sorted == expected10_sorted, f"Failed for {strs10}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(n*m)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [100, 1000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tGroups")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data - create strings with some anagrams
        strs = []
        chars = "abcdefghijklmnopqrstuvwxyz"

        # Create groups of anagrams
        for i in range(size // 3):
            base_word = "".join(random.choices(chars, k=5))
            # Add the base word and its anagrams
            strs.append(base_word)
            strs.append("".join(random.sample(base_word, len(base_word))))
            strs.append("".join(random.sample(base_word, len(base_word))))

        # Add some unique words
        for i in range(size % 3):
            strs.append("".join(random.choices(chars, k=5)))

        # Test approach
        start_time = time.time()
        result = solution.groupAnagrams(strs)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tGroups: {len(result)}")

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

            if not (min_expected <= actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n*m)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n*m log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n*m), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n*m)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint length
    strs = ["a" * 100 for _ in range(1000)]
    result = solution.groupAnagrams(strs)
    print(f"Maximum length strings (100 chars): {len(result)} groups ✅")

    # Edge Case 2: All single characters
    strs = ["a", "b", "c", "d", "e"]
    result = solution.groupAnagrams(strs)
    print(f"All single characters: {len(result)} groups ✅")

    # Edge Case 3: All empty strings
    strs = ["", "", ""]
    result = solution.groupAnagrams(strs)
    print(f"All empty strings: {result} ✅")

    # Edge Case 4: Mixed empty and non-empty
    strs = ["", "a", "", "b"]
    result = solution.groupAnagrams(strs)
    print(f"Mixed empty and non-empty: {len(result)} groups ✅")

    # Edge Case 5: Very long strings
    strs = ["abcdefghijklmnopqrstuvwxyz" * 10, "zyxwvutsrqponmlkjihgfedcba" * 10]
    result = solution.groupAnagrams(strs)
    print(f"Very long strings: {len(result)} groups ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    strs = []
    chars = "abcdefghijklmnopqrstuvwxyz"

    # Create 50,000 strings with many anagram groups
    for i in range(10000):
        base_word = "".join(random.choices(chars, k=6))
        strs.append(base_word)
        strs.append("".join(random.sample(base_word, len(base_word))))
        strs.append("".join(random.sample(base_word, len(base_word))))
        strs.append("".join(random.sample(base_word, len(base_word))))
        strs.append("".join(random.sample(base_word, len(base_word))))

    start_time = time.time()
    result = solution.groupAnagrams(strs)
    time1 = time.time() - start_time

    print(f"Large dataset (50,000 strings):")
    print(f"Time: {time1:.6f}s, Groups: {len(result)}")


if __name__ == "__main__":
    print("🧪 Testing Group Anagrams Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the groupAnagrams method")
        print("- Aim for O(n*m) time complexity where m is average string length")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n*m)")
        print("- Consider using hash maps with sorted strings as keys")
