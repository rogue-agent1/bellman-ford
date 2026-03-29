from bellman_ford import bellman_ford, reconstruct_path
edges = [(0,1,4),(0,2,2),(1,3,-3),(2,1,1),(2,3,5)]
dist, prev = bellman_ford(4, edges, 0)
assert dist[0] == 0
assert dist[1] == 3  # 0->2->1 = 2+1
assert dist[3] == 0  # 0->2->1->3 = 2+1+(-3)
path = reconstruct_path(prev, 3)
assert path[0] == 0 and path[-1] == 3
# Negative cycle detection
try:
    bellman_ford(3, [(0,1,1),(1,2,-1),(2,0,-1)], 0)
    assert False, "Should raise"
except ValueError as e:
    assert "Negative cycle" in str(e)
print("bellman_ford tests passed")
