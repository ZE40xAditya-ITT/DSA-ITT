def Second_smallest(arr):
    if len(arr) < 2:
        return None
    smallest = float('inf')
    second = float('inf')
    for num in arr:
        if num < smallest:
            second = smallest
            smallest = num
        elif num < second and num != smallest:
            second = num
    return second if second != float('inf') else None
print(Second_smallest([10, 5, 8, 20, 15]))