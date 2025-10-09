"""
N-Queens - LeetCode Problem 51

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.
"""

import time
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    solution = Solution()

    # Test Case 1: n=4
    n1 = 4
    result1 = solution.solveNQueens(n1)
    expected1 = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    assert len(result1) == len(
        expected1
    ), f"Failed for n=4, expected {len(expected1)} solutions, got {len(result1)}"
    for sol in expected1:
        assert sol in result1, f"Missing solution {sol} in result {result1}"

    # Test Case 2: n=1
    n2 = 1
    result2 = solution.solveNQueens(n2)
    expected2 = [["Q"]]
    assert result2 == expected2, f"Failed for n=1, expected {expected2}, got {result2}"

    # Test Case 3: n=2
    n3 = 2
    result3 = solution.solveNQueens(n3)
    assert result3 == [], f"Failed for n=2, expected [], got {result3}"

    # Test Case 4: n=3
    n4 = 3
    result4 = solution.solveNQueens(n4)
    assert result4 == [], f"Failed for n=3, expected [], got {result4}"

    # Test Case 5: n=5
    n5 = 5
    result5 = solution.solveNQueens(n5)
    expected5_count = 10  # Known solution count for n=5
    assert (
        len(result5) == expected5_count
    ), f"Failed for n=5, expected {expected5_count} solutions, got {len(result5)}"

    # Test Case 6: n=6
    n6 = 6
    result6 = solution.solveNQueens(n6)
    expected6_count = 4  # Known solution count for n=6
    assert (
        len(result6) == expected6_count
    ), f"Failed for n=6, expected {expected6_count} solutions, got {len(result6)}"

    # Test Case 7: n=7
    n7 = 7
    result7 = solution.solveNQueens(n7)
    expected7_count = 40  # Known solution count for n=7
    assert (
        len(result7) == expected7_count
    ), f"Failed for n=7, expected {expected7_count} solutions, got {len(result7)}"

    # Test Case 8: n=8
    n8 = 8
    result8 = solution.solveNQueens(n8)
    expected8_count = 92  # Known solution count for n=8
    assert (
        len(result8) == expected8_count
    ), f"Failed for n=8, expected {expected8_count} solutions, got {len(result8)}"

    # Verify all solutions are valid
    for n in [4, 5, 6, 7, 8]:
        result = solution.solveNQueens(n)
        for sol in result:
            # Check that each solution has n rows
            assert len(sol) == n, f"Solution has wrong number of rows: {len(sol)}"
            # Check that each row has n characters
            for row in sol:
                assert len(row) == n, f"Row has wrong length: {len(row)}"
            # Check that each row has exactly one 'Q'
            for row in sol:
                assert (
                    row.count("Q") == 1
                ), f"Row has wrong number of queens: {row.count('Q')}"
            # Check that queens don't attack each other
            queens = []
            for i, row in enumerate(sol):
                for j, char in enumerate(row):
                    if char == "Q":
                        queens.append((i, j))
            # Check no two queens are in same row, column, or diagonal
            for i in range(len(queens)):
                for j in range(i + 1, len(queens)):
                    r1, c1 = queens[i]
                    r2, c2 = queens[j]
                    assert r1 != r2, f"Queens in same row: {queens[i]}, {queens[j]}"
                    assert c1 != c2, f"Queens in same column: {queens[i]}, {queens[j]}"
                    assert abs(r1 - r2) != abs(
                        c1 - c2
                    ), f"Queens on same diagonal: {queens[i]}, {queens[j]}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    solution = Solution()

    # Test different input sizes
    test_sizes = [4, 5, 6]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        # Test approach
        start_time = time.time()
        result = solution.solveNQueens(size)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\t{len(result)} solutions")

    # Verify O(N!) complexity
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(N!) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(f"Expected ratios for O(N!): {[f'{r:.2f}x' for r in expected_ratios]}")

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance for factorial complexity
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(N!)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(N!) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(N!), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(N!)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    solution = Solution()

    print("\nTesting Edge Cases:")

    # Edge Case 1: Minimum constraint (n=1)
    result1 = solution.solveNQueens(1)
    assert result1 == [["Q"]], f"n=1 failed: {result1}"
    print(f"n=1: ✅")

    # Edge Case 2: Maximum constraint (n=9)
    result2 = solution.solveNQueens(9)
    assert len(result2) > 0, f"n=9 failed: {len(result2)} solutions"
    print(f"n=9: ✅")

    # Edge Case 3: No solution cases
    result3 = solution.solveNQueens(2)
    assert result3 == [], f"n=2 failed: {result3}"
    print(f"n=2 (no solution): ✅")

    result4 = solution.solveNQueens(3)
    assert result4 == [], f"n=3 failed: {result4}"
    print(f"n=3 (no solution): ✅")

    # Edge Case 4: Small board with solution
    result5 = solution.solveNQueens(4)
    assert len(result5) == 2, f"n=4 failed: {len(result5)} solutions"
    print(f"n=4 (has solution): ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    solution = Solution()

    print("\nBenchmarking N-Queens:")

    # Large dataset
    n = 8

    start_time = time.time()
    result = solution.solveNQueens(n)
    elapsed_time = time.time() - start_time

    print(f"Large dataset (n=8):")
    print(f"Time: {elapsed_time:.6f}s, Result: {len(result)} solutions")


if __name__ == "__main__":
    print("🧪 Testing N-Queens Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the solveNQueens method")
        print("- Aim for O(N!) time complexity")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(N!)")
        print("- Consider using backtracking with pruning")
