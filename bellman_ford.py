#!/usr/bin/env python3
"""Bellman-Ford shortest path (handles negative weights)."""
import sys,json
def bellman_ford(n,edges,src):
    dist=[float('inf')]*n;dist[src]=0;prev=[-1]*n
    for _ in range(n-1):
        for u,v,w in edges:
            if dist[u]+w<dist[v]: dist[v]=dist[u]+w;prev[v]=u
    for u,v,w in edges:
        if dist[u]+w<dist[v]: return None,None  # negative cycle
    return dist,prev
def main():
    if "--demo" in sys.argv:
        edges=[(0,1,4),(0,2,5),(1,2,-3),(2,3,4),(3,1,2)]
        dist,prev=bellman_ford(4,edges,0)
        if dist:
            for i,d in enumerate(dist): print(f"  0→{i}: {d}")
        else: print("Negative cycle detected!")
        print("\nWith negative cycle:")
        edges2=[(0,1,1),(1,2,-1),(2,0,-1)]
        d2,_=bellman_ford(3,edges2,0)
        print("  Negative cycle!" if d2 is None else d2)
    else:
        d=json.loads(sys.stdin.read())
        dist,_=bellman_ford(d["n"],d["edges"],d["src"])
        print(json.dumps(dist))
if __name__=="__main__": main()
