from collections import defaultdict
import math

class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        
        # Group rules by length
        by_len = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            by_len[len(o)].append((o, c, w))
        
        # For each length, build APSP (Floyd-Warshall)
        dist_maps = {}  # length -> {u: {v: min_cost}}
        
        for L, rules in by_len.items():
            nodes = set()
            for o, c, _ in rules:
                nodes.add(o)
                nodes.add(c)
            
            nodes = list(nodes)
            idx = {s: i for i, s in enumerate(nodes)}
            m = len(nodes)
            
            # Init distance matrix
            dist = [[math.inf] * m for _ in range(m)]
            for i in range(m):
                dist[i][i] = 0
            
            # Direct edges
            for o, c, w in rules:
                i, j = idx[o], idx[c]
                dist[i][j] = min(dist[i][j], w)
            
            # Floyd–Warshall
            for k in range(m):
                for i in range(m):
                    if dist[i][k] == math.inf:
                        continue
                    for j in range(m):
                        if dist[k][j] == math.inf:
                            continue
                        new_cost = dist[i][k] + dist[k][j]
                        if new_cost < dist[i][j]:
                            dist[i][j] = new_cost
            
            # Store as dict-of-dicts for easy lookup
            dmap = {u: {} for u in nodes}
            for i, u in enumerate(nodes):
                for j, v in enumerate(nodes):
                    if dist[i][j] < math.inf:
                        dmap[u][v] = dist[i][j]
            
            dist_maps[L] = dmap
        
        # DP
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == math.inf:
                continue
            
            # Case 1: single char already matches
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case 2: try all rule lengths
            for L, dmap in dist_maps.items():
                j = i + L
                if j > n:
                    continue
                
                s_sub = source[i:j]
                t_sub = target[i:j]
                
                if s_sub == t_sub:
                    dp[j] = min(dp[j], dp[i])
                    continue
                
                if s_sub in dmap and t_sub in dmap[s_sub]:
                    dp[j] = min(dp[j], dp[i] + dmap[s_sub][t_sub])
        
        return -1 if dp[n] == math.inf else dp[n]
