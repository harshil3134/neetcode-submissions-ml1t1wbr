class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        # 1. Build the target map
        tmap = {}
        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
            
        smap = {}
        have, need = 0, len(tmap)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # 2. Expand the right pointer
        for r in range(len(s)):
            char = s[r]
            if char in tmap:
                smap[char] = smap.get(char, 0) + 1
                if smap[char] == tmap[char]:
                    have += 1
            
            # 3. Shrink the left pointer while the window is valid
            while have == need:
                # Update our smallest window coordinates
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                
                # Pop from left
                left_char = s[l]
                if left_char in tmap:
                    smap[left_char] -= 1
                    if smap[left_char] < tmap[left_char]:
                        have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""