"""
Problem: Number of Islands (Grid DFS/BFS)
-----------------------------------------
Given an m x n grid of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Approach:
- Iterate all cells; when we see unvisited '1', do DFS/BFS to mark the whole island.
- Count how many times we start such a traversal.

Time: O(m*n) | Space: O(m*n) worst-case recursion/queue
"""
from typing import List

def num_islands(grid: List[List[str]]) -> int:
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    def dfs(r: int, c: int):
        stack = [(r,c)]
        while stack:
            x,y = stack.pop()
            if x<0 or x>=m or y<0 or y>=n or grid[x][y] != '1':
                continue
            grid[x][y] = '#'
            stack.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i,j)
    return count

def _test():
    g1 = [list("11110"),
          list("11010"),
          list("11000"),
          list("00000")]
    assert num_islands(g1) == 1
    g2 = [list("11000"),
          list("11000"),
          list("00100"),
          list("00011")]
    assert num_islands(g2) == 3
    assert num_islands([]) == 0

if __name__ == "__main__":
    _test()
    print("OK")