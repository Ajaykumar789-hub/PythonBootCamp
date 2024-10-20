'''
Asked in companies:

JP Morgan

TCS

Wells fargo

Gameskraft



Description:
You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. There are at least two different characters in letters. Your task is to return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.



Input:

letters: A sorted array of characters in non-decreasing order.

target: A character to compare against.

Output:

Return the smallest character that is greater than target. If no such character exists, return the first character in letters.



Example:

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
 
Input:
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'
 
Input:
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'
'''

lst = ['c', 'f', 'z']
target = 'k'
# output: 'c'

letters = ['c', 'f', 'j']
target2 = 'c'
# Output: 'f'

def binary_searh(letters, target):
    n = len(letters)
    start, end = 0, n-1
    
    if target >= letters[end]:
        return letters[0]
    while(start<=end):
        mid = (start + end)//2
        if(letters[mid] == target):
            return mid
        elif(letters[mid] > target):
            end = mid -1
        else:
            start = mid +1
        
    return letters[start]

print(binary_searh(lst, target))
print(binary_searh(letters, target2))