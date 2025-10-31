"""
Kth Largest Element in a Stream - LeetCode Problem 703

Design a class to find the kth largest element in a stream. Note that it is the kth largest
element in sorted order, not the kth distinct element.
"""

import time
from typing import List


class MinHeap:
    def __init__(self):
        self.h = []

    def heapifyUp(self):
        i = len(self.h) - 1
        while i != 0 and self.h[i] < self.h[self.parent(i)]:
            if not self.swap(i, i // 2):
                raise Exception
            i = self.parent(i)

    def heapifyDown(self):
        i = 0
        while True:
            l, r = i * 2 + 1, i * 2 + 2

            # condition: at the bottom
            if r >= len(self.h):
                if l >= len(self.h):
                    return
                else:
                    if self.h[i] < self.h[l]:
                        return
                    else:
                        self.swap(i, l)
                        return

            if self.h[l] <= self.h[r]:
                min_child = l
            else:
                min_child = r

            if self.h[i] < self.h[min_child]:
                return
            self.swap(i, min_child)
            i = min_child

    def add(self, num: int):
        self.h.append(num)
        self.heapifyUp()

    def removeMin(self) -> int:
        if len(self.h) == 1:
            return self.h.pop()
        else:
            self.swap(0, len(self.h) - 1)
            rv = self.h.pop()
            self.heapifyDown()
            return rv

    def getMin(self) -> int:
        if len(self.h) == 0:
            return None
        else:
            return self.h[0]

    # functions to heap with heapify
    def swap(self, i1: int, i2: int) -> bool:
        if 0 <= i1 < len(self.h) and 0 <= i2 < len(self.h):
            self.h[i1], self.h[i2] = self.h[i2], self.h[i1]
            return True
        else:
            return False

    @staticmethod
    def parent(i: int) -> int:
        if i % 2 == 1:
            return i // 2
        else:
            return i // 2 - 1


class KthLargest:
    h: MinHeap

    def __init__(self, k: int, nums: List[int]):
        self.h = MinHeap()
        i = 0
        while i < len(nums):
            if i < k:
                self.h.add(nums[i])
            else:
                self.add(nums[i])
            i += 1

    def add(self, val: int) -> int:
        if not self.h.getMin():
            self.h.add(val)
        elif self.h.getMin() <= val:
            self.h.removeMin()
            self.h.add(val)
        return self.h.getMin()


def test_accuracy():
    """Test accuracy with various test cases"""
    # Test Case 1: Basic functionality
    kthLargest1 = KthLargest(3, [4, 5, 8, 2])
    result1 = kthLargest1.add(3)
    assert result1 == 4, f"Failed for add(3), expected 4, got {result1}"

    result2 = kthLargest1.add(5)
    assert result2 == 5, f"Failed for add(5), expected 5, got {result2}"

    result3 = kthLargest1.add(10)
    assert result3 == 5, f"Failed for add(10), expected 5, got {result3}"

    result4 = kthLargest1.add(9)
    assert result4 == 8, f"Failed for add(9), expected 8, got {result4}"

    result5 = kthLargest1.add(4)
    assert result5 == 8, f"Failed for add(4), expected 8, got {result5}"

    # Test Case 2: Single element
    kthLargest2 = KthLargest(1, [])
    result6 = kthLargest2.add(1)
    assert result6 == 1, f"Failed for single element, expected 1, got {result6}"

    # Test Case 3: k=1 with multiple elements
    kthLargest3 = KthLargest(1, [1, 2, 3])
    result7 = kthLargest3.add(4)
    assert result7 == 4, f"Failed for k=1, expected 4, got {result7}"

    # Test Case 4: Empty initial array
    kthLargest4 = KthLargest(2, [])
    result8 = kthLargest4.add(1)
    assert result8 == 1, f"Failed for empty initial, expected 1, got {result8}"

    result9 = kthLargest4.add(2)
    assert result9 == 1, f"Failed for empty initial add(2), expected 1, got {result9}"

    # Test Case 5: Negative numbers
    kthLargest5 = KthLargest(2, [-1, -2, -3])
    result10 = kthLargest5.add(-4)
    assert result10 == -2, f"Failed for negative numbers, expected -2, got {result10}"

    # Test Case 6: Duplicate numbers
    kthLargest6 = KthLargest(3, [1, 1, 1, 1])
    result11 = kthLargest6.add(2)
    assert result11 == 1, f"Failed for duplicates, expected 1, got {result11}"

    # Test Case 7: Large numbers
    kthLargest7 = KthLargest(2, [100000, -100000])
    result12 = kthLargest7.add(0)
    assert result12 == 0, f"Failed for large numbers, expected 0, got {result12}"

    # Test Case 8: Sequential adds
    kthLargest8 = KthLargest(3, [])
    for i in range(1, 6):
        result = kthLargest8.add(i)
        if i >= 3:
            assert (
                result == i - 2
            ), f"Failed for sequential add({i}), expected {i-2}, got {result}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    # Test different input sizes
    test_sizes = [1000, 5000, 10000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Test approach - measure time for operations
        start_time = time.time()

        kthLargest = KthLargest(10, list(range(size // 2)))

        # Add numbers
        for i in range(size):
            kthLargest.add(i)

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations completed")

    # Verify O(log k) complexity for add
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log k) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log k): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log k)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(log k) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(log k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(log k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (k=1)
    kthLargest1 = KthLargest(1, [42])
    result1 = kthLargest1.add(43)
    assert result1 == 43, f"Min constraint failed: {result1}"
    print(f"Minimum constraint: ✅")

    # Edge Case 2: Maximum constraint values
    kthLargest2 = KthLargest(10000, [10**4, -(10**4)])
    result2 = kthLargest2.add(0)
    assert result2 == 0, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All same elements
    kthLargest3 = KthLargest(5, [5] * 1000)
    result3 = kthLargest3.add(5)
    assert result3 == 5, f"All same elements failed: {result3}"
    print(f"All same elements: ✅")

    # Edge Case 4: k equals initial array size
    kthLargest4 = KthLargest(3, [1, 2, 3])
    result4 = kthLargest4.add(4)
    assert result4 == 2, f"k equals initial size failed: {result4}"
    print(f"k equals initial array size: ✅")

    # Edge Case 5: Large k
    kthLargest5 = KthLargest(1000, list(range(1000)))
    result5 = kthLargest5.add(1000)
    assert result5 == 1, f"Large k failed: {result5}"
    print(f"Large k: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    print("\nBenchmarking KthLargest Operations:")

    # Large dataset
    kthLargest = KthLargest(100, list(range(1000)))

    start_time = time.time()
    # Add many numbers
    for i in range(10000):
        kthLargest.add(i)

    total_time = time.time() - start_time
    print(f"Large dataset (1,000 initial, 10,000 adds):")
    print(f"Time: {total_time:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Kth Largest Element in a Stream Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the KthLargest class methods")
        print("- Aim for O(n log k) for constructor")
        print("- Aim for O(log k) for add")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log k)")
        print("- Consider using a min heap of size k")
