sisi_depan = int(input("Masukkan sisi depan :"))
sisi_tegak = int(input("Masukkan sisi tegak :"))
sisi_miring = int(input("Masukkan sisi miring :"))

if sisi_miring == (sisi_depan ** 2 + sisi_tegak ** 2)**(0.5) :
    print("->Benar")
else :
    print("->Salah")
