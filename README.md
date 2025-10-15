# NeetCode 150 — Checklist & Table of Contents

_Total problems: **151**_

> Check items as you complete them. Each link opens that problem’s `problem.md` inside this repo.

## Arrays And Hashing (9)

- [x] [Contains Duplicate](01_Arrays_And_Hashing/contains-duplicate/problem.md)
- [x] [Valid Anagram](01_Arrays_And_Hashing/valid-anagram/problem.md)
- [x] [Two Sum](01_Arrays_And_Hashing/two-sum/problem.md)
- [x] [Group Anagrams](01_Arrays_And_Hashing/group-anagrams/problem.md)
- [x] [Top K Frequent Elements](01_Arrays_And_Hashing/top-k-frequent-elements/problem.md)
- [x] [Product of Array Except Self](01_Arrays_And_Hashing/product-of-array-except-self/problem.md)
- [x] [Valid Sudoku](01_Arrays_And_Hashing/valid-sudoku/problem.md)
- [x] [Encode And Decode Strings](01_Arrays_And_Hashing/encode-and-decode-strings/problem.md)
- [x] [Longest Consecutive Sequence](01_Arrays_And_Hashing/longest-consecutive-sequence/problem.md)

_Some Notes on This Section:_
Hash maps provide constant time element lookup; you can check that you have come across specific elements in constant time. If counting element frequency, use a hash map. If you're checking element existence, use a set (also hashed elements, so constant time lookup)

## Two Pointers (5)

- [x] [Valid Palindrome](02_Two_Pointers/valid-palindrome/problem.md)
- [x] [Two Sum II Input Array Is Sorted](02_Two_Pointers/two-sum-ii-input-array-is-sorted/problem.md)
- [x] [3Sum](02_Two_Pointers/3sum/problem.md)
- [x] [Container With Most Water](02_Two_Pointers/container-with-most-water/problem.md)
- [x] [Trapping Rain Water](02_Two_Pointers/trapping-rain-water/problem.md)

_Some Notes on This Section:_
I had some real trouble with the Trapping Rain Water problem. My first algorithm, which was faulty, initialized both pointers to the start of the array. I thought: I should find the left and right edges of the buckets and calculate the internal volume. This required that I calculate sub-array sums & create more variables. Also, the logic was overly complicated.

I questioned whether I should solve the problem vertically or horizontally. Vertically would mean calculating the area of a single _unit-wide_ slice of the array. Horizontally would mean calculating the area of a _unit-tall_ slice of the array. My first algorithm settled somewhere in-between: calculate total sum of the largest bucket and subtract the internal elevations.

I tried to start by defining a bucket- I concluded that a bucket is defined by two conditions: for all elevations ele in range (left, right), ele < elevation @ left && ele < elevation @ right. This is a sound definition of a bucket. What I didn't consider: when I advance ptrs iff the opposite ptr has seen a height >= the ptr's maximum observed height, I guaruntee that any drop in elevation is contained within some bucket.

With this approach in mind, it's best to redefine a bucket: a bucket occurs when there exists some elevation ele in range (left, right) s.t. ele < elevation @ left && ele < elevation @ right. When we prioritize making the bucket edges taller as quickly as possible, we catch all these existing elevations.

When I changed my bucket definition from a more restrictive "for all" predicate to the looser "there exists" predicate, the problem simplified significantly. I'll be keeping this in mind going forward.

It's strange and initially counterintuitive to come at this problem from the left and right sides, but redefining a bucket brings some clarity to the problem.

Another note: every two-pointer problem starts with left & right ptrs at the left and right sides of the iterable object. I'll seek solutions of this form going forward.

## Sliding Window (6)

- [x] [Best Time to Buy And Sell Stock](03_Sliding_Window/best-time-to-buy-and-sell-stock/problem.md)
- [ ] [Longest Substring Without Repeating Characters](03_Sliding_Window/longest-substring-without-repeating-characters/problem.md)
- [ ] [Longest Repeating Character Replacement](03_Sliding_Window/longest-repeating-character-replacement/problem.md)
- [ ] [Permutation In String](03_Sliding_Window/permutation-in-string/problem.md)
- [ ] [Minimum Window Substring](03_Sliding_Window/minimum-window-substring/problem.md)
- [ ] [Sliding Window Maximum](03_Sliding_Window/sliding-window-maximum/problem.md)

## Stack (7)

