print("{:^20}" .format("Latihan"))
print("Berikut akan tampil list dengan kondisi : ")
print("""
    1. range(1,100)
    2. value/item : genap(i>=10 dan i<=20)
    3. value/item ; ganjil(i>=90 and i<=100)
    
    [10,12,14,16,18,20,91,93,95,97,99]
      """)
list = []
for n in range(100):
    if 10<=n<=20 and n%2==0:
        list.append(n)
    elif 90<=n<=100 and n%2==1:
        list.append(n)
print(list)
    