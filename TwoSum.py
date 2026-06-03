def Two_sum(num, target):
    seen = set()
    for i in num:
        complement = target - i
        if complement in seen:
            return (complement, i)
        seen.add(i)
    return None
num = [2, 7, 11, 15]
target = 9
result = Two_sum(num, target)
if result is None:
    print("No two numbers sum to the target")
else:
    print(f"Two numbers that sum to {target}: {result}")
