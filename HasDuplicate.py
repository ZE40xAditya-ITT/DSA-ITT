def has_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
arr = [1, 2, 3, 4, 5, 2]
print(has_duplicate(arr))