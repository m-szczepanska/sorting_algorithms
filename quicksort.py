# First approach to quicksort;
# I guess it lacks optimalization due to creating new subarrays and
# returning result in a new array instead of changing the initial one.


def find_pivot(unsorted_arr):
    pivot = [0, 0]
    array_len = len(unsorted_arr)
    if array_len % 2:
        # pivot = [value, index]
        pivot = [unsorted_arr[array_len//2], array_len//2]
    else:
        pivot = [unsorted_arr[array_len//2- 1], array_len//2 -1]
    return pivot

def partition(unsorted_arr, pivot):
    # create two empty subarrays
    left_subarray = []
    right_subarray = []

    for num in unsorted_arr:
        if num <= pivot[0]:
            left_subarray.append(num)
        else:
            right_subarray.append(num)

    # if unsorted_arr can be divided into two not empty subarrays
    if left_subarray and right_subarray:

        if len(left_subarray) > 1:
            quicksort(left_subarray)
        else:
            final_result.append(left_subarray[0])

        if len(right_subarray) > 1:
            quicksort(right_subarray)
        else:
            final_result.append(right_subarray[0])
    else:
        # if left or right subarray is empty repeat quicksort after changing
        # order in unsorted_arr (thus pivot will be diferrent)
        unsorted_arr[0], unsorted_arr[1] = unsorted_arr[1], unsorted_arr[0]
        quicksort(unsorted_arr)



def quicksort(unsorted_arr):
    pivot = find_pivot(unsorted_arr)
    partition(unsorted_arr, pivot)
    return final_result


# single arrays are appended here; sorted list
final_result = []

print(quicksort([9, 1, 14, 15, 24]))
