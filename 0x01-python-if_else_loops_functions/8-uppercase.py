#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            x -= 32
            c = chr(x)
        print('{}'.format(c), end="")
<<<<<<< HEAD
    print()
=======
        
    print()
>>>>>>> e6872e0a9ca8ce55a863bef1e450e6081f8f0469
