'''
The steps will be the following:

First, we will run a loop that will continue until mid <= high.
There can be three different values of mid pointer i.e. arr[mid]
If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
Finally, our array should be sorted.

'''



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