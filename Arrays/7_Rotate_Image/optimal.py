'''

Original :

1 2 3
4 5 6
7 8 9

Required Output :

7 4 1
8 5 2
9 6 3

----------------------------------------------------

Original :

1 2 3
4 5 6
7 8 9

Transpose:

1 4 7
2 5 8
3 6 9

Reverse Rows :

7 4 1
8 5 2
9 6 3


'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # transposing matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # reversing the row
        for i in range(len(matrix)):
            matrix[i].reverse()



if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix)

