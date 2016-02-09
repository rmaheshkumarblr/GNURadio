with open("test", "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        print (ord(byte))
