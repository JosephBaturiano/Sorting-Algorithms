def bubble_sort(random_num):
    for i in range(len(random_num)-1, 0, -1):
        for j in range(i):
            if random_num[j] > random_num[j+1]:
                swap = random_num[j]
                random_num[j] = random_num[j+1]
                random_num[j+1] = swap
                print(random_num)


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
print("Unsorted array:", random_num, "\n")
print("<<<Process of sorting the array>>>")
bubble_sort(random_num)
