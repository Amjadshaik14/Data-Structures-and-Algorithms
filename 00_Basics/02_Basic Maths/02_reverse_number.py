def reverse_number(num):
    result = 0
    while num:
        rem = num % 10
        result = result * 10 + rem
        num //= 10
    return result


def main():
    t = int(input("Enter the number of test cases: "))

    for _ in range(t):
        num = int(input("Enter the number: "))
        print(reverse_number(num))


if __name__ == "__main__":
    main()

    # 123 - 0 * 10 + 3
    # 3 * 10 + 2
# 32 * 10 + 1
