
def sort(nums):

    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


nums = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
