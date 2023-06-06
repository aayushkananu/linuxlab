import sys

def encode(message: str, key: int)-> str:
    message = message.upper()
    cip_text = ""
    check=0
    for c in message:
        ordd = ord(c)
        if ordd < 65 or ordd > 90:
            continue
        if check%50 == 0 and len(cip_text) != 0:
            cip_text += "\n"
        elif check%5 == 0 and len(cip_text) != 0:
            cip_text += " "
        cip_text += chr(65 + (ord(c)-65+key) % 26)
        check = check + 1
    return cip_text


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print("invalid input")
        sys.exit(1)
      
    key = int(sys.argv[1])
      
    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        message = sys.stdin.read()

    print(encode(message, key))
    print("The End")
    sys.exit(0)
