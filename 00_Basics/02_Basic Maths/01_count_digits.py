def count_digits(num):
    count = 0
    while num:
        num //= 10
        count += 1
    return count


def main():
    t = int(input("Enter test cases: "))

    for _ in range(t):
        num = int(input("Enter the number: "))
        print(count_digits(num))


if __name__ == "__main__":
    main()
