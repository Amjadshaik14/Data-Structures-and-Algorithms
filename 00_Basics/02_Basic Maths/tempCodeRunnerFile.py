def isPalindrome(num):
    result = 0
    original = num
    while num:
        rem = num % 10
        result = result * 10 + rem
        num //= 10
    return True if original == result else False


def main():
    t = int(input("Enter the number of test cases: "))