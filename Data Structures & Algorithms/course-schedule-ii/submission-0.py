class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = { c : [] for c in range(numCourses)}
        visited, cycle = set(), set()

        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        
        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)
            
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
        