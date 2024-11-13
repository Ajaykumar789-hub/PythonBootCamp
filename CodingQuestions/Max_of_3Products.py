# max of 3 products
def max_products(nums):
    nums.sort()

    max1 = nums[-1] * nums[-2] * nums[-3]
    max2 = nums[0] * nums[1] * nums[-1] # this necessary bcz two negative numbs can produce large pos number

    return max(max1, max2) # time complexity: O(n log n) because of sorting

nums = [1,2,3]
print(max_products(nums))