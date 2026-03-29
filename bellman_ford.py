#!/usr/bin/env python3
"""Bellman-Ford shortest path (handles negative weights). Zero dependencies."""

def bellman_ford(n, edges, source):
    """edges: list of (u, v, weight). Returns (dist, prev) or raises if negative cycle."""
    dist = [float("inf")] * n
    prev = [None] * n
    dist[source] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated: break
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Negative cycle detected")
    return dist, prev

def reconstruct_path(prev, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path)) if path else []

if __name__ == "__main__":
    edges = [(0,1,4),(0,2,2),(1,3,-3),(2,1,1),(2,3,5)]
    dist, prev = bellman_ford(4, edges, 0)
    print(f"Distances from 0: {dist}")
    print(f"Path to 3: {reconstruct_path(prev, 3)}")
