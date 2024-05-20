def Encode():
    key=input("enter key: ")
    char=key
    try:
        key=int(key)
    except:
        print("invalid input")
        exit()

# rebuild key:
    if (key>=131 or key<=0 or key==109 or 63<=key<=93):
        add=0
        char=list(char)
        for i in range(len(char)):
            temp=int(char[i])
            add=add+temp
        if(add>130):
            key=123
        elif(add==109):
            key=110
        elif(63<=add<=93):
            key=61
        else:
            key=add

# main encoding
    msg = input("type your massage: ")
    msg = list(msg)
    temp = 0
    print("The encrypted msg is => " ,end="")
    for letters in msg:
        if letters == " ":
            letters = "@"

        temp = ord(letters) + key
        print(chr(temp), end="")
        # adding noise
        temp = hex(temp)
        print(temp[2:], end="")

    print("\n")


def Decode():
    key=input("enter key: ")
    char=key
    try:
        key=int(key)
    except:
        print("invalid input")
        exit()

# rebuild key:
    if (key>=131 or key<=0 or key==109 or 63<=key<=93):
        add=0
        char=list(char)
        for i in range(len(char)):
            temp=int(char[i])
            add=add+temp
        if(add>130):
            key=123
        elif(add==109):
            key=110
        elif(63<=add<=93):
            key=61
        else:
            key=add

# main decoding
    x = input("input massage: ")
    y = len(x)
    msg = []
    # removing noise
    for i in range(0, y, 3):
        msg.append(x[i])
    temp = 0
    for letters in msg:
        temp = ord(letters) - key
        if chr(temp) == "@":
            print(" ", end="")
        else:
            print(chr(temp), end="")
    print("\n")

# main body
x = input("enter 1 for encode\nenter 2 for decode\n==> ")
match x:

    case "1":
        Encode()

    case "2":
        Decode()

    case _:
        print("Invlid input")

