def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
