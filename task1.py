def difference_list(list1: list, list2: list):
    temp_set = set(list2)

    return [elem for elem in list1 if elem not in temp_set]


first = [1, 2, 3, 4, 5, 6]
second = [1, 3, 5, 7, 9]
print(difference_list(first, second))
