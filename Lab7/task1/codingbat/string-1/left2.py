def left2(str):
    if len(str) >= 2:
        print(str[2:] + str[:2])
    else:
        return -1