class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        ops = ['+', '-', '*', '/']
        for i in tokens:
            if i not in ops:
                nums.append(int(i))
            elif i == '+':
                tmp1 = nums.pop()
                tmp2 = nums.pop()
                nums.append(tmp1 + tmp2)
            elif i == '-':
                tmp1 = nums.pop()
                tmp2 = nums.pop()
                nums.append(tmp2 - tmp1)
            elif i == '*':
                tmp1 = nums.pop()
                tmp2 = nums.pop()
                nums.append(tmp1 * tmp2)
            elif i == '/':
                tmp1 = nums.pop()
                tmp2 = nums.pop()
                nums.append(int(tmp2 / tmp1))
            
        return nums.pop()    
                
                
                