def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
        print(random_num)


def quick_sort(random_num, start, end):
    if start < end:
        pi = partition(random_num, start, end)
        quick_sort(random_num, start, pi-1)
        quick_sort(random_num, pi+1, end)


def partition(random_num, start, end):
    pivot_index = start
    pivot = random_num[pivot_index]

    while start < end:
        while start < len(random_num) and random_num[start] <= pivot:
            start += 1

        while random_num[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, random_num)

    swap(pivot_index, end, random_num)

    return end


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
print("Unsorted array:", random_num, "\n")
print("<<<Process of sorting the array>>>")
quick_sort(random_num, 0, len(random_num)-1)
