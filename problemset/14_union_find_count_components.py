"""
Problem: Count Connected Components (Union-Find / DSU)
-----------------------------------------------------
Given `n` nodes labeled 0..n-1 and a list of undirected edges, return the number of connected components.

Approach (Disjoint Set Union):
- Initialize parent and size.
- Union for each edge.
- The number of components is the number of unique roots.

Time: O(n α(n)) ~ almost O(n) | Space: O(n)
"""
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1]*n
        self.count = n
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1

def count_components(n: int, edges: List[List[int]]) -> int:
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.count

def _test():
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2
    assert count_components(5, [[0,1],[1,2],[2,3],[3,4]]) == 1
    assert count_components(4, []) == 4

if __name__ == "__main__":
    _test()
    print("OK")