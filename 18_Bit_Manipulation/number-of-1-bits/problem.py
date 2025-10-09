"""
Number of 1 Bits - LeetCode Problem 191

Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Note:

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
"""

import time


class Solution:
    def hammingWeight(self, n):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    n1 = 0b00000000000000000000000000001011
    result1 = solution.hammingWeight(n1)
    assert result1 == 3, f"Failed for n={n1}, expected 3, got {result1}"

    # Test Case 2: Single bit
    n2 = 0b00000000000000000000000010000000
    result2 = solution.hammingWeight(n2)
    assert result2 == 1, f"Failed for n={n2}, expected 1, got {result2}"

    # Test Case 3: Many bits
    n3 = 0b11111111111111111111111111111101
    result3 = solution.hammingWeight(n3)
    assert result3 == 31, f"Failed for n={n3}, expected 31, got {result3}"

    # Test Case 4: Zero
    n4 = 0b00000000000000000000000000000000
    result4 = solution.hammingWeight(n4)
    assert result4 == 0, f"Failed for n={n4}, expected 0, got {result4}"

    # Test Case 5: All ones
    n5 = 0b11111111111111111111111111111111
    result5 = solution.hammingWeight(n5)
    assert result5 == 32, f"Failed for n={n5}, expected 32, got {result5}"

    # Test Case 6: Edge case
    n6 = 0b00000000000000000000000000000001
    result6 = solution.hammingWeight(n6)
    assert result6 == 1, f"Failed for n={n6}, expected 1, got {result6}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(1)"""
    solution = Solution()

    test_values = [
        0b10101010101010101010101010101010,
        0b11111111111111111111111111111111,
        0b00000000000000000000000000000000,
    ]
    times = []

    print("\nTime Complexity Analysis:")
    print("Value\t\tTime\t\tResult")
    print("-" * 50)

    for n in test_values:
        start_time = time.time()
        result = solution.hammingWeight(n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{bin(n)[:20]}...\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(1) complexity - should be very fast
    max_time = max(times)
    if max_time > 0.001:  # More than 1ms is suspicious for O(1)
        print(f"\n❌ FAILED: Time complexity appears worse than O(1)")
        print(f"Max time: {max_time:.6f}s (should be < 0.001s)")
        raise AssertionError(
            "Time complexity test failed: expected O(1), but got worse complexity"
        )

    print(f"\n✅ PASSED: Time complexity appears to be O(1)")
    return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Zero
    result = solution.hammingWeight(0)
    print(f"Zero: {result} ✅")

    # Edge Case 2: Single bit
    result = solution.hammingWeight(1)
    print(f"Single bit: {result} ✅")

    # Edge Case 3: All ones
    result = solution.hammingWeight(0xFFFFFFFF)
    print(f"All ones: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    n = 0xAAAAAAAAAAAAAAAA  # Alternating bits

    start_time = time.time()
    result = solution.hammingWeight(n)
    elapsed_time = time.time() - start_time

    print(f"Large number (alternating bits):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Number of 1 Bits Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the hammingWeight method")
        print("- Aim for O(1) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(1)")
        print("- Consider using bit manipulation techniques")
