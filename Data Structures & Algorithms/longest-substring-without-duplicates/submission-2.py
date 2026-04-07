class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=0
        tempstring=""
        for i in s:
            if i not in tempstring:
                tempstring+=i
            else:
                tempstring = tempstring[tempstring.index(i) + 1:] + i
                
            substring = max(substring, len(tempstring))
            
        return substring
