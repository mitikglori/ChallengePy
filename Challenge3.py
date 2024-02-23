from datetime import date as dt
print("<<{:^21}>>".format("UMUR"))
print("-"*25)
print("Tuliskan tanggal, bulan dan tahun.")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan   : "))
tahun = int(input("Tahun   : "))
tgl_lahir = dt(tahun, bulan, tanggal)
today = dt.today()
print(f"Tanggal Lahir    : {tgl_lahir}") 
print(f"Tanggal Hari Ini : {today}") 
selisih = today - tgl_lahir
usia_tahun = selisih.days//365
usia_bulan = int((selisih.days%365)//30)
print(f"Umur anda {usia_tahun} dan {usia_bulan} bulan")