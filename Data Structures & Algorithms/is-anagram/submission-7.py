class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets, sett = {}, {}
        if len(s) == len(t):
            for i in range(len(s)):
                sets[s[i]] = 1 + sets.get(s[i],0)
                sett[t[i]] = 1 + sett.get(t[i],0)

            for i in sets:
                if sets[i] != sett.get(i, 0):
                    return False
            return True
        
        return False

        