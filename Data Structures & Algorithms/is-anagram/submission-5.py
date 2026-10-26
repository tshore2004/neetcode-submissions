class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len(t)):
            hashs, hasht = {}, {}

            for i in range(len(s)):
                hashs[s[i]] = 1 + hashs.get(s[i],0)
                hasht[t[i]] = 1 + hasht.get(t[i],0)

            for c in hashs:
                if hashs[c] != hasht.get(c, 0):
                    return False
            return True
        return False
            
        