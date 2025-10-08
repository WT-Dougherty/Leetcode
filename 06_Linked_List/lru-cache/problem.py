"""
LRU Cache - LeetCode Problem 146

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise,
  add the key-value pair to the cache. If the number of keys exceeds the capacity from
  this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

import time


class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


class Solution:
    def __init__(self):
        self.cache = None

    def createLRUCache(self, capacity: int) -> LRUCache:
        """Helper method to create LRU Cache for testing"""
        self.cache = LRUCache(capacity)
        return self.cache


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: Basic operations
    cache = solution.createLRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    result1 = cache.get(1)
    assert result1 == 1, f"Failed for get(1), expected 1, got {result1}"

    cache.put(3, 3)  # evicts key 2
    result2 = cache.get(2)
    assert result2 == -1, f"Failed for get(2), expected -1, got {result2}"

    cache.put(4, 4)  # evicts key 1
    result3 = cache.get(1)
    assert result3 == -1, f"Failed for get(1), expected -1, got {result3}"

    result4 = cache.get(3)
    assert result4 == 3, f"Failed for get(3), expected 3, got {result4}"

    result5 = cache.get(4)
    assert result5 == 4, f"Failed for get(4), expected 4, got {result5}"

    # Test Case 2: Single capacity
    cache2 = solution.createLRUCache(1)
    cache2.put(1, 1)
    result6 = cache2.get(1)
    assert result6 == 1, f"Failed for single capacity get(1), expected 1, got {result6}"

    cache2.put(2, 2)  # evicts key 1
    result7 = cache2.get(1)
    assert (
        result7 == -1
    ), f"Failed for single capacity get(1), expected -1, got {result7}"

    result8 = cache2.get(2)
    assert result8 == 2, f"Failed for single capacity get(2), expected 2, got {result8}"

    # Test Case 3: Update existing key
    cache3 = solution.createLRUCache(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    cache3.put(1, 10)  # update existing key
    result9 = cache3.get(1)
    assert result9 == 10, f"Failed for update existing key, expected 10, got {result9}"

    # Test Case 4: Get non-existent key
    cache4 = solution.createLRUCache(2)
    result10 = cache4.get(1)
    assert (
        result10 == -1
    ), f"Failed for get non-existent key, expected -1, got {result10}"

    # Test Case 5: Multiple operations
    cache5 = solution.createLRUCache(3)
    cache5.put(1, 1)
    cache5.put(2, 2)
    cache5.put(3, 3)
    cache5.get(1)  # make 1 recently used
    cache5.put(4, 4)  # evicts key 2
    result11 = cache5.get(2)
    assert (
        result11 == -1
    ), f"Failed for multiple operations get(2), expected -1, got {result11}"

    result12 = cache5.get(1)
    assert (
        result12 == 1
    ), f"Failed for multiple operations get(1), expected 1, got {result12}"

    # Test Case 6: Maximum constraint
    cache6 = solution.createLRUCache(3000)
    for i in range(3000):
        cache6.put(i, i)

    result13 = cache6.get(0)
    assert (
        result13 == 0
    ), f"Failed for max constraint get(0), expected 0, got {result13}"

    cache6.put(3000, 3000)  # evicts key 0
    result14 = cache6.get(0)
    assert (
        result14 == -1
    ), f"Failed for max constraint get(0), expected -1, got {result14}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(1)"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [1000, 10000, 100000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        cache = solution.createLRUCache(size)

        # Test approach - measure time for operations
        start_time = time.time()

        # Perform operations
        for i in range(size):
            cache.put(i, i)

        for i in range(size):
            cache.get(i)

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations")

    # For O(1) operations, time should grow approximately linearly with number of operations
    # Since we do 2*size operations, expected time should be proportional to size
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(1) per operation (linear growth with operations)
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(1) operations: {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range (allowing some variance)
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (min_expected <= actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(1)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests O(log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(1), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(1)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint capacity
    cache = solution.createLRUCache(3000)
    for i in range(3000):
        cache.put(i, i)

    result = cache.get(1500)
    assert result == 1500
    print(f"Maximum capacity (3000): ✅")

    # Edge Case 2: Maximum constraint key/value
    cache2 = solution.createLRUCache(100)
    cache2.put(10000, 100000)
    result = cache2.get(10000)
    assert result == 100000
    print(f"Maximum constraint key/value: ✅")

    # Edge Case 3: Minimum constraint key/value
    cache3 = solution.createLRUCache(100)
    cache3.put(0, 0)
    result = cache3.get(0)
    assert result == 0
    print(f"Minimum constraint key/value: ✅")

    # Edge Case 4: Maximum constraint calls
    cache4 = solution.createLRUCache(1000)
    for i in range(200000):  # Simulate max calls
        cache4.put(i % 1000, i)
        cache4.get(i % 1000)

    result = cache4.get(0)
    assert result >= 0  # Should be a valid result
    print(f"Maximum constraint calls: ✅")

    # Edge Case 5: Single capacity with many operations
    cache5 = solution.createLRUCache(1)
    for i in range(1000):
        cache5.put(i, i)
        cache5.get(i)

    result = cache5.get(999)
    assert result == 999
    print(f"Single capacity with many operations: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking Solution:")

    # Large dataset
    cache = solution.createLRUCache(10000)

    start_time = time.time()
    for i in range(100000):
        cache.put(i % 10000, i)
        cache.get(i % 10000)
    time1 = time.time() - start_time

    result = cache.get(5000)
    assert result >= 0

    print(f"Large dataset (100k operations):")
    print(f"Time: {time1:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing LRU Cache Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the LRUCache class")
        print("- Aim for O(1) time complexity for get and put operations")
        print("- Handle all edge cases correctly")
        print("- Use hash map + doubly linked list")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(1)")
        print("- Consider using hash map + doubly linked list")
