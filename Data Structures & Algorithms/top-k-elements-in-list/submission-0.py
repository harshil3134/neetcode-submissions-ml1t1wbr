class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        d=defaultdict(int)
        for ele in nums:
             d[ele]+=1
        sort_dict=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))
        li=[]
        k_count=0
        for i in sort_dict.keys():
            #print(k_count)
            if k_count==k:
                break
            li.append(i)
            k_count+=1

       # print(li)
        return li
