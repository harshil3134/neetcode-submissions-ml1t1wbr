class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}

        for i in list(s):
            if i in sdict:
                sdict[i]=sdict[i]+1
            else:
                sdict[i]=1

        for i in list(t):
            if i in tdict:
                tdict[i]=tdict[i]+1
            else:
                tdict[i]=1
        

        return (tdict==sdict)