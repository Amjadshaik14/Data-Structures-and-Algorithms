# Brute force approach


def print_divisor_brute(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    """
i x    = num
1 x 36 = 36
2 x 18 = 36
3 x 12 = 36
4 x 8 = 36
6 x 6 = 36
    """


def print_divisor(num):
    divisors = []
    for i in range(1, int(num ** (0.5)) + 1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num // i)
    divisors.sort()
    print(*divisors)


def main():
    t = int(input("Enter the number of test cases: "))

    for _ in range(t):
        num = int(input("Enter the number: "))
        print_divisor(num)


if __name__ == "__main__":
    main()
