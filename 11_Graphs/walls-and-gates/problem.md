# Walls and Gates

## Problem Description

You are given an m x n grid rooms initialized with these three possible values:

- -1 A wall or an obstacle.
- 0 A gate.
- INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should remain INF.

## Examples

### Example 1:

```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

### Example 2:

```
Input: rooms = [[-1]]
Output: [[-1]]
```

### Example 3:

```
Input: rooms = [[2147483647]]
Output: [[2147483647]]
```

## Constraints

- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is either -1, 0, or 2^31 - 1.

## Desired Time Complexity

- **Time Complexity**: O(m \* n) where m and n are the dimensions of the grid
- **Space Complexity**: O(m \* n) for the queue in the worst case
