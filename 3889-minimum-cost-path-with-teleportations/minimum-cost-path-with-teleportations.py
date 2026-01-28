import heapq

class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        INF = 10**18
        
        dist = [[[INF] * n for _ in range(m)] for _ in range(k + 1)]
        dist[0][0][0] = 0
        
        pq = [(0, 0, 0, 0)]  # cost, row, col, teleports_used
        
        cells = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        activated_ptr = [0] * (k + 1)
        
        while pq:
            cost, i, j, t = heapq.heappop(pq)
            
            if cost > dist[t][i][j]:
                continue
            
            # Normal moves
            if j + 1 < n:
                new_cost = cost + grid[i][j + 1]
                if new_cost < dist[t][i][j + 1]:
                    dist[t][i][j + 1] = new_cost
                    heapq.heappush(pq, (new_cost, i, j + 1, t))
            
            if i + 1 < m:
                new_cost = cost + grid[i + 1][j]
                if new_cost < dist[t][i + 1][j]:
                    dist[t][i + 1][j] = new_cost
                    heapq.heappush(pq, (new_cost, i + 1, j, t))
            
            # Teleport
            if t < k:
                while (activated_ptr[t] < m * n and
                       cells[activated_ptr[t]][0] <= grid[i][j]):
                    _, x, y = cells[activated_ptr[t]]
                    if cost < dist[t + 1][x][y]:
                        dist[t + 1][x][y] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    activated_ptr[t] += 1
        
        return min(dist[t][m - 1][n - 1] for t in range(k + 1))

