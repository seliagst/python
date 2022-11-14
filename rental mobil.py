jam1 = int(input("masukkan jam brngkt :"))
mnt1 = int(input("masukkan mnt brngkt :"))
print("berangkat pukul", jam1, ".", mnt1)
jam2 = int(input("masukkan jam tiba:"))
mnt2 = int(input("masukkan mnt tiba:"))
print("tiba pukul", jam2, ".", mnt2)
jam3 = jam2-jam1
mnt3 = mnt2-mnt1
jam4 = mnt3/60
jam5 = jam3+jam4
harga1 = 200000
print("lama perjalanan:",jam5)
while True :
    if jam4 >= 12:
        print("Tarif harga sewa: Rp.",harga1*jam5/12)
        break
    else:
        print("jika lama perjalanan lebih dari 12 jam, maka tarif harga sewa:")
        jam6 = jam5-12
        harga2 = harga1+jam6*10000
        print("Rp.",harga2)
        break
        
    


