def MaximumSubarraySum(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
arr = [1, 2, 3, 4, 5]
k = 3
print(MaximumSubarraySum(arr, k))
