class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = []
        max_area = 0
        n = len(heights)
        for i, h in enumerate(heights):
            
            while len(area)>0 and h<heights[area[-1]]:
                right = area.pop()
                if len(area) == 0:
                    width = i
                else:
                    left = area[-1]
                    width = i - left - 1
                max_area = max(max_area, heights[right] * width)
                print (max_area)
            area.append(i)
            # print (area)
        while len(area)>0:
            right = area.pop()
            if len(area) == 0:
                width = n
            else:
                left = area[-1]
                width = n - left - 1
            max_area = max(max_area, heights[right] * width)

        return max_area