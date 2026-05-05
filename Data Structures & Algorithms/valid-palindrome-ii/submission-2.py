class Solution:
    def validPalindrome(self, s: str) -> bool:
        a=self.check(s)
        b=self.check(s[::-1])
        return True if a or b else False

    def check(self,s): 
        l,r=0,len(s)-1
        mod=False
        while l<r:
            if s[l]!=s[r]:
                if mod==True:
                    return False
                else:
                    # print("here")
                    # print("else l+1",s[l+1],"r",s[r])
                    if s[l]==s[r-1]:
                        r-=1
                    elif s[l+1]==s[r]:
                        print("in l+1",l,"r",r)
                        l+=1
                    else:
                        print("else l+1",s[l],"r",s[r])
                        return False
                    mod=True
            else:
                l+=1
                r-=1
        return True
            

