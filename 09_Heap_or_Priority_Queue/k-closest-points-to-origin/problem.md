# K Closest Points to Origin

## Problem Description

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √((x1 - x2)2 + (y1 - y2)2)).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Examples

### Example 1:

```
Input: points = [[1,1],[2,2],[3,3]], k = 1
Output: [[1,1]]
Explanation:
The distance between (1, 1) and the origin is sqrt(2).
The distance between (2, 2) and the origin is sqrt(8).
The distance between (3, 3) and the origin is sqrt(18).
Since sqrt(2) < sqrt(8) < sqrt(18), the closest point to the origin is (1, 1).
```

### Example 2:

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## Constraints

- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

## Desired Time Complexity

- **Time Complexity**: O(n log k) where n is the number of points
- **Space Complexity**: O(k) for the heap
