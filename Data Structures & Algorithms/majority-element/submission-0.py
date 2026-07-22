class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i],0)
        
        for key, value in hashMap.items():
            if value > len(nums) / 2:
                return key
        
        return 0