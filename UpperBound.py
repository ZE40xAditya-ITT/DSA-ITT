def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    answer = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer   
arr = [1, 2, 2, 2, 3, 4, 5]
print(upper_bound(arr, 2))
