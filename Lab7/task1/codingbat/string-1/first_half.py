def first_half(str):
    if len(str) % 2 != 0:
        print("The length of the string is Odd.")
    str_half = int(len(str)/2)
    print(str[:str_half])