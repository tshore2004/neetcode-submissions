class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap.keys():
                
                j = hashmap[diff]
                return [j, i]
            else:
                hashmap[nums[i]] = i
            
