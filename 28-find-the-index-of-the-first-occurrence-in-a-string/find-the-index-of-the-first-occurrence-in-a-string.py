class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length_substring = len(needle)

        for i in range(len(haystack) - len(needle) + 1):
            sub_haystack = haystack[i : i + length_substring]
            print(sub_haystack)
            if needle == sub_haystack:
                return i
        return -1

        