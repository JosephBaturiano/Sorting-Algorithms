def quick_sort(numbers, left, right):
    if left < right:
        partition_pos = partition(numbers, left, right)
        quick_sort(numbers, left,  partition_pos - 1)
        quick_sort(numbers, partition_pos + 1, right)


def partition(random_num, left, right):
    i = left
    j = right - 1
    pivot = random_num[right]

    while i < j:
        while i < right and random_num[i] < pivot:
            i += 1
        while j > left and random_num[j] >= pivot:
            j -= 1

        if i < j:
            random_num[i], random_num[j] = random_num[j], random_num[i]

    if random_num[i] > pivot:
        random_num[i], random_num[right] = random_num[right], random_num[i]
    print("\t\t\t ", random_num)
    return i


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
quick_sort(random_num, 0, len(random_num) - 1)
