a = int(input("masukkan a:"))
b = int(input("masukkan b:"))
for i in range(b-a+1):
    bil = i+a
    if bil % 3 == 0:
        print(bil)
