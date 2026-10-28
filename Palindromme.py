n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    remainder = n % 10
    reverse = reverse * 10 + remainder
    n = n // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")