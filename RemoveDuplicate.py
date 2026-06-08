def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result  
arr = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(arr))

#Better Two Pointer Approach
#def remove_duplicates(arr):
#    if not arr:
#        return []
#    result = [arr[0]]
#    i = 0
#    for j in range(1, len(arr)):
#        if arr[j] != arr[i]:
#           i += 1
#            arr[i] = arr[j]
# return i + 1 
#arr = [1, 2, 3, 2, 4, 1, 5]
#print(remove_duplicates(arr))