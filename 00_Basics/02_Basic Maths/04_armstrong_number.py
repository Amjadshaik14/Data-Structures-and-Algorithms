# What is an Armstrong Number?

# An Armstrong number, also known as a narcissistic number or plenary number,
# is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# 153 = 1 ^3 + 5 ^ 3 + 3 ^ 3 = 153


def isArmstrong(num):
    original = num
    num1 = num
    length = 0
    sum = 0
    # find the number of digits
    while num:
        num //= 10
        length += 1

    while original:
        last_digit = original % 10
        sum += last_digit**length
        original //= 10
    return sum == num1


def main():
    t = int(input("Enter the number of test cases: "))

    for _ in range(t):
        num = int(input("Enter the number: "))
        print(isArmstrong(num))


if __name__ == "__main__":
    main()
