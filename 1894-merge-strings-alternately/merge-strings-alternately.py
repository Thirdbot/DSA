class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        length1 = len(word1)
        length2 = len(word2)
        placeholder = ""
        array = []

        min_length = min(length1,length2)
        for i in range(min_length):
            array.append(word1[i])
            array.append(word2[i])        
        placeholder.join([str(x) for x in array])
        print(placeholder)
        if len(word1) > len(word2):
            array.append(word1[min_length:])
        elif len(word2) > len(word1):
            array.append(word2[min_length:])
        return ''.join(array)

