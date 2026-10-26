class Solution:
    def isValid(self, s: str) -> bool:
        check = []

        for i in s:
            if i == '[' or i == '(' or i == '{':
                check.append(i)
            elif i == ']' or i == ')' or i == '}':
                if len(check) == 0:
                    return False
                elif check[-1] == '[' and i == ']':
                    check.pop()
                elif check[-1] == '(' and i == ')':
                    check.pop()
                elif check[-1] == '{' and i == '}':
                    check.pop()
                else:
                    return False
        if len(check) > 0:
            return False

        return True