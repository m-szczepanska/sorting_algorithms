
def merge_two_arrays(arr_a, arr_b):
    merged_arr = []

    while arr_a and arr_b:
        if arr_a[0] < arr_b[0]:
            merged_arr.append(arr_a[0])
            arr_a.pop(0)
        else:
            merged_arr.append(arr_b[0])
            arr_b.pop(0)
    else:
        while arr_a or arr_b:
            if arr_a:
                merged_arr.append(arr_a[0])
                arr_a.pop(0)
            else:
                merged_arr.append(arr_b[0])
                arr_b.pop(0)

    return merged_arr


def single_arrays_list(unsorted_arr):
    arrays_list = []
    for num in unsorted_arr:
        arrays_list.append([num])
    return arrays_list


def loop_merge(result_list):
    while len(result_list) != 1:
        for num in range(0, len(result_list)):
            if num+1 < len(result_list):
                result_list[num:num+2] = [merge_two_arrays(result_list[num], result_list[num+1])]
            else:
                loop_merge(result_list)
    else:
        return result_list


def merge_sort(unsorted_arr):
    divided_arr = single_arrays_list(unsorted_arr)
    # if lenght of divided_arr is odd then merge 2 last elements of the divided_arr
    if len(divided_arr) % 2 and len(divided_arr) > 2:
        divided_arr[len(divided_arr)-2:] = [merge_two_arrays(divided_arr[-2], divided_arr[-1])]
    sorted_array = loop_merge(divided_arr)

    return sorted_array[0]
