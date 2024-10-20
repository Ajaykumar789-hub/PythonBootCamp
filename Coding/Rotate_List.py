'''
Description:
Given a list of integers and an integer D, write a function to rotate the list to the left by D positions.

Input Parameters:

ARR (List[int]): A list of integers.

D (int): The number of positions to rotate the list to the left.

Output:

List[int]: The list after rotating it to the left by D positions.

Example:

Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]
'''

def rotate_list(lst, D):
    D = D % len(lst)

    return lst[D:] + lst[:D]
    

