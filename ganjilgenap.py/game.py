import random

# Daftar kata untuk game hangman dengan clue
DAFTAR_KATA = [
    ("python", "Bahasa pemrograman yang populer dan mudah dipelajari"),
    ("hangman", "Game tebak kata dengan karakter yang menggantung"),
    ("komputer", "Mesin elektronik untuk memproses data dan informasi"),
    ("programmer", "Orang yang menulis kode program"),
    ("keyboard", "Perangkat input dengan tombol untuk mengetik"),
    ("monitor", "Perangkat output yang menampilkan gambar atau teks"),
    ("internet", "Jaringan global yang menghubungkan komputer di seluruh dunia"),
    ("game", "Permainan atau hiburan interaktif"),
    ("bintang", "Benda langit yang bersinar di malam hari"),
    ("pembelajaran", "Proses memperoleh pengetahuan dan keterampilan"),
    ("matahari", "Bintang terbesar di tata surya kita"),
    ("bulan", "Satelit alami yang mengelilingi bumi"),
    ("segitiga", "Bangun datar dengan 3 sisi dan sudut 180 derajat"),
    ("persegi", "Bangun datar dengan 4 sisi sama panjang"),
    ("lautan", "Kumpulan air asin yang luas di bumi"),
    ("pantai", "Daerah pertemuan antara laut dan daratan"),
    ("hutan", "Area luas yang penuh dengan pohon-pohon"),
    ("anjing", "Hewan peliharaan berbulu yang setia"),
    ("kucing", "Hewan peliharaan kecil yang mandiri dan lincah"),
    ("burung", "Hewan yang dapat terbang dengan sayap"),
    ("ikan", "Hewan air yang bergerak dengan sirip"),
    ("mobil", "Kendaraan darat beroda empat untuk transportasi"),
    ("motor", "Kendaraan beroda dua yang cepat"),
    ("pesawat", "Kendaraan udara untuk penerbangan jarak jauh"),
    ("kereta", "Kendaraan darat yang bergerak di atas rel"),
    ("jembatan", "Struktur yang menghubungkan dua tempat yang terpisah"),
    ("rumah", "Bangunan tempat tinggal manusia")
]

# Gambar Hangman untuk setiap tahap
GAMBAR_HANGMAN = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   \\|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   \\|/
       |    |
       |   / \\
    --------
    """
]
# Hangman yang sedih untuk game over
HANGMAN_SEDIH = """
   ------
   |    |
   |    O_O
   |   \\|/
   |    |
   |   / \\
--------

