class Solution(object):

  def remainingMethods(self, n, k, invocations):
    # Step 1: Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in invocations:
      adj[u].append(v)

    # Step 2: Find all suspicious methods using BFS
    suspicious = [False] * n
    suspicious[k] = True
    queue = [k]

    while queue:
      curr = queue.pop(0)
      for neighbor in adj[curr]:
        if not suspicious[neighbor]:
          suspicious[neighbor] = True
          queue.append(neighbor)

    # Step 3: Check if any non-suspicious method invokes a suspicious method
    for u, v in invocations:
      if not suspicious[u] and suspicious[v]:
        return list(range(n))

    # Step 4: Return remaining non-suspicious methods
    return [i for i in range(n) if not suspicious[i]]