class Solution(object):
        def isAnagram(self, s,t):
            s = str(s)
            t = str(t)
            if len(s) != len(t):
                return False
            else:
                SCount = {}
                TCount = {}
                for C in range(len(s)):
                    SCount[s[C]] = 1 + SCount.get(s[C],0)
                    TCount[t[C]] = 1 + TCount.get(t[C], 0)
                for i in SCount:
                    if SCount[i] != TCount.get(i,0):
                        print("False")
                        return False
            print("True")
            return True