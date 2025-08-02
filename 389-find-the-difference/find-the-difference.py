class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1

        return sorted_t[i]
