def sort_list(arr):

    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)


    if min_val == max_val:
        return arr + [min_val]

    
    min_indices = [i for i, x in enumerate(arr) if x == min_val]
    max_indices = [i for i, x in enumerate(arr) if x == max_val]


    new_arr = arr[:]


    for i in range(len(min_indices)):

        new_arr[min_indices[i]] = max_val
    for i in range(len(max_indices)):

        new_arr[max_indices[i]] = min_val


    new_arr.append(min_val)

    return new_arr

print(f"sort_list([])           => {sort_list([])}")
print(f"sort_list([2, 4, 6, 8]) => {sort_list([2, 4, 6, 8])}")
print(f"sort_list([1])          => {sort_list([1])}")
print(f"sort_list([1, 2, 1, 3]) => {sort_list([1, 2, 1, 3])}")
print(f"sort_list([5, 5, 5])    => {sort_list([5, 5, 5])}")
print(f"sort_list([10, 1, 5, 1, 10, 8]) => {sort_list([10, 1, 5, 1, 10, 8])}")