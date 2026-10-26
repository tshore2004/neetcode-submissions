class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        tmp = ""
        comma = "~"
        for i in strs:
            tmp = i
            # tmp.reverse()
            tmp = tmp + comma
            out = out + tmp
        # out = out[:len(out)-1]


        return out


    def decode(self, s: str) -> List[str]:
        comma = "~"
        count = 0
        out = []
        t = 0
        for i in range(len(s)):
            
            if s[i] == comma:
                
                count = i
                tmp = s[t:i]
                out.append(tmp)
                t = i+1
        return out

