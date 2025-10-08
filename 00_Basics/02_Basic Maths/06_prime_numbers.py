def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(3, int(num ** (0.5)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    t = int(input("Enter the number of test cases: "))

    for _ in range(t):
        num = int(input("Enter the number: "))
        isPrime(num)


if __name__ == "__main__":
    main()
