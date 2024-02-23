x = int(input("x : "))
y = int(input("y : "))
if(x>0 and y>0):
    print(f"Koordinat {x,y} berada di kuadran I")
elif(x>0 and y<0):
    print(f"Koordinat {x,y} berada di kuadran IV")
elif(x<0 and y>0):
    print(f"Koordinat {x,y} berada di kuadran II")
elif(x<0 and y<0):
    print(f"Koordinat {x,y} berada di kuadran III")
elif(x==0 and y == 0):
    print(f"Koordinat {x,y} berada di titik pusat")
elif(x==0 and y!=0):
    print(f"Koordinat {x,y} berada di sumbu x pos")
elif(x!=0 and y==0):
    print(f"Koordinat {x,y} berada di sumbu y pos")
    