😭 KAMU GAGAL! 😭
"""

def tampilkan_gambar(kesalahan):
    """Menampilkan gambar hangman sesuai jumlah kesalahan"""
    if kesalahan < len(GAMBAR_HANGMAN):
        print(GAMBAR_HANGMAN[kesalahan])
    else:
        print(GAMBAR_HANGMAN[-1])


def tampilkan_status_kata(kata, huruf_ditebak):
    """Menampilkan kata dengan huruf yang sudah ditebak"""
    tampilan = ""
    for huruf in kata:
        if huruf in huruf_ditebak:
            tampilan += huruf + " "
        else:
            tampilan += "_ "
    return tampilan


def main_hangman():
    """Fungsi main untuk game Hangman"""
    
    print("\n" + "=" * 60)
    print("🎮 SELAMAT DATANG DI GAME HANGMAN! 🎮".center(60))
    print("=" * 60)
    print("\nTebak kata tersembunyi sebelum hangman selesai!")
    print("⚠️  Batas kesalahan: 5 kali")
    print("⭐ Setiap tebakan benar = +1 bintang\n")
    
    # Input nama pemain
    nama = input("Nama kamu siapa? ").strip()
    if not nama:
        nama = "Petualang"
    
    print(f"\nHai {nama}, selamat bermain! 😊\n")
    
    bintang = 0
    permainan_berlanjut = True
    
    while permainan_berlanjut:
        # Pilih kata acak beserta clue-nya
        kata, clue = random.choice(DAFTAR_KATA)
        kata = kata.lower()
        huruf_ditebak = set()
        kesalahan = 0
        benar_tebak = False
        
        print("=" * 60)
        print("🎮 PERMAINAN BARU 🎮")
        print("=" * 60)
        print(f"Panjang kata: {len(kata)} huruf")
        print(f"💡 Clue: {clue}")
        print(f"Kesalahan tersisa: {5 - kesalahan} dari 5")
        print(f"Bintang: {bintang} ⭐\n")
        
        # Loop tebakan
        while kesalahan < 5:
            tampilkan_gambar(kesalahan)
            
            print(f"\nKata: {tampilkan_status_kata(kata, huruf_ditebak)}")
            print(f"Huruf yang sudah ditebak: {', '.join(sorted(huruf_ditebak)) if huruf_ditebak else 'Belum ada'}")
            print(f"Kesalahan: {kesalahan}/5")
            
            # Input tebakan dari pemain
            tebakan = input("\nTebak huruf (a-z) atau ketik kata lengkapnya: ").lower().strip()
            
            if not tebakan:
                print("⚠️  Masukkan huruf atau kata!")
                continue
            
            # Jika tebakan adalah kata lengkap
            if len(tebakan) > 1:
                if tebakan == kata:
                    benar_tebak = True
                    bintang += 5
                    print(f"\n🎉 BENAR! Kata adalah '{kata}'!")
                    print(f"Dapat 5 bintang! ⭐⭐⭐⭐⭐")
                    break
                else:
                    kesalahan += 1
                    bintang -= 1
                    if bintang < 0:
                        bintang = 0
                    print(f"\n❌ Salah! Kata bukan '{tebakan}'")
                    print(f"Kesalahan +1 (Sisa: {5 - kesalahan})")
                    print(f"Bintang berkurang -1! (Sisa: {bintang} ⭐)")
                    continue
            
            # Jika tebakan adalah huruf
            if len(tebakan) != 1:
                print("⚠️  Masukkan satu huruf saja!")
                continue
            
            if tebakan in huruf_ditebak:
                print("⚠️  Huruf ini sudah pernah ditebak!")
                continue
            
            huruf_ditebak.add(tebakan)
            
            # Periksa tebakan
            if tebakan in kata:
                bintang += 1
                print(f"\n✓ BENAR! Huruf '{tebakan}' ada di kata")
                print(f"Dapat 1 bintang! ⭐")
                
                # Cek apakah semua huruf sudah ditebak
                if all(huruf in huruf_ditebak for huruf in kata):
                    benar_tebak = True
                    print(f"\n🎉 BENAR! Kata adalah '{kata}'!")
                    break
            else:
                kesalahan += 1
                bintang -= 1
                if bintang < 0:
                    bintang = 0
                print(f"\n❌ SALAH! Huruf '{tebakan}' tidak ada di kata")
                print(f"Kesalahan +1 (Sisa: {5 - kesalahan})")
                print(f"Bintang berkurang -1! (Sisa: {bintang} ⭐)")
        
        # Cek kondisi akhir permainan
        if kesalahan >= 5:
            print(HANGMAN_SEDIH)
            print(f"Kata yang benar: '{kata}'")
            print(f"💡 Clue: {clue}")
            print(f"\n😢 Jangan menyerah! Coba lagi di permainan berikutnya!\n")
        elif benar_tebak:
            print(f"\nTotal bintang sekarang: {bintang} ⭐\n")
        
        # Tanya lanjut bermain
        print("=" * 60)
        print(f"Total Bintang: {bintang} ⭐")
        print("Ingin bermain lagi? (y=ya / n=tidak): ", end="")
        lanjut = input().lower().strip()
        
        if lanjut != 'y':
            permainan_berlanjut = False
    
    # Hasil akhir
    print("\n" + "=" * 60)
    print("🏆 PERMAINAN SELESAI! TERIMA KASIH TELAH BERMAIN 🏆".center(60))
    print("=" * 60)
    print(f"Nama Pemain: {nama}")
    print(f"Total Bintang yang Dikumpulkan: {bintang} ⭐")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main_hangman()
