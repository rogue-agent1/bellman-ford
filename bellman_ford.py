#!/usr/bin/env python3
"""bellman_ford - Bellman-Ford shortest path (handles negative weights)."""
import sys
def bellman_ford(n,edges,src):
    dist=[float('inf')]*n;dist[src]=0;prev=[-1]*n
    for _ in range(n-1):
        for u,v,w in edges:
            if dist[u]+w<dist[v]:dist[v]=dist[u]+w;prev[v]=u
    for u,v,w in edges:
        if dist[u]+w<dist[v]:return None,None  # negative cycle
    return dist,prev
if __name__=="__main__":
    edges=[(0,1,4),(0,2,5),(1,2,-3),(2,3,4),(3,1,2)]
    dist,prev=bellman_ford(4,edges,0)
    if dist:
        for i,d in enumerate(dist):print(f"  0→{i}: {d}")
    else:print("Negative cycle detected!")
