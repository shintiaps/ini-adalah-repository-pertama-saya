import random

def quiz_matematika_tk():
    """
    Game quiz matematika untuk anak TK dengan penjumlahan (+)
    Soal mudah dengan bilangan 1-10
    """
    
    print("\n" + "🌟" * 25)
    print("HALO! SELAMAT BERMAIN QUIZ MATEMATIKA!")
    print("🌟" * 25)
    print("\nSoal: Penjumlahan (+)")
    print("Bilangan: 1 - 10")
    print("Jawab dengan benar untuk dapat bintang! ⭐")
    print("=" * 50 + "\n")
    
    # Input nama pemain
    nama = input("Nama kamu siapa? ").strip()
    if not nama:
        nama = "Teman"
    
    print(f"\nHai {nama}, ayo main!\n")
    
    bintang = 0  # Jumlah bintang yang dikumpulkan
    soal_no = 1
    benar = 0
    salah = 0
    
    # Looping soal dengan bilangan mudah
    while True:
        print(f"Soal {soal_no} ⭐ Bintang: {bintang}")
        print("-" * 30)
        
        # Generate bilangan random antara 1-10 (cocok untuk TK)
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        
        # Hitung jawaban yang benar
        jawaban_benar = angka1 + angka2
        
        # Tampilkan soal dengan format sederhana
        print(f"   {angka1} + {angka2} = ?\n")
        
        # Ambil input jawaban dari pemain
        try:
            jawaban_pemain = int(input("Jawaban mu: "))
        except ValueError:
            print("⚠️  Masukkan angka yang benar ya!\n")
            continue
        
        # Periksa jawaban
        if jawaban_pemain == jawaban_benar:
            bintang += 1
            benar += 1
            print(f"\n🎉 BENAR! Jawaban: {jawaban_benar}")
            print("Dapat bintang! ⭐\n")
        else:
            salah += 1
            print(f"\n😅 Kurang tepat. Jawaban yang benar: {jawaban_benar}")
            print("Coba lagi di soal berikutnya!\n")
        
        print(f"Bintang sekarang: {bintang}\n")
        
        soal_no += 1
        
        # Tanya apakah ingin melanjutkan atau selesai
        if soal_no > 1:
            print("-" * 30)
            print("Mau lanjut? (y=ya / n=selesai): ", end="")
            lanjut = input().lower().strip()
            
            if lanjut != 'y':
                break
            print()
    
    # Hasil akhir
    print("\n" + "=" * 50)
    print("🏆 SELESAI! BAGUS SEKALI! 🏆")
    print("=" * 50)
    print(f"Nama: {nama}")
    print(f"Bintang yang dikumpulkan: {bintang} ⭐")
    print(f"Jawaban Benar: {benar}")
    print(f"Jawaban Salah: {salah}")
    print(f"Total Soal: {soal_no - 1}")
    print("=" * 50 + "\n")


def main():
    """Fungsi utama untuk menjalankan game"""
    while True:
        quiz_matematika_tk()
        
        # Tanya apakah ingin bermain lagi
        print("Mau bermain lagi? (y=ya / n=tidak): ", end="")
        lagi = input().lower().strip()
        
        if lagi != 'y':
            print("\n👋 Sampai jumpa lagi! Terima kasih sudah bermain!")
            print("Semangat belajar! 🌟\n")
            break
        print()


if __name__ == "__main__":
    main()
