class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        tstack=[]

        for i in range(len(temperatures)):
            if len(tstack)==0:
                tstack.append([temperatures[i],i])
                continue
            # print(tstack)
            # print(temperatures[i]," ",tstack[-1][0])
            while tstack and temperatures[i]>tstack[-1][0]:
                    num,ind=tstack.pop()
                    # print(num, " ",ind)
                    res[ind]=i-ind
            tstack.append([temperatures[i],i])
            
        return res
