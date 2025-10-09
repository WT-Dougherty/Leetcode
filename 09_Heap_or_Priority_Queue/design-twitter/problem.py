"""
Design Twitter - LeetCode Problem 355

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and see the 10 most recent tweets in the user's news feed.
"""

import time
import heapq
from typing import List


class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


def test_accuracy():
    """Test accuracy with various test cases"""
    twitter = Twitter()

    # Test Case 1: Basic functionality
    twitter.postTweet(1, 5)
    result1 = twitter.getNewsFeed(1)
    assert result1 == [5], f"Failed for basic post, expected [5], got {result1}"

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    result2 = twitter.getNewsFeed(1)
    assert result2 == [
        6,
        5,
    ], f"Failed for follow and post, expected [6, 5], got {result2}"

    twitter.unfollow(1, 2)
    result3 = twitter.getNewsFeed(1)
    assert result3 == [5], f"Failed for unfollow, expected [5], got {result3}"

    # Test Case 2: Multiple users and tweets
    twitter2 = Twitter()
    twitter2.postTweet(1, 1)
    twitter2.postTweet(1, 2)
    twitter2.postTweet(2, 3)
    twitter2.follow(1, 2)
    result4 = twitter2.getNewsFeed(1)
    assert set(result4) == {
        1,
        2,
        3,
    }, f"Failed for multiple tweets, expected {{1, 2, 3}}, got {set(result4)}"

    # Test Case 3: Self-following
    twitter3 = Twitter()
    twitter3.postTweet(1, 1)
    twitter3.follow(1, 1)
    result5 = twitter3.getNewsFeed(1)
    assert result5 == [1], f"Failed for self-following, expected [1], got {result5}"

    # Test Case 4: Empty news feed
    twitter4 = Twitter()
    result6 = twitter4.getNewsFeed(1)
    assert result6 == [], f"Failed for empty news feed, expected [], got {result6}"

    # Test Case 5: Maximum tweets (10)
    twitter5 = Twitter()
    for i in range(15):
        twitter5.postTweet(1, i)
    result7 = twitter5.getNewsFeed(1)
    assert len(result7) == 10, f"Failed for max tweets, expected 10, got {len(result7)}"

    # Test Case 6: Unfollow non-existent user
    twitter6 = Twitter()
    twitter6.postTweet(1, 1)
    twitter6.unfollow(1, 2)  # User 2 doesn't exist
    result8 = twitter6.getNewsFeed(1)
    assert result8 == [
        1
    ], f"Failed for unfollow non-existent, expected [1], got {result8}"

    # Test Case 7: Multiple follows
    twitter7 = Twitter()
    twitter7.postTweet(1, 1)
    twitter7.postTweet(2, 2)
    twitter7.postTweet(3, 3)
    twitter7.follow(1, 2)
    twitter7.follow(1, 3)
    result9 = twitter7.getNewsFeed(1)
    assert set(result9) == {
        1,
        2,
        3,
    }, f"Failed for multiple follows, expected {{1, 2, 3}}, got {set(result9)}"

    print("✅ All accuracy tests passed!")


