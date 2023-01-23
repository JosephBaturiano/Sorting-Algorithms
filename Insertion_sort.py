def insertion_sort(random_num):
    for i in range(1, len(random_num)):
        anchor = random_num[i]
        j = i - 1
        while j >= 0 and anchor < random_num[j]:
            random_num[j+1] = random_num[j]
            j = j - 1
        random_num[j+1] = anchor
        print(random_num)


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
print("Unsorted array:", random_num, "\n")
print("<<<Process of sorting the array>>>")
insertion_sort(random_num)
