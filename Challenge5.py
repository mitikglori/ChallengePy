print("{:^35}".format("TIKET BUS"))
print("-"*35)
print("""
Kode Kota : 
1. Prabumulih
2. Muara Enim
3. Lubuklinggau
""")
kota = int(input("Pilihan Kota (1/2/3) :  "))
print(""""
Kode Kelas : 
1. Ekonomi
2. Bisnis
3. Eksekutif
""")
Kelas = int(input("Pilihan Kelas (1/2/3) : "))
bnyktkt = int(input("Banyak Tiket : "))
kode = input("Kode Promo : ")
print(f"{'-'*35}")
if kode.lower() == "igs" : 
    diskon = 0.1
else:
    diskon = 0
if (kota == 1):
    if(Kelas == 1):
        hargatkt = 100000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 2):
        hargatkt = 400000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 3):
        hargatkt = 700000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    else:
        print("Kelas invalid")

elif(kota == 2):
    if(Kelas == 1):
        hargatkt = 200000
        harga = hargatkt*bnyktkt
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 2):
        hargatkt = 500000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 3):
        hargatkt = 800000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    else:
        print("Kelas invalid")

elif(kota == 3):
    if(Kelas == 1):
        hargatkt = 300000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 2):
        hargatkt = 600000
        harga = hargatkt*bnyktkt
        diskon = 0
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    elif(Kelas == 3):
        hargatkt = 900000
        harga = hargatkt*bnyktkt
        total = harga - (harga*diskon)
        print(f"Harga Tiket           : Rp.{hargatkt}")
        print(f"Sub Total             : Rp.{harga}")
        print(f"Diskon                : Rp.{diskon}")
        print(f"Total Bayar           : Rp.{total}")
    else:
        print("Kelas invalid")
else:
    print("Kota invalid")