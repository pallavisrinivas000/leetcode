class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: collect positions of zero
        n = len(matrix)       # number of rows
        m = len(matrix[0])
        def mark_row(i):
            for j in range(m):
                matrix[i][j] =0
    
        def mark_col(j):
            for i in range(n):
                matrix[i][j] = 0

        zero_positions = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        
        # Step 2: mark rows and cols
        for i, j in zero_positions:
            mark_row(i)
            mark_col(j)
    
