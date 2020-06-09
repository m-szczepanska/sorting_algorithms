def insertion_sort(unsorted_arr):
    for num in range(1, len(unsorted_arr)):
        # at he beginning of unsorted_arr start to build sorted part of
        # unsorted_arr; I chose increasing order.
        sorted_part = unsorted_arr[:num]
        for num_2 in range(len(sorted_part)):
            # if the next num in unsorted_arr is smaller then any number in
            # sorted_part remove the num from unsorted_arr and insert it
            # in sorted_part.
            if unsorted_arr[num] < sorted_part[num_2]:
                sorted_part = sorted_part[:num_2] + [unsorted_arr[num]] + sorted_part[num_2:]
                unsorted_arr = sorted_part + unsorted_arr[num+1:]
    return sorted_part




print(insertion_sort([3, 1, 4, 2, 5, 8, 6]))



# 3, 1, 4, 2, 5, 8, 6
# 1, 3, 4, 2, 5, 8, 6
# [1] + [2] + [3, 4] = [1, 2, 3, 4]
