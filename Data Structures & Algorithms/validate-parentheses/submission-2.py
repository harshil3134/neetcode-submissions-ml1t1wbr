class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        symap={")":"(","}":"{","]":"["}
        stack1=[]

        for i in s:
            if i in ["(","{","["]:
                stack1.append(i)
            if i in [")","}","]"]:
                if len(stack1)==0:
                    return False
                ele=stack1.pop()
                if symap[i]!=ele:
                    return False
        if len(stack1)!=0:
            return False
        return True