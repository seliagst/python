jarak = int(input("jarak yang ditempuh:"))
print("perbandinganbbm dengan jarak")
bbm = int(input("masukkan angka:"))
jarak1 = int(input("masukkan angka:"))
print("perbandingan bbm dengan jarak", bbm, ":", jarak1)
bbm_dibutuhkan = jarak/12
print("bbm yang dibutuhkan untuk menempuh jarak", jarak, "adalah", bbm_dibutuhkan)
print("kapasitas tangki mobil adalah 50 lt")
tangki = bbm_dibutuhkan//50
if bbm_dibutuhkan%50 >= 0.5 :
    isi = tangki+1
else:
    isi = tangki
print("isi tangki dilakukuan sebanyak", isi, "kali")
