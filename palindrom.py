def is_palindrome(a):
    if a == a[-1::-1]:
        return True
    return False
print(is_palindrome(input("Enter name : ").lower()))