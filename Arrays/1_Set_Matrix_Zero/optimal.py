'''
In the previous approach, the time complexity is minimal as the traversal of a matrix takes 
at least O(N*M)(where N = row and M = column). In this approach, we can just improve the space complexity. 
So, instead of using two extra matrices row and col, we will use the 1st row and 1st column of the given matrix 
to keep a track of the cells that need to be marked with 0. But here comes a problem. 
If we try to use the 1st row and 1st column to serve the purpose, the cell matrix[0][0] is taken twice. 
To solve this problem we will take an extra variable col0 initialized with 1. 
Now the entire 1st row of the matrix will serve the purpose of the row array.
And the 1st column from (0,1) to (0,m-1) with the col0 variable will serve the purpose of the col array.
'''


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # finding out the length of row and column
        r = len(matrix)
        c = len(matrix[0])

        # col0 to keep track of first column
        col0 = 1


        # using the first row and first col to store into about 0 col and row 
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j!=0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0


        # using first row and col to check whether the non zero value at a position is supposed to be zero or not 
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0


        # checking for first row and first column
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0
        
        if col0 == 0:
            for i in range(r):
                matrix[i][0] = 0

        print(matrix)
                        


class main():
    solution = Solution()
    List = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(List)

main()