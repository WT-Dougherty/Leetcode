"""
Min Stack - LeetCode Problem 155

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

import time
import random


class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    # Test Case 1: Basic operations
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3, f"Expected -3, got {minStack.getMin()}"
    minStack.pop()
    assert minStack.top() == 0, f"Expected 0, got {minStack.top()}"
    assert minStack.getMin() == -2, f"Expected -2, got {minStack.getMin()}"

    # Test Case 2: Single element
    minStack = MinStack()
    minStack.push(5)
    assert minStack.top() == 5, f"Expected 5, got {minStack.top()}"
    assert minStack.getMin() == 5, f"Expected 5, got {minStack.getMin()}"

    # Test Case 3: Increasing sequence
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(3)
    assert minStack.getMin() == 1, f"Expected 1, got {minStack.getMin()}"
    assert minStack.top() == 3, f"Expected 3, got {minStack.top()}"

    # Test Case 4: Decreasing sequence
    minStack = MinStack()
    minStack.push(3)
    minStack.push(2)
    minStack.push(1)
    assert minStack.getMin() == 1, f"Expected 1, got {minStack.getMin()}"
    assert minStack.top() == 1, f"Expected 1, got {minStack.top()}"

    # Test Case 5: Duplicate minimums
    minStack = MinStack()
    minStack.push(2)
    minStack.push(1)
    minStack.push(1)
    assert minStack.getMin() == 1, f"Expected 1, got {minStack.getMin()}"
    minStack.pop()
    assert minStack.getMin() == 1, f"Expected 1, got {minStack.getMin()}"

    # Test Case 6: Large numbers
    minStack = MinStack()
    minStack.push(2147483647)
    minStack.push(-2147483648)
    assert (
        minStack.getMin() == -2147483648
    ), f"Expected -2147483648, got {minStack.getMin()}"

    # Test Case 7: Mixed operations
    minStack = MinStack()
    minStack.push(10)
    minStack.push(5)
    minStack.push(15)
    minStack.push(3)
    minStack.push(8)
    assert minStack.getMin() == 3, f"Expected 3, got {minStack.getMin()}"
    minStack.pop()
    assert minStack.top() == 3, f"Expected 3, got {minStack.top()}"
    assert minStack.getMin() == 3, f"Expected 3, got {minStack.getMin()}"

    # Test Case 8: Zero values
    minStack = MinStack()
    minStack.push(0)
    minStack.push(0)
    assert minStack.getMin() == 0, f"Expected 0, got {minStack.getMin()}"
    assert minStack.top() == 0, f"Expected 0, got {minStack.top()}"

    # Test Case 9: Negative numbers
    minStack = MinStack()
    minStack.push(-1)
    minStack.push(-5)
    minStack.push(-3)
    assert minStack.getMin() == -5, f"Expected -5, got {minStack.getMin()}"

    # Test Case 10: Complex sequence
    minStack = MinStack()
    operations = [5, 3, 7, 1, 9, 2, 4]
    for op in operations:
        minStack.push(op)
    assert minStack.getMin() == 1, f"Expected 1, got {minStack.getMin()}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than O(1) per operation"""
    # Test different input sizes
    test_sizes = [1000, 10000, 30000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tOperations")
    print("-" * 40)

    for size in test_sizes:
        minStack = MinStack()

        # Test approach
        start_time = time.time()

        # Perform operations
        for i in range(size):
            val = random.randint(-10000, 10000)
            minStack.push(val)

        # Test getMin operations
        for i in range(size // 10):  # Test 10% of operations
            minStack.getMin()

        # Test pop operations
        for i in range(size // 2):  # Pop half
            minStack.pop()

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{size + size//10 + size//2}")

    # Verify O(1) complexity by checking if time per operation is constant
    if len(times) >= 2:
        # Calculate time per operation
        operations = [size + size // 10 + size // 2 for size in test_sizes]
        time_per_op = [times[i] / operations[i] for i in range(len(times))]

        print(f"\nTime per operation: {[f'{t:.8f}s' for t in time_per_op]}")

        # Check if time per operation is roughly constant (within 50% variance)
        tolerance = 0.5
        avg_time_per_op = sum(time_per_op) / len(time_per_op)

        for i, tpo in enumerate(time_per_op):
            min_expected = avg_time_per_op * (1 - tolerance)
            max_expected = avg_time_per_op * (1 + tolerance)

            if not (min_expected <= tpo <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(1)")
                print(f"   Size {test_sizes[i]}: time per operation {tpo:.8f}s")
                print(f"   Expected around {avg_time_per_op:.8f}s (±{tolerance*100}%)")
                print(f"   This suggests O(log n) or worse complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(1), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(1) per operation")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\nTesting Edge Cases:")

    # Edge Case 1: Maximum constraint calls
    minStack = MinStack()
    for i in range(30000):
        minStack.push(random.randint(-2147483648, 2147483647))
    print(f"Maximum constraint calls (30k): {minStack.getMin()} ✅")

    # Edge Case 2: Maximum integer values
    minStack = MinStack()
    minStack.push(2147483647)
    minStack.push(-2147483648)
    assert minStack.getMin() == -2147483648
    print(f"Maximum integer values: {minStack.getMin()} ✅")

    # Edge Case 3: All same values
    minStack = MinStack()
    for i in range(1000):
        minStack.push(42)
    assert minStack.getMin() == 42
    print(f"All same values: {minStack.getMin()} ✅")

    # Edge Case 4: Alternating min values
    minStack = MinStack()
    for i in range(100):
        minStack.push(1 if i % 2 == 0 else 2)
    assert minStack.getMin() == 1
    print(f"Alternating min values: {minStack.getMin()} ✅")

    # Edge Case 5: Zero values
    minStack = MinStack()
    for i in range(100):
        minStack.push(0)
    assert minStack.getMin() == 0
    print(f"Zero values: {minStack.getMin()} ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark solution with large datasets"""
    print("\nBenchmarking Solution:")

    # Large dataset
    minStack = MinStack()

    start_time = time.time()

    # Push operations
    for i in range(30000):
        minStack.push(random.randint(-10000, 10000))

    # Mixed operations
    for i in range(10000):
        if i % 3 == 0:
            minStack.pop()
        elif i % 3 == 1:
            minStack.top()
        else:
            minStack.getMin()

    time1 = time.time() - start_time

    print(f"Large dataset (30k push + 10k mixed operations):")
    print(f"Time: {time1:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Min Stack Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the MinStack class")
        print("- Aim for O(1) time complexity for all operations")
        print("- Handle all edge cases correctly")
        print("- Use auxiliary stack or other O(1) approach")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(1)")
        print("- Consider using auxiliary stack for minimum tracking")
