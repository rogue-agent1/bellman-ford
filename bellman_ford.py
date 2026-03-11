#!/usr/bin/env python3
"""bellman_ford — Shortest paths with negative edge detection. Zero deps."""

def bellman_ford(n, edges, source):
    dist = [float('inf')] * n
    pred = [-1] * n
    dist[source] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
    # Negative cycle detection
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, None  # negative cycle
    return dist, pred

def reconstruct(pred, target):
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        cur = pred[cur]
    return path[::-1]

def main():
    edges = [(0,1,4),(0,2,5),(1,2,-3),(2,3,4),(3,1,2),(1,3,6)]
    n = 4
    dist, pred = bellman_ford(n, edges, 0)
    if dist is None:
        print("Negative cycle detected!")
    else:
        print("Bellman-Ford from node 0:")
        for i in range(n):
            path = reconstruct(pred, i)
            print(f"  -> {i}: dist={dist[i]}, path={path}")
    # Negative cycle example
    edges2 = [(0,1,1),(1,2,-1),(2,0,-1)]
    d2, _ = bellman_ford(3, edges2, 0)
    print(f"\nNegative cycle test: {'detected!' if d2 is None else 'none'}")

if __name__ == "__main__":
    main()
