def pattern_1(n):
    """
    ****
    ****
    ****
    ****
    """
    for row in range(n):
        for col in range(n):
            print("*", end="")
        print()


###################################################################################################


def pattern_2(n):
    """
    *
    **
    ***
    ****
    *****
    """
    for row in range(n):
        for col in range(row + 1):
            print("*", end="")
        print()


###################################################################################################
def pattern_3(n):
    """
    1
    12
    123
    1234
    """
    for row in range(n):
        for col in range(row + 1):
            print(col + 1, end="")
        print()


###################################################################################################
def pattern_4(n):
    """
    1
    22
    333
    4444
    """
    for row in range(n):
        for col in range(row + 1):
            print(row + 1, end="")
        print()


###################################################################################################
def pattern_5(n):
    """
    ****
    ***
    **
    *
    """
    for row in range(n):
        for col in range(n - row):
            print("*", end="")
        print()


###################################################################################################
def pattern_6(n):
    """
    12345
    1234
    123
    12
    1
    """
    for row in range(n):
        for col in range(n - row):
            print(col + 1, end="")
        print()


###################################################################################################
def pattern_7(n):
    """
       *
      ***
     *****
    *******

    """
    for row in range(n):
        # For spaces
        for col in range(n - row - 1):
            print(" ", end="")

        # for stars
        for col in range(2 * row + 1):
            print("*", end="")

        # for spaces
        for col in range(n - row - 1):
            print(" ", end="")
        print()


###################################################################################################
def pattern_8(n):
    """
    *******
     *****
      ***
       *
    """
    for row in range(n):
        # for spaces
        for col in range(row):
            print(" ", end="")
        # for stars
        for col in range(2 * (n - row) - 1):
            print("*", end="")
        # for spaces
        for col in range(row):
            print(" ", end="")
        print()


###################################################################################################
def pattern_9(n):
    # Combination of pattern 7 and 8
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end="")
        for col in range(2 * row + 1):
            print("*", end="")
        for col in range(n - row + 1):
            print(" ", end="")
        print()
    for row in range(n):
        for col in range(row):
            print(" ", end="")
        for col in range(2 * (n - row) - 1):
            print("*", end="")
        for col in range(row):
            print(" ", end="")
        print()


###################################################################################################
def pattern_10(n):
    """
    *
    **
    ***
    ****
    ***
    **
    *
    """
    for row in range(2 * n - 1):
        for col in range(n):
            if row < n:
                if col <= row:
                    print("*", end="")
            else:
                if col <= (2 * n - row - 2):
                    print("*", end="")
        print()


###################################################################################################
def pattern_11(n):
    """
    1
    01
    101
    0101
    """

    for row in range(n):
        if row % 2 == 0:
            start = 1
        else:
            start = 0
        for col in range(row + 1):
            print(start, end="")
            start = 1 - start

        print()


###################################################################################################
def pattern_12(n):
    """
    1      1    0[6] n = 4
    12    21    1[4]
    123  321    2[2]
    12344321    3[0]

    """
    for row in range(n):
        # first set of numbers
        for col in range(row + 1):
            print(col + 1, end="")

        # for spaces
        for col in range(2 * (n - row - 1)):
            print(" ", end="")

        # for numbers in reverse

        for col in range(row + 1, 0, -1):
            print(col, end="")
        print()


