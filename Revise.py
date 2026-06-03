def largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
arr = [5,2,8,1,9]
print(largest_element(arr))