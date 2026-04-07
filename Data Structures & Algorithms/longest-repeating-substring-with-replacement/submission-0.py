class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphadict={}
        res=0
        l=0
        for r in range(len(s)):
            alphadict[s[r]]=alphadict.get(s[r],0)+1


            if ((r-l+1)-max(alphadict.values()))>k:
                alphadict[s[l]]-=1
                l+=1
            
            res= max(res,r-l+1)
        return res

