class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_size = 0
        max_freq = 0
        left, right = 0, len(s) - 1
        count = [0] * 26
         
        for right in range(len(s)):
            
            # 1. Update frequency for current character s[right]
            count[ord(s[right]) - ord('A')] += 1
            # 2. Update max_freq seen so far
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            # 3. Check if window is invalid: (window_length - max_freq) > k
            if right-left + 1-max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left+=1
                
            max_size = max(max_size, right-left+1)
            # 4. If invalid, shrink window from left and update count[s[left]]
            # 5. Update max_length with current valid window size

        return max_size