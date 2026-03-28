#!/usr/bin/env python3
"""Bellman-Ford — shortest paths with negative edge detection."""
import sys
def bellman_ford(n, edges, start):
    dist = [float("inf")] * n; dist[start] = 0; prev = [None]*n
    for _ in range(n-1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]: dist[v] = dist[u] + w; prev[v] = u
    for u, v, w in edges:
        if dist[u] + w < dist[v]: return None, None  # negative cycle
    return dist, prev
def path(prev, start, end):
    p = []; n = end
    while n is not None and n != start: p.append(n); n = prev[n]
    if n == start: p.append(start)
    return list(reversed(p))
def cli():
    edges = [(0,1,4),(0,2,5),(1,2,-3),(2,3,4),(3,1,2)]
    dist, prev = bellman_ford(4, edges, 0)
    if dist is None: print("  Negative cycle detected!"); return
    print("  From node 0:")
    for i in range(4): print(f"    → {i}: dist={dist[i]} path={path(prev,0,i)}")
if __name__ == "__main__": cli()
