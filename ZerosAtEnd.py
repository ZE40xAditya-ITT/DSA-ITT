def zeros_at_end(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1

arr = [0, 1, 0, 3, 12]
zeros_at_end(arr)
print(arr)