class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numstack = []
        operators = {'+', '-', '*', '/'}
        
        for i in tokens:
            if i not in operators:
                # This handles negative numbers correctly
                numstack.append(int(i))
            else:
                # Order matters: first pop is right, second pop is left
                num1 = numstack.pop() # right operand
                num2 = numstack.pop() # left operand
                
                if i == "+":
                    numstack.append(num2 + num1)
                elif i == "-":
                    numstack.append(num2 - num1)
                elif i == "*":
                    numstack.append(num2 * num1)
                else:
                    # int() on a float division truncates toward zero
                    numstack.append(int(num2 / num1))
        
        return numstack[0]