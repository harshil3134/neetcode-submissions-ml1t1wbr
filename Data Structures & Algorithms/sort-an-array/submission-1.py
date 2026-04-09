class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums


    def merge(self,nums,l,m,r):
        aleft,aright=nums[l:m+1],nums[m+1:r+1]
        i,j,k=l,0,0

        while j<len(aleft) and k<len(aright):
            if aleft[j]<aright[k]:
                nums[i]=aleft[j]
                i+=1
                j+=1
            
            else:
                nums[i]=aright[k]
                i+=1
                k+=1
            
        while j<len(aleft):
            nums[i]=aleft[j]
            i+=1
            j+=1
        
        while k<len(aright):
            nums[i]=aright[k]
            i+=1
            k+=1

        

    
    def mergesort(self,arr, l,r):
        if l>=r:
            return
        
        m=(l+r)//2
        self.mergesort(arr,l,m)
        self.mergesort(arr,m+1,r)

        self.merge(arr,l,m,r)
        
        return arr