def sum_n(n):
    if n == 1:
        return 1 
    else:
        return n + sum_n(n-1)
n = 10
print(sum_n(n))
