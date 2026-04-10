class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=[]
       

        for i in range(200):
            buffer=set()
            for word in strs:

                try :
                    buffer.add(word[i])
                except:
                    buffer.add("")
        
            if len(buffer)==1:
                result.append(buffer.pop())
            else:
                break

        res="".join(result)
        return res