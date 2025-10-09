# Min Cost to Connect All Points

## Problem Description

You are given an array of points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Examples

### Example 1:

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

### Example 2:

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

### Example 3:

```
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
```

## Constraints

- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.

## Desired Time Complexity

- **Time Complexity**: O(n^2 \* log n) where n is the number of points
- **Space Complexity**: O(n^2) for the adjacency list
