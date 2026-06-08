def Linear_Search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
target = 3
print(Linear_Search(arr, target))
