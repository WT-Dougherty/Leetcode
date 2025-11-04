"""
Time Based Key-Value Store - LeetCode Problem 981

Design a time-based key-value data structure that can store multiple values for the same
key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value
  value at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called
  previously, with timestamp_prev <= timestamp. If there are multiple such values,
  it returns the value associated with the largest timestamp_prev. If no values exist
  at that timestamp, it returns "".
"""

import time
from collections import defaultdict
import random


class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        l, r = 0, len(self.data[key]) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if self.data[key][mid][0] <= timestamp:
                l = mid
            else:
                r = mid - 1
        if self.data[key][0][0] <= timestamp:
            return self.data[key][l][1]
        else:
            return ""


def test_accuracy():
    """Test accuracy with various test cases"""
    timeMap = TimeMap()

    # Test Case 1: Basic operations
    timeMap.set("foo", "bar", 1)
    result1 = timeMap.get("foo", 1)
    assert result1 == "bar", f"Expected 'bar', got '{result1}'"

    # Test Case 2: Get with timestamp that doesn't exist
    result2 = timeMap.get("foo", 3)
    assert result2 == "bar", f"Expected 'bar', got '{result2}'"

    # Test Case 3: Set and get with new timestamp
    timeMap.set("foo", "bar2", 4)
    result3 = timeMap.get("foo", 4)
    assert result3 == "bar2", f"Expected 'bar2', got '{result3}'"

    # Test Case 4: Get with timestamp between two values
    result4 = timeMap.get("foo", 5)
    assert result4 == "bar2", f"Expected 'bar2', got '{result4}'"

    # Test Case 5: Get non-existent key
    result5 = timeMap.get("baz", 1)
    assert result5 == "", f"Expected '', got '{result5}'"

    # Test Case 6: Multiple keys
    timeMap.set("key1", "value1", 1)
    timeMap.set("key2", "value2", 2)
    result6a = timeMap.get("key1", 1)
    result6b = timeMap.get("key2", 2)
    assert result6a == "value1", f"Expected 'value1', got '{result6a}'"
    assert result6b == "value2", f"Expected 'value2', got '{result6b}'"

    # Test Case 7: Same key, multiple timestamps
    timeMap.set("test", "v1", 1)
    timeMap.set("test", "v2", 2)
    timeMap.set("test", "v3", 3)
    result7a = timeMap.get("test", 1)
    result7b = timeMap.get("test", 2)
    result7c = timeMap.get("test", 3)
    assert result7a == "v1", f"Expected 'v1', got '{result7a}'"
    assert result7b == "v2", f"Expected 'v2', got '{result7b}'"
    assert result7c == "v3", f"Expected 'v3', got '{result7c}'"

    # Test Case 8: Get with timestamp before any set
    result8 = timeMap.get("test", 0)
    assert result8 == "", f"Expected '', got '{result8}'"

    # Test Case 9: Large timestamps
    timeMap.set("large", "value", 1000000)
    result9 = timeMap.get("large", 1000000)
    assert result9 == "value", f"Expected 'value', got '{result9}'"

    # Test Case 10: Edge case with minimum timestamp
    timeMap.set("min", "val", 1)
    result10 = timeMap.get("min", 1)
    assert result10 == "val", f"Expected 'val', got '{result10}'"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(log n) for get"""
    timeMap = TimeMap()

    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Generate test data
        key = "test_key"
        for i in range(size):
            timeMap.set(key, f"value_{i}", i + 1)

        # Test get operations
        target_timestamp = random.randint(1, size)
        start_time = time.time()
        result = timeMap.get(key, target_timestamp)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{result}")

    # Verify O(log n) complexity for get operations
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            n1, n2 = test_sizes[i - 1], test_sizes[i]
            expected_ratio = (n2.bit_length() - 1) / (n1.bit_length() - 1)
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 1.0  # Allow 100% variance for logarithmic
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(log n), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log n)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    timeMap = TimeMap()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint calls
    for i in range(100000):  # Simulate max calls
        timeMap.set(f"key_{i % 1000}", f"value_{i}", i + 1)

    result = timeMap.get("key_0", 50000)
    print(f"Maximum constraint calls: {result} ✅")

    # Edge Case 2: Maximum constraint timestamp
    timeMap.set("max_ts", "value", 10**7)
    result = timeMap.get("max_ts", 10**7)
    assert result == "value"
    print(f"Maximum constraint timestamp: {result} ✅")

    # Edge Case 3: Minimum constraint timestamp
    timeMap.set("min_ts", "value", 1)
    result = timeMap.get("min_ts", 1)
    assert result == "value"
    print(f"Minimum constraint timestamp: {result} ✅")

    # Edge Case 4: Maximum constraint key/value length
    long_key = "a" * 100
    long_value = "b" * 100
    timeMap.set(long_key, long_value, 1)
    result = timeMap.get(long_key, 1)
    assert result == long_value
    print(f"Maximum constraint key/value length: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    timeMap = TimeMap()

    print("\nBenchmarking Solution:")

    # Large dataset
    key = "benchmark_key"
    for i in range(50000):
        timeMap.set(key, f"value_{i}", i + 1)

    start_time = time.time()
    result = timeMap.get(key, 25000)
    time1 = time.time() - start_time

    print(f"Large dataset (50k timestamps):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Time Based Key-Value Store Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the TimeMap class")
        print("- Aim for O(log n) time complexity for get operations")
        print("- Handle all edge cases correctly")
        print("- Use binary search for timestamp lookups")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using binary search for timestamp lookups")
