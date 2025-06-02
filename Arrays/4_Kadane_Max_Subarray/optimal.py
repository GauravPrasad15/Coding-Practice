'''
Logic -

Step-by-step example with your input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Index	Value	     current_sum Calculation	              max_sum Update
0	     -2	     current_sum = max(-2, 0 + (-2)) = -2	        max_sum = -2
1	     1	     current_sum = max(1, -2 + 1) = 1	            max_sum = 1
2	     -3	     current_sum = max(-3, 1 + (-3)) = -2	        max_sum = 1
3	     4	     current_sum = max(4, -2 + 4) = 4	            max_sum = 4
4	     -1	     current_sum = max(-1, 4 + (-1)) = 3	        max_sum = 4
5	     2	     current_sum = max(2, 3 + 2) = 5	            max_sum = 5
6	     1	     current_sum = max(1, 5 + 1) = 6	            max_sum = 6
7	     -5	     current_sum = max(-5, 6 + (-5)) = 1	        max_sum = 6
8	     4	     current_sum = max(4, 1 + 4) = 5	            max_sum = 6

'''


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]):

        # initialing the final and current sum and array

        final_sum = nums[0]
        final_arr = [nums[0]]
        current_sum = nums[0]
        current_arr = [nums[0]]

        for i in range(1,len(nums)):
            '''

            This is for when you just want to find the max sum

            #current_sum = max(nums[i], current_sum + nums[i])
            #final_sum = max(final_sum, current_sum)

            '''
            
            # if the max(current_sum + nums[i], nums[i]) = current_sum
            if current_sum + nums[i] > nums[i]:
                current_sum = current_sum + nums[i]
                current_arr.append(nums[i])
            
            # if the max(current_sum + nums[i], nums[i]) = nums[i] -> reinitiazlizing current sum and array
            else:
                current_sum = nums[i]
                current_arr = [nums[i]]

            # if max(current_sum, final_sum) = current_sum, else no changes to final sum or array
            if current_sum > final_sum:
                final_sum = current_sum
                final_arr = current_arr.copy()


        print(final_sum)
        print(final_arr)

        


if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution.maxSubArray(nums)