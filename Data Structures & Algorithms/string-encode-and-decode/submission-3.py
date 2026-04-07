class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            tem=len(i)
            s=s+str(tem)+'#'+i
        #print(s)    
        return s

    def decode(self, s: str) -> List[str]:
        s1=""
        li=[]
        ind=0
        while True:
            if ind>=len(s):
                break
            #print("ind",ind)
            dig=""
            for e in range(ind,len(s)):
                if s[e]=='#':
                    break
                dig+=s[e]
            #print('dig ',dig)
            len1=int(dig)
            s1 = s[ind + len(dig)+1 : ind + len(dig)+1 + len1]
            #print('s1 ',s1)
            ind=ind+len1+len(dig)+1
            li.append(s1)
            s1=""
        #print(li)
        return li
