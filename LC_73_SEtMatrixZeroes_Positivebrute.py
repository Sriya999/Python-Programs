class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    #store index i,j where 0 occurs
                    for k in range(len(matrix[i])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=-1
                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]=-1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
