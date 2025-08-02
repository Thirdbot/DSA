class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        number_order = ord(target)

        for char in letters:
            if ord(char) > number_order:
                return char
        return letters[0]
        