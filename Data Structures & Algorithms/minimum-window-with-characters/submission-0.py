class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapS = {}
        mapT = {}

        for i in t:
            if i not in mapT:
                mapT[i] = 1
            else:
                mapT[i] += 1

        need = len(mapT)
        have = 0
        left = 0
        res = [-1, -1]
        res_len = float("inf")
        for right in range(len(s)):
            if s[right] not in mapS:
                mapS[s[right]] = 1
            else:
                mapS[s[right]] += 1
            if mapS[s[right]] == mapT.get(s[right], 0):   
                have +=1
    

            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = [left, right]
                if s[left] in mapT and mapS[s[left]] == mapT[s[left]]:
                    have -= 1

                mapS[s[left]] -= 1
                left +=1
                
        if res_len == float("inf"):
            return ""
        return s[res[0] : res[1] + 1]
