from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num_arr_count = [0]*10

        for i in range(len(nums)):
            num_arr_count[nums[i]]+=1

        c=0
        for i in range(len(num_arr_count)):
            while(num_arr_count[i]>0):
                nums[c] = i
                c=c+1
                num_arr_count[i]-=1

        print(nums)






if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,0,2,1,1,0]
    solution.sortColors(nums)