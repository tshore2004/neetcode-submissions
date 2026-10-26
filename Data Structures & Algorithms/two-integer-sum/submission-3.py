class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        
        result = []

        for i,n in enumerate(nums):
            diff = target-n
            if diff in prev:
                result = [prev[diff], i]
                return result
            prev[n] = i
        return
    