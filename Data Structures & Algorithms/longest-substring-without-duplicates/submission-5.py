class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        count = 0
        for char in s:
            if char not in sub:
                sub.append(char)
                
            else:
                lastIndex = sub.index(char)
                sub = sub[lastIndex + 1:]
                sub.append(char)
            # print(sub)
            count = max(count, len(sub))
        return count