def outlier_num(my_list):
    largest_num = float('-inf')
    smallest_num = float('inf')
    for nums in my_list:
        if nums > largest_num:
            largest_num = nums
        if nums < smallest_num:
            smallest_num = nums
    return smallest_num, largest_num


kknjb
print(outlier_num([20, 50, 12, 6, 14, 8]))
