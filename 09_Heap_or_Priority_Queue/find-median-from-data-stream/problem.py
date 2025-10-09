"""
Find Median from Data Stream - LeetCode Problem 295

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.
"""

import time
import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    medianFinder = MedianFinder()

    # Test Case 1: Basic functionality
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    result1 = medianFinder.findMedian()
    assert result1 == 1.5, f"Failed for [1,2], expected 1.5, got {result1}"

    medianFinder.addNum(3)
    result2 = medianFinder.findMedian()
    assert result2 == 2.0, f"Failed for [1,2,3], expected 2.0, got {result2}"

    # Test Case 2: Single element
    medianFinder2 = MedianFinder()
    medianFinder2.addNum(5)
    result3 = medianFinder2.findMedian()
    assert result3 == 5.0, f"Failed for [5], expected 5.0, got {result3}"

    # Test Case 3: Two elements
    medianFinder3 = MedianFinder()
    medianFinder3.addNum(3)
    medianFinder3.addNum(1)
    result4 = medianFinder3.findMedian()
    assert result4 == 2.0, f"Failed for [3,1], expected 2.0, got {result4}"

    # Test Case 4: Negative numbers
    medianFinder4 = MedianFinder()
    medianFinder4.addNum(-1)
    medianFinder4.addNum(-2)
    medianFinder4.addNum(-3)
    result5 = medianFinder4.findMedian()
    assert result5 == -2.0, f"Failed for [-1,-2,-3], expected -2.0, got {result5}"

    # Test Case 5: Mixed positive and negative
    medianFinder5 = MedianFinder()
    medianFinder5.addNum(-1)
    medianFinder5.addNum(1)
    medianFinder5.addNum(-2)
    medianFinder5.addNum(2)
    result6 = medianFinder5.findMedian()
    assert result6 == 0.0, f"Failed for [-1,1,-2,2], expected 0.0, got {result6}"

    # Test Case 6: Duplicate numbers
    medianFinder6 = MedianFinder()
    medianFinder6.addNum(1)
    medianFinder6.addNum(1)
    medianFinder6.addNum(1)
    result7 = medianFinder6.findMedian()
    assert result7 == 1.0, f"Failed for [1,1,1], expected 1.0, got {result7}"

    # Test Case 7: Large numbers
    medianFinder7 = MedianFinder()
    medianFinder7.addNum(100000)
    medianFinder7.addNum(-100000)
    result8 = medianFinder7.findMedian()
    assert result8 == 0.0, f"Failed for [100000,-100000], expected 0.0, got {result8}"

    # Test Case 8: Sequential numbers
    medianFinder8 = MedianFinder()
    for i in range(1, 6):
        medianFinder8.addNum(i)
    result9 = medianFinder8.findMedian()
    assert result9 == 3.0, f"Failed for [1,2,3,4,5], expected 3.0, got {result9}"

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
        medianFinder = MedianFinder()

        # Test approach - measure time for operations
        start_time = time.time()

        # Add numbers
        for i in range(size):
            medianFinder.addNum(i)

        # Find median multiple times
        for _ in range(size // 10):
            medianFinder.findMedian()

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations completed")

    # Verify O(log n) complexity for addNum
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(log n) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(log n): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 0.5  # Allow 50% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(log n)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(log n) complexity")
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
    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (1 element)
    medianFinder1 = MedianFinder()
    medianFinder1.addNum(42)
    result1 = medianFinder1.findMedian()
    assert result1 == 42.0, f"Single element failed: {result1}"
    print(f"Single element: ✅")

    # Edge Case 2: Maximum constraint values
    medianFinder2 = MedianFinder()
    medianFinder2.addNum(10**5)
    medianFinder2.addNum(-(10**5))
    result2 = medianFinder2.findMedian()
    assert result2 == 0.0, f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: All same elements
    medianFinder3 = MedianFinder()
    for _ in range(1000):
        medianFinder3.addNum(5)
    result3 = medianFinder3.findMedian()
    assert result3 == 5.0, f"All same elements failed: {result3}"
    print(f"All same elements: ✅")

    # Edge Case 4: Alternating pattern
    medianFinder4 = MedianFinder()
    for i in range(100):
        medianFinder4.addNum(1 if i % 2 == 0 else -1)
    result4 = medianFinder4.findMedian()
    assert result4 == 0.0, f"Alternating pattern failed: {result4}"
    print(f"Alternating pattern: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    print("\nBenchmarking MedianFinder Operations:")

    # Large dataset
    medianFinder = MedianFinder()

    start_time = time.time()
    # Add many numbers
    for i in range(50000):
        medianFinder.addNum(i)

    # Find median multiple times
    for _ in range(1000):
        medianFinder.findMedian()

    total_time = time.time() - start_time
    print(f"Large dataset (50,000 adds, 1,000 median finds):")
    print(f"Time: {total_time:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Find Median from Data Stream Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the MedianFinder class methods")
        print("- Aim for O(log n) for addNum")
        print("- Aim for O(1) for findMedian")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(log n)")
        print("- Consider using two heaps (max heap + min heap)")
