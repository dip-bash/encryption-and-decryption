def Encode():
    key = int(input("input kay: "))
    msg = input("type your massage: ")
    msg = list(msg)
    print(msg)
    temp = 0
    for letters in msg:
        if letters == " ":
            letters = "!"

        temp = ord(letters) + key
        print(chr(temp), end="")
        temp = hex(temp)
        print(temp[2:], end="")

    print("\n")


def Decode():
    key = int(input("input key: "))
    x = input("input massage: ")
    y = len(x)
    msg = []
    for i in range(0, y, 3):
        msg.append(x[i])
    print(msg)
    temp = 0
    for letters in msg:
        temp = ord(letters) - key
        if chr(temp) == "!":
            print(" ", end="")
        else:
            print(chr(temp), end="")
    print("\n")


x = input("enter 1 for encode\nenter 2 for decode\n==> ")
match x:

    case "1":
        Encode()

    case "2":
        Decode()

    case _:
        print("Invlid input")

