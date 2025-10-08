# GCD and HCF are the same thing

# This is the brute force approach
def gcd_brute(num1, num2):
    gcd = 1
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    return gcd


def euclidean(num1, num2):
    # gcd(a, b) = gcd(a-b, b) where a>b
    # we can further decrease this to gcd(a, b)= gcd(a%b, b) where a > b
    """
    gcd(52, 10) -> gcd(42, 10) -> gcd(32, 10) -> gcd(22, 10) -> gcd(2, 10) -> gcd(10, 2) -> gcd(8, 2) -> gcd(6, 2) -> gcd(4, 2) -> gcd(2, 2) -> gcd(0,2) # 2 is the gcd

    instead of subtracting 1o 5 times to go from 52,10 -> 2, 10, we can directly do gcd(52%10, 10) which will be gcd(2, 10). then gcd(10, 2) = gcd(10% 2, 2) = gcd(0, 2)
    """
    while num1 and num2:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2  # Returns whichever is not zero


def main():
    t = int(input("Enter the number of test cases: "))

    for _ in range(t):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(euclidean(num1, num2))


if __name__ == "__main__":
    main()
