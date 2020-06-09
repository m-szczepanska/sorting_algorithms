def neighbor_swapping(unsorted_arr):
    for num in range(len(unsorted_arr)):
        if num+1 < len(unsorted_arr):
            nums_pair = unsorted_arr[num], unsorted_arr[num+1]
            if unsorted_arr[num+1] < unsorted_arr[num]:
                unsorted_arr[num], unsorted_arr[num+1] = unsorted_arr[num+1], unsorted_arr[num]

def check_if_arr_is_sorted(unsorted_arr):
    for num in range(len(unsorted_arr)):
        if num+1 < len(unsorted_arr):
            if unsorted_arr[num] > unsorted_arr[num+1]:
                return True
    return False

def bubble_sort(unsorted_arr):
    not_sorted = True
    while not_sorted:
        neighbor_swapping(unsorted_arr)
        not_sorted = check_if_arr_is_sorted(unsorted_arr)

    return unsorted_arr
