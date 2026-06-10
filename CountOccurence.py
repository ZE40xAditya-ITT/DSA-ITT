def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    result = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def count_occurrence(arr, target):
    upper = upper_bound(arr, target)
    lower = first_occurrence(arr, target)
    return upper - lower

arr = [1, 2, 2, 2, 3, 4, 5]
print(count_occurrence(arr, 2))
