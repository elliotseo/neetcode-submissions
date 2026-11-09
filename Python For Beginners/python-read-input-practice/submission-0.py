def add_two_numbers() -> int:
    user_input = input()
    list_n = [int(n) for n in user_input.split(",")]

    return list_n[0] + list_n[1]




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
