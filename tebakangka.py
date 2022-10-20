import random
angka_rahasia = random.randint(1, 100)
print("hi, my name is Mr. laptop , i have chosen an integer number between 1-100. can you guess what it is!")

nilai = 100

while True:
  jawaban = int(input("\nMasukkan angka: "))
  if jawaban == angka_rahasia:
    print("Tebakanmu benar!")
    break
  else:
    print(
      "sorry,tebakanmu terlalu",
      "kecil" if jawaban < angka_rahasia else "besar"
    )
    nilai -= 5
print("nilai anda :", nilai)
