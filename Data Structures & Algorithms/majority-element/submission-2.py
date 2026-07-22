class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majElement = 0 

        for i in range(len(nums)):
            
            if count == 0:
                count = 1
                majElement = nums[i]
            
            if nums[i] != majElement:
                count -= 1
            else:
                count += 1
        
        return majElement