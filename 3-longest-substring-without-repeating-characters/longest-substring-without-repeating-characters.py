class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = 0
        memory = set()
        res = 0
        for j in range(len(s)):
            
            if s[j] in memory:
                while s[j] in memory:
                    memory.remove(s[i])
                    i += 1
                memory.add(s[j])
            else:
                memory.add(s[j])
                res = max(j-i+1,res)
                
                
        return res





        