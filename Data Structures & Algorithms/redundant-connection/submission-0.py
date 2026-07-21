class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = {i : [] for i in range(n + 1)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        def dfs(node, prev):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True

            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)
        
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]

        return []
        