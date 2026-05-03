class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        i=0
        while i<len(path)-1:

            if path[i]=="/" and i<len(path)-1 and path[i+1]!="/":
                pstr=""
                i+=1
                while  i<len(path) and path[i]!="/":
                    pstr+=path[i]
                    i+=1
                if pstr==".." and len(st)>0:
                    st.pop()
                elif pstr=="..":
                    continue
                elif pstr==".":
                    pass
                else:
                    st.append(pstr)
            else:
                i+=1

        res=""
        for i in st:
            res+="/"+i
        # print("res",res)

        return res if res else "/"
