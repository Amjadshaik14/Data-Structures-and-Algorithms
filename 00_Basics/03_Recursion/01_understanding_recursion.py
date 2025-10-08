def print_numbers(num):
    if num == 100:
        return
    print(num)
    num += 1
    print_numbers()


print_numbers()
