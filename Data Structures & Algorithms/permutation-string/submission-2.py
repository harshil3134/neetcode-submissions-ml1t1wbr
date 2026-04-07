class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1, count2 = {}, {}
        # 1. Initialize maps for the first window
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        
        # 2. Initial matches count
        matches = 0
        for i in range(97, 123):
            char = chr(i)
            if count1.get(char, 0) == count2.get(char, 0):
                matches += 1

        l = 0
        # 3. Slide the window
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add right character
            char_r = s2[r]
            count2[char_r] = 1 + count2.get(char_r, 0)
            if count1.get(char_r, 0) == count2[char_r]:
                matches += 1
            elif count1.get(char_r, 0) + 1 == count2[char_r]:
                matches -= 1

            # Remove left character
            char_l = s2[l]
            count2[char_l] -= 1
            if count1.get(char_l, 0) == count2[char_l]:
                matches += 1
            elif count1.get(char_l, 0) - 1 == count2[char_l]:
                matches -= 1
            l += 1

        return matches == 26