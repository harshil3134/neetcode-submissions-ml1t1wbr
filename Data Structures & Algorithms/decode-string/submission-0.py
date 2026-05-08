class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):

            if s[i]!=']':
                stack.append(s[i])
            
            else:
                subs=""
                while stack[-1]!='[':
                    subs=stack.pop()+subs
                stack.pop()
                
                dig=""
                while stack and stack[-1].isdigit():
                    dig=stack.pop() +dig
                
                stack.append(int(dig)*subs)
        return "".join(stack)