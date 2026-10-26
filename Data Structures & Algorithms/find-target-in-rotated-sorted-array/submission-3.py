class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            condA = nums[right] >= target
            condB = nums[mid] < target
            condC = nums[mid] > nums[right]

            if (condA and condB) or (condC and (condA or condB)):
                left = mid + 1
            else:
                right = mid - 1

        return -1
