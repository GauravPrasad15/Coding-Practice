from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        for i in range(len(nums)):
            while mid <= high:
                if nums[mid]==0:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low+=1
                    mid+=1

                elif nums[mid]==2:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high-=1

                else:
                    mid+=1

        print(nums)


        






if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,0,2,1,1,0]
    solution.sortColors(nums)