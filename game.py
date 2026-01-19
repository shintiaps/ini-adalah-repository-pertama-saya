# Game Tebak Angka

angka_rahasia = 2008
max_tebakan = 10
percobaan = 0

print("Clue kecil: Angka rahasia adalah angka 4 digit!")

while percobaan < max_tebakan:
    try:
        tebakan = int(input(f"Percobaan {percobaan+1}/{max_tebakan}: Masukkan tebakan angka: "))
    except ValueError:
        print("Masukkan angka yang valid! 😢")
        continue

    percobaan += 1

    if tebakan == angka_rahasia:
        print(f"Selamat! Tebakan Anda benar! 😊 Anda berhasil dalam {percobaan} percobaan.\n         \\(^_^)/\n            |\n           / \\\n  🎉 YOU WIN! 🎉")
        break
    elif tebakan < angka_rahasia:
        print("Tebakan terlalu kecil! \n   (T_T)\n   /|\\\n   / \\")
    else:
        print("Tebakan terlalu besar! \n   (T_T)\n   /|\\\n   / \\")

else:
    print("Game over! Anda telah mencapai batas maksimal percobaan.\n   (T_T)\n   /|\\\n   / \\")