class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        adj = { i : [] for i in range(n)}
        visited = set()
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        queue = collections.deque()

        
        queue.append([0, -1])
        visited.add(0)

        while queue:
            node, prev = queue.popleft()
            for nei in adj[node]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                
                visited.add(nei)
                queue.append([nei, node])
        
        return len(visited) == n

