class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def sort(array1,array2):
            #since sorted then i can alternate sort using i,j
            i = 0
            j = 1

            s_i = 0

            if (len(array1) < 1) and (len(array2) < 1):
                return [0]
            
            if (len(array1) > 0):
                i = 0
                j = 0
            if (len(array1) < 1):
                return array2
                


            while (len(array2)>0):
                # if array 2 element in range of array 1 then insert between alway move on i + 1,j + 1  pop array 2
                # if out of element then push at last recall an array again pop array 2
                #if array 2 run out jump of loop and return
                if array1[i] <= array2[s_i] and array1[j] >= array2[s_i]:
                    array1.insert(j,array2[s_i])
                    array2.pop(s_i)
                    
                elif array1[i] >= array2[s_i] and array1[j] >= array2[s_i]:
                    array1.insert(i,array2[s_i])
                    array2.pop(s_i)
                    
                
                if j < len(array1)-1:
                    j += 1

                else:
                    array1.append(array2[s_i])
                    array2.pop(s_i)
                    s_i = 0

                if i < j - 1:
                    i += 1
                # print(i,j,s_i,array1,array2)
            return array1
    
        sorted = sort(nums1,nums2)
        # print(sorted)
        length = len(sorted)
        if length % 2 == 0:
            left =( length - 1 ) // 2
            right = (length + 1) // 2
            print(left,right)
            sum_both = sorted[left] + sorted[right]
            print(sum_both)
            sol = float(sum_both) / 2
            return sol
        else:
            middle = length // 2
            sol = sorted[middle]
            return sol






        