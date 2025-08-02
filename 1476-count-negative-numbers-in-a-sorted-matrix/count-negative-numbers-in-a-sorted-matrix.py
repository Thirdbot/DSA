class Solution(object):
    def countNegatives(self, grid,i=0,sumNeg=0):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if i >= len(grid[:]):
            return sumNeg
            
        placeholder = 0
        
        for j in grid[i][:]:
            if j < 0:
                sumNeg += 1

        return self.countNegatives(grid,i+1,sumNeg)
        
