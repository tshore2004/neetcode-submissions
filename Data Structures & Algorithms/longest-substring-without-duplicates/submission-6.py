class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 1. While s[right] is in char_set, remove s[left] and increment left
            
            # 2. Add s[right] to char_set
            
            # 3. Update max_len
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len