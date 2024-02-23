print("<<{:^59}>>".format("Identifikasi Bilangan"))
print("Identifikasi nilai jika nilai 10-15 atau nilai 20-25 atau 35-40")
print("-"*63)
n = int(input("Masukkan Bilangan : "))
while (n<10 or 15<n<20 or 25<n<35 or n>40):
    print("Salah..")
    n = int(input("Masukkan Bilangan : "))
else:
    print("Benar!")