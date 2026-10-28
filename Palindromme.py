n = 121

original = n
reverse = 0

while n > 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n = n // 10

if original == reverse:
    print(original, "is a Palindrome number")
else:
    print(original, "is not a Palindrome number")
