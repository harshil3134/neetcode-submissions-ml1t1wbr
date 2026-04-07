class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash=defaultdict(int)
        seq=1
        ite=1
        if len(nums)==0:
            return 0
        for i in nums:
            if i in hash:
                continue
            else:
                hash[i]=1
        for i in nums:
            if not(i-1 in hash) and (i+1 in hash):
                ite=1
                while True:
                    if i+ite in hash:
                        ite+=1
                    else:
                        break
                if ite>seq:
                    seq=ite
        
        return seq
