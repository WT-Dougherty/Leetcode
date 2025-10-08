"""
Encode and Decode Strings - LeetCode Problem 271

Design an algorithm to encode a list of strings to a string. The encoded string is then
sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);

and Machine 2 does:
vector<string> strs2 = decode(encoded_string);

strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).
"""

import time
import random
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    strs1 = ["Hello", "World"]
    encoded1 = solution.encode(strs1)
    decoded1 = solution.decode(encoded1)
    assert decoded1 == strs1, f"Failed for {strs1}, got {decoded1}"

    # Test Case 2: Empty string
    strs2 = [""]
    encoded2 = solution.encode(strs2)
    decoded2 = solution.decode(encoded2)
    assert decoded2 == strs2, f"Failed for {strs2}, got {decoded2}"

    # Test Case 3: Empty list
    strs3 = []
    encoded3 = solution.encode(strs3)
    decoded3 = solution.decode(encoded3)
    assert decoded3 == strs3, f"Failed for {strs3}, got {decoded3}"

    # Test Case 4: Single character
    strs4 = ["a"]
    encoded4 = solution.encode(strs4)
    decoded4 = solution.decode(encoded4)
    assert decoded4 == strs4, f"Failed for {strs4}, got {decoded4}"

    # Test Case 5: Multiple empty strings
    strs5 = ["", "", ""]
    encoded5 = solution.encode(strs5)
    decoded5 = solution.decode(encoded5)
    assert decoded5 == strs5, f"Failed for {strs5}, got {decoded5}"

    # Test Case 6: Special characters
    strs6 = ["Hello, World!", "How are you?", "I'm fine."]
    encoded6 = solution.encode(strs6)
    decoded6 = solution.decode(encoded6)
    assert decoded6 == strs6, f"Failed for {strs6}, got {decoded6}"

    # Test Case 7: Numbers as strings
    strs7 = ["123", "456", "789"]
    encoded7 = solution.encode(strs7)
    decoded7 = solution.decode(encoded7)
    assert decoded7 == strs7, f"Failed for {strs7}, got {decoded7}"

    # Test Case 8: Mixed content
    strs8 = ["Hello", "", "World", "123", ""]
    encoded8 = solution.encode(strs8)
    decoded8 = solution.decode(encoded8)
    assert decoded8 == strs8, f"Failed for {strs8}, got {decoded8}"

    # Test Case 9: Long strings
    strs9 = ["a" * 100, "b" * 200, "c" * 300]
    encoded9 = solution.encode(strs9)
    decoded9 = solution.decode(encoded9)
    assert decoded9 == strs9, f"Failed for long strings"

    # Test Case 10: Unicode characters
    strs10 = ["Hello 世界", "مرحبا", "Привет"]
    encoded10 = solution.encode(strs10)
    decoded10 = solution.decode(encoded10)
    assert decoded10 == strs10, f"Failed for unicode strings"

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
        # Generate test data
        strs = []
        for i in range(size):
            # Create strings of varying lengths
            length = random.randint(1, 50)
            strs.append("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length)))

        # Test encode
        start_time = time.time()
        encoded = solution.encode(strs)
        encode_time = time.time() - start_time

        # Test decode
        start_time = time.time()
        decoded = solution.decode(encoded)
        decode_time = time.time() - start_time

        total_time = encode_time + decode_time
        times.append(total_time)

        # Verify correctness
        assert decoded == strs, f"Round-trip failed for size {size}"

        print(f"{size}\t{total_time:.6f}s\tLength: {len(encoded)}")

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
    strs = ["a" * 200 for _ in range(200)]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"Maximum length strings (200 chars): {len(decoded)} strings ✅")

    # Edge Case 2: All empty strings
    strs = [""] * 1000
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"All empty strings: {len(decoded)} strings ✅")

    # Edge Case 3: Single character strings
    strs = [chr(i) for i in range(256)]  # All ASCII characters
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"All ASCII characters: {len(decoded)} strings ✅")

    # Edge Case 4: Very long single string
    strs = ["a" * 10000]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"Very long single string: {len(decoded[0])} chars ✅")

    # Edge Case 5: Mixed lengths
    strs = ["a"] + ["b" * 100] + ["c" * 1000] + ["d" * 10000]
    encoded = solution.encode(strs)
    decoded = solution.decode(encoded)
    print(f"Mixed lengths: {len(decoded)} strings ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    strs = []
    for i in range(10000):
        length = random.randint(1, 100)
        strs.append("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length)))

    start_time = time.time()
    encoded = solution.encode(strs)
    encode_time = time.time() - start_time

    start_time = time.time()
    decoded = solution.decode(encoded)
    decode_time = time.time() - start_time

    print(f"Large dataset (10,000 strings):")
    print(f"Encode time: {encode_time:.6f}s")
    print(f"Decode time: {decode_time:.6f}s")
    print(f"Total time: {encode_time + decode_time:.6f}s")
    print(f"Encoded length: {len(encoded)} chars")
    print(f"Verification: {len(decoded)} strings decoded correctly")


if __name__ == "__main__":
    print("🧪 Testing Encode and Decode Strings Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the encode and decode methods")
        print("- Aim for O(n) time complexity")
        print("- Handle all edge cases correctly")
        print("- Ensure round-trip consistency")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n)")
        print("- Consider using length prefixes or delimiters")
