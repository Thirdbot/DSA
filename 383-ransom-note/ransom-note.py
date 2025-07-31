class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """


        for i in ransomNote:
            if i in magazine:
                del_magazine_index = magazine.index(i)
                magazine = magazine[:del_magazine_index] + magazine[del_magazine_index+1:]
            else:
                return False
        return True
        