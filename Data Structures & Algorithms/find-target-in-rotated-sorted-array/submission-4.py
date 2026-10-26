class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            elif nums[mid] < nums[right]:
                right = mid
        if nums[right] <= target <= nums[-1]:
            left = right
            right = len(nums)-1
        else:
            left = 0
            right = right -1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
