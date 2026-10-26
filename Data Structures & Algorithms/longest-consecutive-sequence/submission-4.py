class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        count = 1
        max_len = 0
        for i in lookup:
            if i-1 not in lookup:
                start = i
                print (start)
                while start + 1 in lookup:
                    count += 1
                    start += 1
                max_len = max(max_len, count)
            count = 1
        return max_len