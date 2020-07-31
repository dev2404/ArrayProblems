#SET MATRIX ZEROS
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])

        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    for k in range(C):
                        if matrix[i][k] != 0:
                            matrix[i][k] = MODIFIED
                        else:
                            0
                    for k in range(R):
                        if matrix[k][j] != 0:
                            matrix[k][j] = MODIFIED
                        else:
                            0
        for i in range(R):
            for j in range(C):
                if  matrix[i][j] == MODIFIED:
                    matrix[i][j] = 0
                    