###################################################################################################
def pattern_13(n):
    """
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    num = 1
    for row in range(n):
        for col in range(row + 1):
            print(num, end=" ")
            num += 1
        print()


###################################################################################################
def pattern_14(n):
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    for row in range(n):
        alpha = 65
        for col in range(row + 1):
            print(chr(alpha), end="")
            alpha += 1
        print()


###################################################################################################
def pattern_15(n):
    """
    ABCDE
    ABCD
    ABC
    AB
    A
    """
    for row in range(n):
        alpha = 65
        for col in range(n - row):
            print(chr(alpha), end="")
            alpha += 1
        print()


###################################################################################################
def pattern_16(n):
    """
    A
    BB
    CCC
    DDDD
    EEEEE
    """
    alpha = 65
    for row in range(n):
        for col in range(row + 1):
            print(chr(alpha), end="")
        print()
        alpha += 1


###################################################################################################
def pattern_17(n):
    """
       A
      ABA
     ABCBA
    ABCDCBA
    """
    for row in range(n):
        alpha = 65
        # for spaces
        for col in range(n - row - 1):
            print(" ", end="")

        # for alphabets
        for col in range(2 * row + 1):
            print(chr(alpha), end="")
            if col < row:
                alpha += 1
            else:
                alpha -= 1

        # for spaces
        for col in range(n - row - 1):
            print(" ", end="")
        print()


###################################################################################################
def pattern_18(n):
    """
    E
    D E
    C D E
    B C D E
    A B C D E
    """
    for row in range(n):
        alpha = 65 + n - 1 - row
        for col in range(row + 1):
            print(chr(alpha), end="")
            alpha += 1

        print()


###################################################################################################
def pattern_19(n):
    """
    **********      0 [5, 0 , 5]
    ****  ****      1 [4, 2, 4]
    ***    ***      2 [3, 4 , 3]
    **      **      3 [2, 6, 2]
    *        *      4 [1, 8, 1]
    -------------------------------
    *        *      0 [1, 8, 1]
    **      **      1 [2, 6, 2]
    ***    ***      2 [3, 4, 3]
    ****  ****      3 [4, 2, 2]
    **********      4 [5, 0, 5]

    """
    # for upper half of the pattern
    for row in range(n):
        # for stars
        for col in range(n - row):
            print("*", end="")

        # for spaces
        for col in range(2 * row):
            print(" ", end="")

        # for stars
        for col in range(n - row):
            print("*", end="")
        print()

    # for lower half of the pattern
    for row in range(n):
        # for stars
        for col in range(row + 1):
            print("*", end="")

        # for spaces
        for col in range(2 * (n - row) - 2):
            print(" ", end="")

        # for stars
        for col in range(row + 1):
            print("*", end="")
        print()


###################################################################################################
def pattern_20(n):
    """
    *        *      0 [1, 8, 1]
    **      **      1 [2, 6, 2]
    ***    ***      2 [3, 4, 3]
    ****  ****      3 [4, 2, 4]
    **********      4 [5, 0, 5]
    ****  ****      5 [4, 2, 4]
    ***    ***      6 [3, 4, 3]
    **      **      7 [2, 6, 2]
    *        *      8 [1, 8, 1]

    """
    spaces = 2 * n - 2
    for row in range(2 * n - 1):
        # for stars
        stars = row + 1
        if row > n - 1:
            stars = 2 * n - row - 1
        for col in range(stars):
            print("*", end="")

        # for spaces
        for col in range(spaces):
            print(" ", end="")

        for col in range(stars):
            print("*", end="")
        print()
        if row < n - 1:
            spaces -= 2
        else:
            spaces += 2


###################################################################################################
def pattern_21(n):
    """
    ****
    *  *
    *  *
    ****
    """
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


###################################################################################################
def pattern_22(n):
    """
    4 4 4 4 4 4 4
    4 3 3 3 3 3 4
    4 3 2 2 2 3 4
    4 3 2 1 2 3 4
    4 3 2 2 2 3 4
    4 3 3 3 3 3 4
    4 4 4 4 4 4 4
    """
    for row in range(2 * n - 1):
        for col in range(2 * n - 1):
            top = row
            left = col
            bottom = (2 * n - 2) - row
            right = (2 * n - 2) - col
            print(n - min(min(top, bottom), min(left, right)), end=" ")
        print()


def main():
    t = int(input("Enter test cases: "))

    for _ in range(t):
        n = int(input("Enter the number: "))
        pattern_22(n)


if __name__ == "__main__":
    main()
