import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []
        current_time = 0

        for j, task in enumerate(tasks):
            current_time = max(current_time, j)

            while busy and busy[0][0] <= current_time:
                t, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            if not free:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    t, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            ans.append(i)

            heapq.heappush(busy, (current_time + task, w, i))

        return ans