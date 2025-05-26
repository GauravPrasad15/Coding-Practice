from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # finding out the length of row and column
        r = len(matrix)
        c = len(matrix[0])

        # defining empty set for row and column to track which index of
        # row or column has 0
        row = set()
        col = set()


        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                        row.add(i)
                        col.add(j)


        for i in row:
            for j in range(0,c):
                matrix[i][j] = 0

        
        for j in col:
            for i in range(0,r):
                matrix[i][j] = 0

        print(matrix)
                        


class main():
    solution = Solution()
    List = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(List)

main()