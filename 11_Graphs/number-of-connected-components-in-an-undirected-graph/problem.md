# Number of Connected Components in an Undirected Graph

## Problem Description

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return the number of connected components in the graph.

## Examples

### Example 1:

```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

### Example 2:

```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

## Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

## Desired Time Complexity

- **Time Complexity**: O(V + E) where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(V + E) for the adjacency list and visited array
