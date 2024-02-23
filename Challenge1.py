a = int(input("Masukkan nilai 1 : "))
while True:
    if a>10 and a<13:
        print("Benar")
        a = int(input("Masukan nilai 2 : "))
        while True:
            if 20<=a<=23 or 34<=a<=38 or 40<=a<=42:
                print("Benar")
                break
            else:
                print("Salah")
                a = int(input("Masukan nilai 2 : "))

        break
    else:
        print("Salah")
        a = int(input("Masukan nilai 1 : "))