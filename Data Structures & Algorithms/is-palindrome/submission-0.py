import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0
        
        text = s.translate(s.maketrans("", "", string.punctuation))
        clean_text = text.replace(" ", "")
        while forward < len(clean_text):
            backward = len(clean_text) - forward - 1
            if clean_text[backward].lower() != clean_text[forward].lower():
                return False
            forward += 1
        return True