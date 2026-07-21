class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0
        adj_list = self.getList(edges, n)
        visited = set()

        for node in adj_list:
            if self.explore(adj_list, node, visited):
                count += 1
        
        return count
    
    def explore(self, adj_list, current, visited):

        if current in visited:
            return False
        
        visited.add(current)

        for neighbour in adj_list[current]:
            self.explore(adj_list, neighbour, visited)
        
        return True
    
    def getList(self, edges, n):
        adj_list = {i: [] for i in range(n)}

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        return adj_list