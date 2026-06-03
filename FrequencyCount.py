def frequency_count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
arr = [1, 2, 2, 3, 3, 3, 4]
print(frequency_count(arr))