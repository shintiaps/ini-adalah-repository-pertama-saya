# Aplikasi game secreat number

secreat_number = 777

guess_number = int(input("Masukkan Tebak Angka:"))

while guess_number != secreat_number:
    print("Tebakan Salah, Silakan Coba Lagi")
    guess_number = int(input("Masukkan Tebakan Angka"))

print("Selamat..!!, Tebakan anda benar!!")
print("Kode ini saya buat di codespace")
