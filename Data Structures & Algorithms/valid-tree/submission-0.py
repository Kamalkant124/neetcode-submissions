class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        hashMap = { i : [] for i in range(n)}
        visited = set()
        
        for u,v in edges:
            hashMap[u].append(v)
            hashMap[v].append(u)
        
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            
            for neighbour in hashMap[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visited)
