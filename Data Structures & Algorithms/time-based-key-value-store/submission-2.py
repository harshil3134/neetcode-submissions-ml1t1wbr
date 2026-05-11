class TimeMap:

    def __init__(self):
        self.kmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kmap.setdefault(key,[]).append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        
        klist=self.kmap.get(key,[])
        if klist:
            print("klist",klist)
            res=self.binarysearch(klist,0,len(klist)-1,timestamp)
            print("res1",res)
            print("res",klist[res][1])
            
            return klist[res][1] if klist[res][0]<=timestamp else ""
        else:
            return ""

    def binarysearch(self,arr,start,end,target):

        if start>end:
            return end

        mid=(start+end)//2
        print("mid",mid,"target",target,"arr mid",arr[mid][0])
        if target==arr[mid][0]:
            return mid
        elif arr[mid][0]<target:
            return self.binarysearch(arr,mid+1,end,target)
        else:
            return self.binarysearch(arr,start,mid-1,target)
        




