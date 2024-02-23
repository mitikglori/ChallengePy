print("<<{:^25}>>".format("PENJUALAN"))
Harga = int(input("Masukan Harga       : Rp."))
qty = int(input("Masukan Jumlah beli : "))
subtotal = Harga*qty
if qty >=12:
    diskon = 0.2 * subtotal
else:
    diskon = 0
Total = subtotal - diskon
print(f"Subtotal            : Rp.{subtotal},00")
print(f"Diskon              : Rp.{diskon},00")
print(f"Total               : Rp.{float(Total)},00")