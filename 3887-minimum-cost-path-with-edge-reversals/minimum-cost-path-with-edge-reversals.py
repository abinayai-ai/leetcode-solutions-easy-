import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        incoming = defaultdict(list)
        
        # Build graph
        for u, v, w in edges:
            adj[u].append((v, w))          # normal edge
            incoming[v].append((u, w))     # for reversal
        
        # Distance array
        dist = [float('inf')] * n
        dist[0] = 0
        
        # Min-heap (cost, node)
        pq = [(0, 0)]
        
        while pq:
            cost, u = heapq.heappop(pq)
            
            # Skip if we already found a better path
            if cost > dist[u]:
                continue
            
            # 1️⃣ Normal edges
            for v, w in adj[u]:
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))
            
            # 2️⃣ Reversed incoming edges (use switch at u)
            for v, w in incoming[u]:
                if dist[v] > cost + 2 * w:
                    dist[v] = cost + 2 * w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist[n - 1] if dist[n - 1] != float('inf') else -1