- [ ] [Valid Parentheses](04_Stack/valid-parentheses/problem.md)
- [ ] [Min Stack](04_Stack/min-stack/problem.md)
- [ ] [Evaluate Reverse Polish Notation](04_Stack/evaluate-reverse-polish-notation/problem.md)
- [ ] [Generate Parentheses](04_Stack/generate-parentheses/problem.md)
- [ ] [Daily Temperatures](04_Stack/daily-temperatures/problem.md)
- [ ] [Car Fleet](04_Stack/car-fleet/problem.md)
- [ ] [Largest Rectangle In Histogram](04_Stack/largest-rectangle-in-histogram/problem.md)

## Binary Search (7)

- [ ] [Binary Search](05_Binary_Search/binary-search/problem.md)
- [ ] [Search a 2D Matrix](05_Binary_Search/search-a-2d-matrix/problem.md)
- [ ] [Koko Eating Bananas](05_Binary_Search/koko-eating-bananas/problem.md)
- [ ] [Search In Rotated Sorted Array](05_Binary_Search/search-in-rotated-sorted-array/problem.md)
- [ ] [Find Minimum In Rotated Sorted Array](05_Binary_Search/find-minimum-in-rotated-sorted-array/problem.md)
- [ ] [Time Based Key Value Store](05_Binary_Search/time-based-key-value-store/problem.md)
- [ ] [Median of Two Sorted Arrays](05_Binary_Search/median-of-two-sorted-arrays/problem.md)

## Linked List (11)

- [ ] [Reverse Linked List](06_Linked_List/reverse-linked-list/problem.md)
- [ ] [Merge Two Sorted Lists](06_Linked_List/merge-two-sorted-lists/problem.md)
- [ ] [Reorder List](06_Linked_List/reorder-list/problem.md)
- [ ] [Remove Nth Node From End of List](06_Linked_List/remove-nth-node-from-end-of-list/problem.md)
- [ ] [Copy List With Random Pointer](06_Linked_List/copy-list-with-random-pointer/problem.md)
- [ ] [Add Two Numbers](06_Linked_List/add-two-numbers/problem.md)
- [ ] [Linked List Cycle](06_Linked_List/linked-list-cycle/problem.md)
- [ ] [Find The Duplicate Number](06_Linked_List/find-the-duplicate-number/problem.md)
- [ ] [LRU Cache](06_Linked_List/lru-cache/problem.md)
- [ ] [Merge K Sorted Lists](06_Linked_List/merge-k-sorted-lists/problem.md)
- [ ] [Reverse Nodes In K Group](06_Linked_List/reverse-nodes-in-k-group/problem.md)

## Trees (15)

- [ ] [Invert Binary Tree](07_Trees/invert-binary-tree/problem.md)
- [ ] [Maximum Depth of Binary Tree](07_Trees/maximum-depth-of-binary-tree/problem.md)
- [ ] [Diameter of Binary Tree](07_Trees/diameter-of-binary-tree/problem.md)
- [ ] [Balanced Binary Tree](07_Trees/balanced-binary-tree/problem.md)
- [ ] [Same Tree](07_Trees/same-tree/problem.md)
- [ ] [Subtree of Another Tree](07_Trees/subtree-of-another-tree/problem.md)
- [ ] [Lowest Common Ancestor of a Binary Search Tree](07_Trees/lowest-common-ancestor-of-a-binary-search-tree/problem.md)
- [ ] [Binary Tree Level Order Traversal](07_Trees/binary-tree-level-order-traversal/problem.md)
- [ ] [Binary Tree Right Side View](07_Trees/binary-tree-right-side-view/problem.md)
- [ ] [Count Good Nodes In Binary Tree](07_Trees/count-good-nodes-in-binary-tree/problem.md)
- [ ] [Validate Binary Search Tree](07_Trees/validate-binary-search-tree/problem.md)
- [ ] [Kth Smallest Element In a Bst](07_Trees/kth-smallest-element-in-a-bst/problem.md)
- [ ] [Construct Binary Tree From Preorder And Inorder Traversal](07_Trees/construct-binary-tree-from-preorder-and-inorder-traversal/problem.md)
- [ ] [Binary Tree Maximum Path Sum](07_Trees/binary-tree-maximum-path-sum/problem.md)
- [ ] [Serialize And Deserialize Binary Tree](07_Trees/serialize-and-deserialize-binary-tree/problem.md)

## Tries (3)

- [ ] [Implement Trie Prefix Tree](08_Tries/implement-trie-prefix-tree/problem.md)
- [ ] [Design Add And Search Words Data Structure](08_Tries/design-add-and-search-words-data-structure/problem.md)
- [ ] [Word Search II](08_Tries/word-search-ii/problem.md)

## Heap / Priority Queue (7)

