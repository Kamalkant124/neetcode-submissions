class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i in range(len(nums)):

            rem = target - nums[i]

            if rem in hashMap:
                return [hashMap[rem], i]
            
            hashMap[nums[i]] = i
        
        