class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while(start<=end):
            temp=numbers[start]+numbers[end]
            if temp==target:
                return [start+1,end+1]
            elif temp>target:
                end-=1
            else:
                start+=1
        return [0,0]

            
            
