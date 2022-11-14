def Pythagoras(a, b, c):
    if c**2 == a**2 + b**2:
        print("->Benar")
    else :
        print("->Salah")
x = int(input("Jumlah Percobaan:"))        
for i in range(x):
    Pythagoras(int(input("Nilai a:")), int(input("Nilai b:")), int(input("Nilai c:")))

