from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        arr = []

        intervals.sort()

        for i in range(len(intervals)):
            if not arr or intervals[i][0] > arr[-1][1]:
                arr.append(intervals[i])

            else:
                arr[-1][1] = max(arr[-1][1],intervals[i][1])


        return arr
    

if __name__ == "__main__":
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    output = solution.merge(intervals)
    print(output)