- [ ] [Kth Largest Element In a Stream](09_Heap_or_Priority_Queue/kth-largest-element-in-a-stream/problem.md)
- [ ] [Last Stone Weight](09_Heap_or_Priority_Queue/last-stone-weight/problem.md)
- [ ] [K Closest Points to Origin](09_Heap_or_Priority_Queue/k-closest-points-to-origin/problem.md)
- [ ] [Kth Largest Element In An Array](09_Heap_or_Priority_Queue/kth-largest-element-in-an-array/problem.md)
- [ ] [Task Scheduler](09_Heap_or_Priority_Queue/task-scheduler/problem.md)
- [ ] [Design Twitter](09_Heap_or_Priority_Queue/design-twitter/problem.md)
- [ ] [Find Median From Data Stream](09_Heap_or_Priority_Queue/find-median-from-data-stream/problem.md)

## Backtracking (9)

- [ ] [Subsets](10_Backtracking/subsets/problem.md)
- [ ] [Combination Sum](10_Backtracking/combination-sum/problem.md)
- [ ] [Permutations](10_Backtracking/permute/problem.md)
- [ ] [Subsets II](10_Backtracking/subsets-ii/problem.md)
- [ ] [Combination Sum II](10_Backtracking/combination-sum-ii/problem.md)
- [ ] [Word Search](10_Backtracking/word-search/problem.md)
- [ ] [Palindrome Partitioning](10_Backtracking/palindrome-partitioning/problem.md)
- [ ] [Letter Combinations of a Phone Number](10_Backtracking/letter-combinations-of-a-phone-number/problem.md)
- [ ] [N Queens](10_Backtracking/n-queens/problem.md)

## Graphs (13)

- [ ] [Number of Islands](11_Graphs/number-of-islands/problem.md)
- [ ] [Clone Graph](11_Graphs/clone-graph/problem.md)
- [ ] [Max Area of Island](11_Graphs/max-area-of-island/problem.md)
- [ ] [Pacific Atlantic Water Flow](11_Graphs/pacific-atlantic-water-flow/problem.md)
- [ ] [Surrounded Regions](11_Graphs/surrounded-regions/problem.md)
- [ ] [Rotting Oranges](11_Graphs/rotting-oranges/problem.md)
- [ ] [Walls And Gates](11_Graphs/walls-and-gates/problem.md)
- [ ] [Course Schedule](11_Graphs/course-schedule/problem.md)
- [ ] [Course Schedule II](11_Graphs/course-schedule-ii/problem.md)
- [ ] [Redundant Connection](11_Graphs/redundant-connection/problem.md)
- [ ] [Number of Connected Components In An Undirected Graph](11_Graphs/number-of-connected-components-in-an-undirected-graph/problem.md)
- [ ] [Graph Valid Tree](11_Graphs/graph-valid-tree/problem.md)
- [ ] [Word Ladder](11_Graphs/word-ladder/problem.md)

## Advanced Graphs (6)

- [ ] [Reconstruct Itinerary](12_Advanced_Graphs/reconstruct-itinerary/problem.md)
- [ ] [Min Cost to Connect All Points](12_Advanced_Graphs/min-cost-to-connect-all-points/problem.md)
- [ ] [Network Delay Time](12_Advanced_Graphs/network-delay-time/problem.md)
- [ ] [Swim In Rising Water](12_Advanced_Graphs/swim-in-rising-water/problem.md)
- [ ] [Alien Dictionary](12_Advanced_Graphs/alien-dictionary/problem.md)
- [ ] [Cheapest Flights Within K Stops](12_Advanced_Graphs/cheapest-flights-within-k-stops/problem.md)

## 1D Dynamic Programming (12)

- [ ] [Climbing Stairs](13_1D_Dynamic_Programming/climbing-stairs/problem.md)
- [ ] [Min Cost Climbing Stairs](13_1D_Dynamic_Programming/min-cost-climbing-stairs/problem.md)
- [ ] [House Robber](13_1D_Dynamic_Programming/house-robber/problem.md)
- [ ] [House Robber II](13_1D_Dynamic_Programming/house-robber-ii/problem.md)
- [ ] [Longest Palindromic Substring](13_1D_Dynamic_Programming/longest-palindromic-substring/problem.md)
- [ ] [Palindromic Substrings](13_1D_Dynamic_Programming/palindromic-substrings/problem.md)
- [ ] [Decode Ways](13_1D_Dynamic_Programming/decode-ways/problem.md)
- [ ] [Coin Change](13_1D_Dynamic_Programming/coin-change/problem.md)
- [ ] [Maximum Product Subarray](13_1D_Dynamic_Programming/maximum-product-subarray/problem.md)
- [ ] [Word Break](13_1D_Dynamic_Programming/word-break/problem.md)
- [ ] [Longest Increasing Subsequence](13_1D_Dynamic_Programming/longest-increasing-subsequence/problem.md)
- [ ] [Partition Equal Subset Sum](13_1D_Dynamic_Programming/partition-equal-subset-sum/problem.md)

