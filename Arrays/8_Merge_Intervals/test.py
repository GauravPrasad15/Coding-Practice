from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = []

        #sorting the array
        intervals.sort()
        
        #appending the first row
        arr.append(intervals[0])
        
        #arr index counter
        c = 0

        for i in range(1, len(intervals)):
            # if the last value in arr is greater than the first value in interval but less than the last value in interval - take first of arr and last of interval and remove the row c
            if arr[c][1] >= intervals[i][0] and arr[c][1] <= intervals[i][1]:
                arr.append([arr[c][0],intervals[i][1]])
                del arr[c]

            # if the last value in arr is greater than the first value in interval and greater than the last value in interval - just kip the iteration
            elif arr[c][1] >= intervals[i][0] and arr[c][1] >= intervals[i][1]:
                continue
            
            # else add the interval row into the new arr
            else:
                arr.append(intervals[i])
                c+=1

        return arr
    

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    output = solution.merge(intervals)
    print(output)