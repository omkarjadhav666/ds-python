def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merged_array = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", merged_array)
