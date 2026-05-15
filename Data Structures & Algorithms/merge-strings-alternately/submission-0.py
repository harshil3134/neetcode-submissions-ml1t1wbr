class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        l2=0
        ans=""
        while l<len(word1) and l2<len(word2):
            ans=ans+word1[l]+word2[l2]
            l+=1
            l2+=1
        
        while l<len(word1):
            ans=ans+word1[l]
            l+=1
        
        while l2<len(word2):
            ans=ans+word2[l2]
            l2+=1
        
        return ans