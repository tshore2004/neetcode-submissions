class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        count = 0
        window = deque()
        for i in range(0, len(nums)):
            if window and window[0] <= i-k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)

            if i>= k-1:
                out.append(nums[window[0]])
                
        return out