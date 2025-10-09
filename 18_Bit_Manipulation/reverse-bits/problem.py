"""
Reverse Bits - LeetCode Problem 190

Reverse bits of a given 32 bits unsigned integer.

Note:

- Note that in some languages such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary
representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement
notation. Therefore, in Example 2 above, the input represents the signed
integer -3 and the output represents the signed integer -1073741825.
"""

import time


class Solution:
    def reverseBits(self, n):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic case
    n1 = 0b00000010100101000001111010011100
    result1 = solution.reverseBits(n1)
    expected1 = 0b00111001011110000010100101000000
    assert (
        result1 == expected1
    ), f"Failed for n={n1}, expected {expected1}, got {result1}"

    # Test Case 2: Negative case
    n2 = 0b11111111111111111111111111111101
    result2 = solution.reverseBits(n2)
    expected2 = 0b10111111111111111111111111111111
    assert (
        result2 == expected2
    ), f"Failed for n={n2}, expected {expected2}, got {result2}"

    # Test Case 3: Zero
    n3 = 0b00000000000000000000000000000000
    result3 = solution.reverseBits(n3)
    expected3 = 0b00000000000000000000000000000000
    assert (
        result3 == expected3
    ), f"Failed for n={n3}, expected {expected3}, got {result3}"

    # Test Case 4: All ones
    n4 = 0b11111111111111111111111111111111
    result4 = solution.reverseBits(n4)
    expected4 = 0b11111111111111111111111111111111
    assert (
        result4 == expected4
    ), f"Failed for n={n4}, expected {expected4}, got {result4}"

    # Test Case 5: Single bit
    n5 = 0b00000000000000000000000000000001
    result5 = solution.reverseBits(n5)
    expected5 = 0b10000000000000000000000000000000
    assert (
        result5 == expected5
    ), f"Failed for n={n5}, expected {expected5}, got {result5}"

    # Test Case 6: Edge case
    n6 = 0b10000000000000000000000000000000
    result6 = solution.reverseBits(n6)
    expected6 = 0b00000000000000000000000000000001
    assert (
        result6 == expected6
    ), f"Failed for n={n6}, expected {expected6}, got {result6}"

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
        result = solution.reverseBits(n)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{bin(n)[:20]}...\t{elapsed_time:.6f}s\tResult: {bin(result)[:20]}...")

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
    result = solution.reverseBits(0)
    print(f"Zero: {result} ✅")

    # Edge Case 2: Single bit
    result = solution.reverseBits(1)
    print(f"Single bit: {result} ✅")

    # Edge Case 3: All ones
    result = solution.reverseBits(0xFFFFFFFF)
    print(f"All ones: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large number
    n = 0xAAAAAAAA  # Alternating bits

    start_time = time.time()
    result = solution.reverseBits(n)
    elapsed_time = time.time() - start_time

    print(f"Large number (alternating bits):")
    print(f"Time: {elapsed_time:.6f}s, Result: {bin(result)}")


if __name__ == "__main__":
    print("🧪 Testing Reverse Bits Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the reverseBits method")
        print("- Aim for O(1) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(1)")
        print("- Consider using bit manipulation techniques")
