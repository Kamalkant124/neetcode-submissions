class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        for crs in range(numCourses):
            if not self.dfs(numCourses, crs, preMap, visited):
                return False
        
        return True
    
    def dfs(self, numCourses, crs, preMap, visited):
        if crs in visited:
            return False
        
        if preMap[crs] == []:
            return True
        
        visited.add(crs)

        for prereq in preMap[crs]:
            if not self.dfs(numCourses, prereq, preMap, visited):
                return False
        visited.remove(crs)
        preMap[crs] = []
        return True