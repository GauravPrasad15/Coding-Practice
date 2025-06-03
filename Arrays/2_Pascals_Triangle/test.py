from typing import List

class Solution:
    def generate_pascals_triangle(self, numRows: int) -> List[List[int]]:
        # creation of new List for storing the matrix
        List = []

        for i in range(numRows):
            # arr for storing each new row of the matrix
            arr = [0]*(i+1)
            
            #initializing first and last position in the row with 1
            arr[0] = 1
            arr[i] = 1

            # assigning 2 pointers front and back for traversal
            f = 1
            b = i-f

            # continuting the loop this back pointer crosses front pointer
            while f<=b:
                if f==b:
                    # List[i-1] - to check in the previous row
                    arr[f] = List[i-1][f-1] + List[i-1][f]

                    # traversing front pointer 1 step ahead while back pointer 1 step back
                    f = f+1
                    b = i-f

                else:
                    arr[f] = List[i-1][f-1] + List[i-1][f]
                    arr[b] = List[i-1][b-1] + List[i-1][b]
                    
                    # traversing front pointer 1 step ahead while back pointer 1 step back
                    f = f+1
                    b = i-f

            # appendind the new row to the matrix        
            List.append(arr)
                    
        return List
        
                        


if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(solution.generate_pascals_triangle(n))