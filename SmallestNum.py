def smallest_element(arr):
    if not arr:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest
arr = [8, 3, 11, 2, 15]
print(smallest_element(arr))