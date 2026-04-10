class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=0
        flag=True
        for e in range(len(strs[0])):
            for i in strs:
    
                if len(i)<=j or i[j]!=strs[0][j] :
                    flag=False
                    break
            
            if flag==False:
                break
            j+=1
        res=strs[0][0:j]
        return res
            