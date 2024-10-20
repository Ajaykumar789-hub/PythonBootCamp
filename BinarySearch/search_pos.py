nums = [5, 7, 7, 8, 8, 10]
target = 8
def search_postion(nums, target):

    def binary_sear(nums, target):
        start, end = 0, len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid]==target):
                result = mid
                end = mid -1
            elif(nums[mid]>target):
                end = mid-1
            else:
                start = mid +1
        return result

    def findLast(nums, target):
            """
            Find the last occurrence of the target using binary search.
            """
            start, end = 0, len(nums) - 1
            result = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    result = mid
                    start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return result
    
    start = binary_sear(nums, target)
    end = findLast(nums, target=target)
    return [start, end]

print(search_postion(nums, target))