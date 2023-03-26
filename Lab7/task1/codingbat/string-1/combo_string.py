def combo_string(a, b):
    short = ""
    long = ""
    
    if len(a) < len(b):
        short = a
        long = b
        print(short + long + short)
        
    elif len(a) == len(b) or len(a) == len(b) == 0:
        print(a + b)
        
    else:
        short = b
        long = a
        print(short + long + short)