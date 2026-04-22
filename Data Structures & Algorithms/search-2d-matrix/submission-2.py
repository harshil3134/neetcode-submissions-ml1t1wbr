class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if len(matrix)==1:
        #     return self.binarysearch(matrix[0],0,len())
        return self.binarysearcharr(matrix,0,len(matrix)-1,target)


    
    def binarysearcharr(self,arr,start,end,target):
        if start>end:
            return False
        mid=(start+end)//2
        print("mid",mid)
        if arr[mid][0]<=target and arr[mid][-1]>=target:
            return self.binarysearch(arr[mid],0,len(arr[mid])-1,target)
        elif target<arr[mid][0]:
            return self.binarysearcharr(arr,start,mid-1,target)
        else:
            return self.binarysearcharr(arr,mid+1,end,target)
    
    def binarysearch(self,narr,start,end,target):
        print("fun called",narr,",",start,",",end,",",target)
        if start>end:
            return False
        
        mid=(start+end)//2
        print("mid",mid)
        print("narr mid",narr[mid])
        if narr[mid]==target:
            return True
        elif narr[mid]>target:
            return self.binarysearch(narr,start,mid-1,target)
        else:
            return self.binarysearch(narr,mid+1,end,target)