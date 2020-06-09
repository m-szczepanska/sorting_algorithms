def selection_sort(unsorted_arr):
    for num in range(len(unsorted_arr)):
        local_min = [unsorted_arr[num], num]
        if num < len(unsorted_arr)-1:
            shorten_arr = unsorted_arr[(num+1):]

            for num_2 in range(len(shorten_arr)):
                if shorten_arr[num_2] < local_min[0]:
                    local_min = [shorten_arr[num_2], num_2+(num+1)]

            if local_min[1] != num:
                unsorted_arr[num], unsorted_arr[local_min[1]] = unsorted_arr[local_min[1]], unsorted_arr[num]

    return unsorted_arr
