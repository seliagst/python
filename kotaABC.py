print("diketahui:")
jarakA = int(input("masukkan jarak A ke B:"))
kec_A = int(input("masukkan angka A ke B:"))
jarakB = int(input("masukkan jarak B ke C:"))
kec_B = int(input("masukkan angka B ke C:"))
jam = int(input("masukkan jam berangkat:"))
menit = int(input("masukkan menit berangkat:"))
print("waktu berangkat pukul", jam, ".", menit, "WIB")
istirahat = int(input("menit waktu istirahat:"))
print("jawab:")
waktuA = jarakA//kec_A
waktu1 = jarakA%kec_A
waktuB = jarakB//kec_B
waktu2 = jarakB%kec_B
jam_total = waktuA+waktuB+jam
mnt_total = waktu1+waktu2+menit+istirahat
print("jam:", jam_total)
print("mnt:", mnt_total)
mnt = mnt_total//60
waktu = jam_total+mnt
wkt = mnt_total%60
print("Tiba pada pukul:", waktu, ".", wkt, "WIB")







                
