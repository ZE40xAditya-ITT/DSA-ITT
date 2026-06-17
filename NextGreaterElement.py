def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    
    return result
arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))