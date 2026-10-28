class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = len(nums1)

        while left <= right:
            mid = (left+right) // 2
            halfLen = (len(nums1) + len(nums2) + 1) // 2
            j = halfLen-mid
            if mid == 0:
                maxLeftX = float('-inf')
            else:
                maxLeftX = nums1[mid-1]
            if mid == len(nums1):
                minRightX = float('inf')
            else:
                minRightX = nums1[mid]
            if j == 0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[j-1]
            if j == len(nums2):
                minRightY = float('inf')
            else:
                minRightY = nums2[j]
            

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = mid - 1
            elif maxLeftY > minRightX:
                left = mid + 1
        return mid