def test_time_complexity():
    """Test time complexity with different input sizes - FAILS if worse than expected"""
    # Test different input sizes
    test_sizes = [100, 1000, 5000]
    times = []

    print("\nTime Complexity Analysis:")
    print("Size\tTime\t\tResult")
    print("-" * 40)

    for size in test_sizes:
        twitter = Twitter()

        # Test approach - measure time for operations
        start_time = time.time()

        # Post tweets
        for i in range(size):
            twitter.postTweet(1, i)

        # Follow users
        for i in range(2, min(size // 10 + 2, 100)):  # Follow up to 100 users
            twitter.follow(1, i)

        # Get news feed multiple times
        for _ in range(size // 10):
            twitter.getNewsFeed(1)

        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"{size}\t{elapsed_time:.6f}s\tOperations completed")

    # Verify O(n log k) complexity for getNewsFeed
    if len(times) >= 2:
        # Calculate ratios between consecutive time measurements
        ratios = []
        for i in range(1, len(times)):
            ratio = times[i] / times[i - 1]
            ratios.append(ratio)

        # Calculate expected ratios for O(n log k) complexity
        expected_ratios = []
        for i in range(1, len(test_sizes)):
            expected_ratio = test_sizes[i] / test_sizes[i - 1]
            expected_ratios.append(expected_ratio)

        print(f"\nTime ratios: {[f'{r:.2f}x' for r in ratios]}")
        print(
            f"Expected ratios for O(n log k): {[f'{r:.2f}x' for r in expected_ratios]}"
        )

        # Check if ratios are within acceptable range
        tolerance = 1.0  # Allow 100% variance
        for i, (actual, expected) in enumerate(zip(ratios, expected_ratios)):
            min_expected = expected * (1 - tolerance)
            max_expected = expected * (1 + tolerance)

            if not (actual <= max_expected):
                print(f"\n❌ FAILED: Time complexity appears worse than O(n log k)")
                print(
                    f"   Size {test_sizes[i]} to {test_sizes[i+1]}: expected ~{expected:.2f}x, got {actual:.2f}x"
                )
                print(f"   This suggests worse than O(n log k) complexity")
                raise AssertionError(
                    f"Time complexity test failed: expected O(n log k), but got worse complexity"
                )

        print(f"\n✅ PASSED: Time complexity appears to be O(n log k)")
        return True
    else:
        print(f"\n⚠️  Not enough data points to verify complexity")
        return True


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\nTesting Edge Cases:")

    # Edge Case 1: Single user, single tweet
    twitter1 = Twitter()
    twitter1.postTweet(1, 1)
    result1 = twitter1.getNewsFeed(1)
    assert result1 == [1], f"Single user tweet failed: {result1}"
    print(f"Single user tweet: ✅")

    # Edge Case 2: Maximum constraint values
    twitter2 = Twitter()
    twitter2.postTweet(500, 10000)
    result2 = twitter2.getNewsFeed(500)
    assert result2 == [10000], f"Max constraint values failed: {result2}"
    print(f"Maximum constraint values: ✅")

    # Edge Case 3: Many follows
    twitter3 = Twitter()
    for i in range(2, 52):  # Follow 50 users
        twitter3.postTweet(i, i)
        twitter3.follow(1, i)
    twitter3.postTweet(1, 1)
    result3 = twitter3.getNewsFeed(1)
    assert len(result3) == 10, f"Many follows failed: expected 10, got {len(result3)}"
    print(f"Many follows: ✅")

    # Edge Case 4: Rapid follow/unfollow
    twitter4 = Twitter()
    twitter4.postTweet(1, 1)
    twitter4.postTweet(2, 2)
    for _ in range(100):
        twitter4.follow(1, 2)
        twitter4.unfollow(1, 2)
    result4 = twitter4.getNewsFeed(1)
    assert result4 == [1], f"Rapid follow/unfollow failed: {result4}"
    print(f"Rapid follow/unfollow: ✅")

    print("✅ All edge case tests passed!")


def benchmark_solution():
    """Benchmark the solution with large datasets"""
    print("\nBenchmarking Twitter Operations:")

    # Large dataset
    twitter = Twitter()

    start_time = time.time()
    # Post many tweets
    for i in range(10000):
        twitter.postTweet(1, i)

    # Follow many users
    for i in range(2, 100):
        twitter.postTweet(i, i * 1000)
        twitter.follow(1, i)

    # Get news feed multiple times
    for _ in range(100):
        twitter.getNewsFeed(1)

    total_time = time.time() - start_time
    print(f"Large dataset (10,000 tweets, 98 follows, 100 news feeds):")
    print(f"Time: {total_time:.6f}s")


if __name__ == "__main__":
    print("🧪 Testing Design Twitter Problem")
    print("=" * 50)

    # Run all tests
    test_accuracy()
    test_edge_cases()
    complexity_passed = test_time_complexity()
    benchmark_solution()

    if complexity_passed:
        print("\n🎉 All tests completed successfully!")
        print("\nSummary:")
        print("- Implement your solution in the Twitter class methods")
        print("- Aim for O(1) for postTweet, follow, unfollow")
        print("- Aim for O(k log n) for getNewsFeed where k=10")
        print("- Handle all edge cases correctly")
    else:
        print("\n❌ Tests failed - improve your solution's time complexity!")
        print("- Your solution appears to be worse than O(n log k)")
        print("- Consider using heaps for efficient news feed retrieval")
