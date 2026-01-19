# Game Tebak Angka
# Angka rahasia adalah 2008

angka_rahasia = 2008
max_tebakan = 10
percobaan = 0

while percobaan < max_tebakan:
    try:
        tebakan = int(input(f"Percobaan {percobaan+1}/{max_tebakan}: Masukkan tebakan angka: "))
    except ValueError:
        print("Masukkan angka yang valid! 😢")
        continue

    percobaan += 1

    if tebakan == angka_rahasia:
        print(f"Selamat! Tebakan Anda benar! 😊 Anda berhasil dalam {percobaan} percobaan.")
        break
    elif tebakan < angka_rahasia:
        print("Tebakan terlalu kecil! 😢")
    else:
        print("Tebakan terlalu besar! 😢")

else:
    print("Game over! Anda telah mencapai batas maksimal percobaan. 😢")
