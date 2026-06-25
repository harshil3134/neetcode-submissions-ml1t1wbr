class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict(int)

        for i in nums:
            count[i]+=1

            if len(count)<=2:
                continue
            
            new_count=defaultdict(int)
            for k,v in count.items():
                if v>1:
                    new_count[k]=v-1
            
            count=new_count

        res=[]
        for i in count:
            if nums.count(i)>len(nums)//3:
                res.append(i)
        
        return res