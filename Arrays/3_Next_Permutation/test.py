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
        b = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                b=i-1
                break
        
        
        if b == -1:
            nums.sort(reverse=False)
        else:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]>nums[b]:
                    nums[i], nums[b] = nums[b], nums[i]
                    break

            nums[b+1:] = reversed(nums[b+1:])


        print(nums)
        
        
                        


class main():
    solution = Solution()
    List = [2,1,5,4,3,0,0]
    #List = [1,2,3]
    solution.nextPermutation(List)

main()