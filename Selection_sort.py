
def select_sort(random_num):

    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if random_num[j] < random_num[minpos]:
                minpos = j

        temp = random_num[i]
        random_num[i] = random_num[minpos]
        random_num[minpos] = temp
        print(random_num)


random_num = [66, 35, 88, 93, 28, 59, 97, 69, 62, 9]
print("Unsorted array:", random_num, "\n")
print("<<<Process of sorting the array>>>")
select_sort(random_num)
