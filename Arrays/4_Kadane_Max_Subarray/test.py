from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]):
        # initialziing final_sum and final_arr
        final_sum = -999
        final_arr = []

        for i in range(len(nums)):
            # putting the first element in sum and arr
            a = [nums[i]]
            sum = nums[i]

            # checking if a single element is greater than the sum
            if nums[i] > final_sum:
                    final_sum = nums[i]
                    final_arr = [nums[i]]

            # takes ith element and runs through the entire list after it to check max sum and the max sum subarray
            if i != len(nums)-1:
                for j in range(i+1,len(nums)):
                    sum = sum + nums[j]
                    a.append(nums[j])
                            
                    if sum > final_sum:
                        final_sum = sum
                        final_arr = a.copy()         


        print(final_sum)
        print(final_arr)


if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution.maxSubArray(nums)