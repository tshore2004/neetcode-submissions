class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        right_max, left_max = 0, 0
        while l<r:
            right_max = max(right_max, height[r])
            left_max = max(left_max, height[l])
            if left_max<right_max:
                area = area + min(left_max, right_max)-height[l]
                l+=1
                # print ("Area", area)
                # print ("Right: ", right_max)
                # print ("left: " , left_max)
            else:
                area = area + min(left_max, right_max)-height[r]
                r-=1
            
        return area