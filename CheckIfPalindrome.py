def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
phrase = "mom"
if is_palindrome(phrase):
    print(f'"{phrase}" is a palindrome.')
else:
    print(f'"{phrase}" is not a palindrome.')