## 2D Dynamic Programming (11)

- [ ] [Unique Paths](14_2D_Dynamic_Programming/unique-paths/problem.md)
- [ ] [Longest Common Subsequence](14_2D_Dynamic_Programming/longest-common-subsequence/problem.md)
- [ ] [Best Time to Buy And Sell Stock With Cooldown](14_2D_Dynamic_Programming/best-time-to-buy-and-sell-stock-with-cooldown/problem.md)
- [ ] [Coin Change II](14_2D_Dynamic_Programming/coin-change-ii/problem.md)
- [ ] [Target Sum](14_2D_Dynamic_Programming/target-sum/problem.md)
- [ ] [Interleaving String](14_2D_Dynamic_Programming/interleaving-string/problem.md)
- [ ] [Longest Increasing Path In a Matrix](14_2D_Dynamic_Programming/longest-increasing-path-in-a-matrix/problem.md)
- [ ] [Distinct Subsequences](14_2D_Dynamic_Programming/distinct-subsequences/problem.md)
- [ ] [Edit Distance](14_2D_Dynamic_Programming/edit-distance/problem.md)
- [ ] [Burst Balloons](14_2D_Dynamic_Programming/burst-balloons/problem.md)
- [ ] [Regular Expression Matching](14_2D_Dynamic_Programming/regular-expression-matching/problem.md)

## Greedy (8)

- [ ] [Maximum Subarray](15_Greedy/maximum-subarray/problem.md)
- [ ] [Jump Game](15_Greedy/jump-game/problem.md)
- [ ] [Jump Game II](15_Greedy/jump-game-ii/problem.md)
- [ ] [Gas Station](15_Greedy/gas-station/problem.md)
- [ ] [Hand of Straights](15_Greedy/hand-of-straights/problem.md)
- [ ] [Merge Triplets to Form Target Triplet](15_Greedy/merge-triplets-to-form-target-triplet/problem.md)
- [ ] [Partition Labels](15_Greedy/partition-labels/problem.md)
- [ ] [Valid Parenthesis String](15_Greedy/valid-parenthesis-string/problem.md)

## Intervals (6)

- [ ] [Insert Interval](16_Intervals/insert-interval/problem.md)
- [ ] [Merge Intervals](16_Intervals/merge-intervals/problem.md)
- [ ] [Non Overlapping Intervals](16_Intervals/non-overlapping-intervals/problem.md)
- [ ] [Meeting Rooms](16_Intervals/meeting-rooms/problem.md)
- [ ] [Meeting Rooms II](16_Intervals/meeting-rooms-ii/problem.md)
- [ ] [Minimum Interval to Include Each Query](16_Intervals/minimum-interval-to-include-each-query/problem.md)

## Math & Geometry (8)

- [ ] [Rotate Image](17_Math_&_Geometry/rotate-image/problem.md)
- [ ] [Spiral Matrix](17_Math_&_Geometry/spiral-matrix/problem.md)
- [ ] [Set Matrix Zeroes](17_Math_&_Geometry/set-matrix-zeroes/problem.md)
- [ ] [Happy Number](17_Math_&_Geometry/happy-number/problem.md)
- [ ] [Plus One](17_Math_&_Geometry/plus-one/problem.md)
- [ ] [Multiply Strings](17_Math_&_Geometry/multiply-strings/problem.md)
- [ ] [Detect Squares](17_Math_&_Geometry/detect-squares/problem.md)

## Bit Manipulation (9)

- [ ] [Number of 1 Bits](18_Bit_Manipulation/number-of-1-bits/problem.md)
- [ ] [Counting Bits](18_Bit_Manipulation/counting-bits/problem.md)
- [ ] [Reverse Bits](18_Bit_Manipulation/reverse-bits/problem.md)
- [ ] [Missing Number](18_Bit_Manipulation/missing-number/problem.md)
- [ ] [Sum of Two Integers](18_Bit_Manipulation/sum-of-two-integers/problem.md)
- [ ] [Reverse Integer](18_Bit_Manipulation/reverse-integer/problem.md)
- [ ] [Single Number](18_Bit_Manipulation/single-number/problem.md)
- [ ] [Single Number II](18_Bit_Manipulation/single-number-ii/problem.md)
- [ ] [Bitwise AND of Numbers Range](18_Bit_Manipulation/bitwise-and-of-numbers-range/problem.md)
