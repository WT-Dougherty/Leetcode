"""
Detect Squares - LeetCode Problem 2013

You are given a stream of points on the X-Y plane. Design an algorithm that:

- Adds new points from the stream into a data structure. Duplicate points are allowed
and should be treated as different points.
- Given a query point, counts the number of ways to choose three points from
the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all aligned with the x-axis and y-axis.

Implement the DetectSquares class:

- DetectSquares() Initializes the object with an empty data structure.
- void add(int[] point) Adds a new point point = [x, y] to the data structure.
- int count(int[] point) Counts the number of ways to form axis-aligned squares
with point point = [x, y] as one of the vertices of the squares.
"""

import time


class DetectSquares:
    def __init__(self):
        pass

    def add(self, point):
        pass

    def count(self, point):
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    detectSquares = DetectSquares()

    # Test Case 1: Basic case
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    result1 = detectSquares.count([11, 10])
    assert result1 == 1, f"Failed for count([11, 10]), expected 1, got {result1}"

    # Test Case 2: No squares
    result2 = detectSquares.count([14, 8])
    assert result2 == 0, f"Failed for count([14, 8]), expected 0, got {result2}"

    # Test Case 3: Duplicate points
    detectSquares.add([11, 2])
    result3 = detectSquares.count([11, 10])
    assert (
        result3 == 2
    ), f"Failed for count([11, 10]) after duplicate, expected 2, got {result3}"

    # Test Case 4: Edge case
    detectSquares2 = DetectSquares()
    detectSquares2.add([0, 0])
    detectSquares2.add([1, 0])
    detectSquares2.add([0, 1])
    result4 = detectSquares2.count([1, 1])
    assert result4 == 1, f"Failed for count([1, 1]), expected 1, got {result4}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(k) for count"""
    detectSquares = DetectSquares()

    test_sizes = [100, 500, 1000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Add points
        for i in range(size):
            detectSquares.add([i, i])

        # Test count operation
        start_time = time.time()
        result = detectSquares.count([size // 2, size // 2])
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tResult: {result}")

    # Verify O(k) complexity for count
    if len(times) >= 2:
        ratios = [times[i] / times[i - 1] for i in range(1, len(times))]
        expected_ratios = [
            test_sizes[i] / test_sizes[i - 1] for i in range(1, len(test_sizes))
        ]

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(k): {[f'{r:.2f}x' for r in expected_ratios]}")

        tolerance = 0.5
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            max_expected = expected * (1 + tolerance)
            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(k)")
                raise AssertionError(
                    "Time complexity test failed: expected O(k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    detectSquares = DetectSquares()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Empty data structure
    result = detectSquares.count([0, 0])
    print(f"Empty data structure: {result} ✅")

    # Edge Case 2: Single point
    detectSquares.add([0, 0])
    result = detectSquares.count([0, 0])
    print(f"Single point: {result} ✅")

    # Edge Case 3: Large coordinates
    detectSquares.add([1000, 1000])
    detectSquares.add([1000, 0])
    detectSquares.add([0, 1000])
    result = detectSquares.count([0, 0])
    print(f"Large coordinates: {result} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    detectSquares = DetectSquares()

    print("\nBenchmarking Solution:")

    # Large dataset
    size = 1000
    for i in range(size):
        detectSquares.add([i, i])

    start_time = time.time()
    result = detectSquares.count([size // 2, size // 2])
    elapsed_time = time.time() - start_time

    print(f"Large dataset ({size} points):")
    print(f"Time: {elapsed_time:.6f}s, Result: {result}")


if __name__ == "__main__":
    print("🧪 Testing Detect Squares Problem")
    print("=" * 50)

    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the DetectSquares class")
        print("- Aim for O(1) time complexity for add, O(k) for count")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(k)")
        print("- Consider using hash map to store points")
