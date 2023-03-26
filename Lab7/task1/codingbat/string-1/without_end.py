def without_end(str):
    if len(str) < 2:
        return str
    
    if len(str) % 2 == 0:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str:-1]
        print(front + rear)

    else:
        half_len_str = int(len(str)/2)
        front = str[1:half_len_str]
        rear = str[-half_len_str-1:-1]
        print(front + rear)  