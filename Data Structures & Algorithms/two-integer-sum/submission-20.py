class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        
        while count < len(nums):
            i = nums[count]
            
            for t in range(count + 1, len(nums)):
                j = nums[t]
                if i + j == target:
                    return [count, t]


            count += 1
        return []
        