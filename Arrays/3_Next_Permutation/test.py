# Brute Force - use recursion to find and store all possible permutation. However Time Complexity = n! * n
#
""" 
Optimal 

1. Start from back and find the position where value dips
2. Swap the dipped value with the smallest value till it from end
3. arrange all the next values in reverse

Edge case - if no dip, just sort it
"""


from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # flag to track the breaking index where the i-1th num us smaller than ith num going reverse
        b = -1

        # loop to find the breaking index and then break
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                b=i-1
                break
        
        
        # if no break was found just reverse the list
        if b == -1:
            nums.sort(reverse=False)
        else:
            for i in range(len(nums)-1,-1,-1):
                # if break found - traverse reverse until you find a nun greater than at breaking index - then swap and break
                if nums[i]>nums[b]:
                    nums[i], nums[b] = nums[b], nums[i]
                    break
            
            # reverse the entire sub list after the break index to determine the smallest next permutation
            nums[b+1:] = reversed(nums[b+1:])


        print(nums)
        
        
                        


if __name__ == "__main__":
    solution = Solution()
    nums = [2,1,5,4,3,0,0]
    #List = [1,2,3]
    solution.nextPermutation(nums)