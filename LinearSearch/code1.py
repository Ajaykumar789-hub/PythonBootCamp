'''
Asked in companies: Microsoft, Amazon, Uber

Description:
Given a sorted array that has been rotated, find the index of a given target value. The array was originally sorted in ascending order and then rotated at some pivot.

Parameters:

nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.

target (int): The integer value to search for in the array.

Return Values:

int: The index of the target value in the array, or -1 if the target is not in the array.

Example:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 
Output: 4 
Explanation: The target value 0 is at index 4 in the rotated array.
'''
##Linear Search
def find_target(nums, target):
    size = len(nums)
    for i in range(size):
        if(nums[i]==target):
            return i
    return -1
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
a = find_target(nums, target)
print(a)
