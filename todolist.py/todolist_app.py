import json
import os
from datetime import datetime, timedelta
import time
import threading
from pathlib import Path

# ==================== ASCII ART CHARACTERS ====================
def print_success_character():
    """Menampilkan karakter lucu ASCII art untuk success"""
    success_art = """
    ╔═══════════════════════════════╗
    ║                               ║
    ║        ( ´∀｀)ﾉ                ║
    ║         /つ つ                ║
    ║          ゙ゝ                  ║
    ║                               ║
    ║      🎉 SELESAI! 🎉           ║
    ║                               ║
    ╚═══════════════════════════════╝
    """
    return success_art

def print_celebration():
    """Menampilkan perayaan ASCII art"""
    celebration = """
    ✨✨✨✨✨✨✨✨✨✨
    ║ BAGUS BANGET PEKERJAAN MU! ║
    ✨✨✨✨✨✨✨✨✨✨
    """
    return celebration

def print_dancing_character():
    """Karakter yang sedang menari"""
    dancing = """
    ♪ ♫ ♪
    (´・ω・`)
    ♫ ♪ ♫
    """
    return dancing

def print_reminder_character():
    """Karakter pengingat"""
    reminder = """
    ┏━━━━━━━━━━━━━━━━━┓
    ┃  ⏰ REMINDER! ⏰  ┃
    ┃  Jangan lupa! 🔔  ┃
    ┗━━━━━━━━━━━━━━━━━┛
    """
    return reminder

# ==================== SUCCESS MESSAGES ====================
SUCCESS_MESSAGES = [
    "🎉 Luar Biasa! Tugasmu selesai dengan sempurna!",
    "💪 Anda hebat! Terus semangat!",
    "🌟 Kerjaan bagus! Patut diacungi jempol!",
    "🚀 Wah, cepat sekali! Mantap!",
    "✨ Sempurna! Kamu adalah jagoan!",
    "🏆 Juara! Tidak ada yang bisa mengalahkanmu!",
    "🎯 Target tercapai! Excellent!",
    "💯 100% Sempurna! Gali terus!",
]

# ==================== FILE MANAGEMENT ====================
TASKS_FILE = "tasks.json"

def load_tasks():
    """Memuat tugas dari file JSON"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    """Menyimpan tugas ke file JSON"""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# ==================== REMINDER SYSTEM ====================
class ReminderSystem:
    def __init__(self):
        self.active = True
        self.thread = None
    
    def start(self, tasks):
        """Memulai sistem pengingat di thread terpisah"""
        self.thread = threading.Thread(target=self._check_reminders, args=(tasks,), daemon=True)
        self.thread.start()
    
    def _check_reminders(self, tasks):
        """Memeriksa pengingat secara berkala"""
        while self.active:
            current_time = datetime.now()
            
            for task in tasks:
                if task.get('completed', False):
                    continue
                
                reminder_time_str = task.get('reminder_time', '')
                if not reminder_time_str:
                    continue
                
                try:
                    reminder_time = datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")
                    
                    # Cek jika waktu pengingat sudah tiba dan kurang dari 2 menit yang lalu
                    if reminder_time <= current_time < (reminder_time + timedelta(minutes=2)):
                        if not task.get('reminded', False):
                            self._show_reminder(task)
                            task['reminded'] = True
                            save_tasks(tasks)
                except ValueError:
                    pass
            
            time.sleep(30)  # Cek setiap 30 detik
    
    def _show_reminder(self, task):
        """Menampilkan pengingat"""
        print("\n" + print_reminder_character())
        print(f"📌 Tugas: {task['title']}")
        print(f"⏰ Waktu: {task['reminder_time']}")
        print("🔔 Jangan sampai lupa! 🔔\n")

# ==================== MAIN APPLICATION ====================
class TodoListApp:
    def __init__(self):
        self.tasks = load_tasks()
        self.reminder_system = ReminderSystem()
        self.reminder_system.start(self.tasks)
    
    def clear_screen(self):
        """Membersihkan layar"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def display_menu(self):
        """Menampilkan menu utama"""
        print("\n" + "="*50)
        print("         📝 TODO LIST APPLICATION 📝")
        print("="*50)
        print("1. 📋 Lihat semua tugas")
        print("2. ➕ Tambah tugas baru")
        print("3. ✏️  Edit tugas")
        print("4. ✅ Tandai tugas selesai")
        print("5. 🗑️  Hapus tugas")
        print("6. ⏰ Atur pengingat")
        print("7. 🌟 Lihat statistik")
        print("8. 🚪 Keluar")
        print("="*50)
    
    def display_tasks(self):
        """Menampilkan semua tugas"""
        self.clear_screen()
        print("\n" + "="*60)
        print("                 📋 DAFTAR TUGAS ANDA")
        print("="*60)
        
        if not self.tasks:
            print("\n✨ Tidak ada tugas! Urusanmu sudah selesai semua! ✨")
            print(print_dancing_character())
        else:
            for idx, task in enumerate(self.tasks, 1):
                status = "✅" if task.get('completed', False) else "⭕"
                reminder = f" 🔔 ({task['reminder_time']})" if task.get('reminder_time') else ""
                print(f"\n{idx}. {status} {task['title']}{reminder}")
                if task.get('description'):
                    print(f"   📌 {task['description']}")
                if task.get('completed'):
                    print(f"   ✓ Selesai pada: {task.get('completed_date', 'N/A')}")
        
        print("\n" + "="*60)
        input("\nTekan Enter untuk melanjutkan...")
    
    def add_task(self):
        """Menambah tugas baru"""
        self.clear_screen()
        print("\n" + "="*50)
        print("         ➕ TAMBAH TUGAS BARU")
        print("="*50)
        
        title = input("\n📝 Judul tugas: ").strip()
        if not title:
            print("❌ Judul tidak boleh kosong!")
            return
        
        description = input("📌 Deskripsi (opsional): ").strip()
        
        reminder = input("🔔 Ingin atur pengingat? (y/n): ").strip().lower()
        reminder_time = None
        
        if reminder == 'y':
            print("\n📅 Format waktu: YYYY-MM-DD HH:MM (contoh: 2025-01-28 14:30)")
            reminder_time = input("⏰ Masukkan waktu pengingat: ").strip()
            try:
                datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
            except ValueError:
                print("❌ Format waktu salah! Pengingat tidak disimpan.")
                reminder_time = None
        
        new_task = {
            'id': int(time.time() * 1000),
            'title': title,
            'description': description,
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'completed': False,
            'reminder_time': reminder_time,
            'reminded': False,
            'completed_date': None
        }
        
        self.tasks.append(new_task)
        save_tasks(self.tasks)
        
        print("\n✅ Tugas berhasil ditambahkan!")
        input("Tekan Enter untuk melanjutkan...")
    
    def edit_task(self):
        """Mengedit tugas"""
        if not self.tasks:
            print("\n❌ Tidak ada tugas untuk diedit!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        self.clear_screen()
        print("\n" + "="*50)
        print("         ✏️  EDIT TUGAS")
        print("="*50)
        
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task.get('completed', False) else "⭕"
            print(f"{idx}. {status} {task['title']}")
        
        try:
            choice = int(input("\nPilih nomor tugas yang ingin diedit: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks[choice - 1]
                
                print(f"\n📝 Judul lama: {task['title']}")
                new_title = input("Judul baru (kosongkan untuk tidak mengubah): ").strip()
                if new_title:
                    task['title'] = new_title
                
                print(f"\n📌 Deskripsi lama: {task.get('description', '')}")
                new_desc = input("Deskripsi baru (kosongkan untuk tidak mengubah): ").strip()
                if new_desc:
                    task['description'] = new_desc
                
                save_tasks(self.tasks)
                print("\n✅ Tugas berhasil diperbarui!")
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def complete_task(self):
        """Menandai tugas sebagai selesai"""
        if not self.tasks:
            print("\n❌ Tidak ada tugas untuk diselesaikan!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        self.clear_screen()
        print("\n" + "="*50)
        print("         ✅ TANDAI TUGAS SELESAI")
        print("="*50)
        
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task.get('completed', False) else "⭕"
            print(f"{idx}. {status} {task['title']}")
        
        try:
            choice = int(input("\nPilih nomor tugas yang selesai: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks[choice - 1]
                if task['completed']:
                    print("\n⚠️  Tugas ini sudah selesai!")
                else:
                    task['completed'] = True
                    task['completed_date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    save_tasks(self.tasks)
                    
                    # Tampilkan perayaan
                    self.clear_screen()
                    print(print_success_character())
                    print(print_celebration())
                    
                    import random
                    message = random.choice(SUCCESS_MESSAGES)
                    print(f"\n{message}\n")
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def delete_task(self):
        """Menghapus tugas"""
        if not self.tasks:
            print("\n❌ Tidak ada tugas untuk dihapus!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        self.clear_screen()
        print("\n" + "="*50)
        print("         🗑️  HAPUS TUGAS")
        print("="*50)
        
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task.get('completed', False) else "⭕"
            print(f"{idx}. {status} {task['title']}")
        
        try:
            choice = int(input("\nPilih nomor tugas yang ingin dihapus: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks[choice - 1]
                confirm = input(f"\nKonfirmasi hapus '{task['title']}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    self.tasks.pop(choice - 1)
                    save_tasks(self.tasks)
                    print("\n✅ Tugas berhasil dihapus!")
                else:
                    print("\n❌ Penghapusan dibatalkan!")
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def set_reminder(self):
        """Mengatur pengingat untuk tugas"""
        if not self.tasks:
            print("\n❌ Tidak ada tugas untuk diatur pengingat!")
            input("Tekan Enter untuk melanjutkan...")
            return
        
        self.clear_screen()
        print("\n" + "="*50)
        print("         ⏰ ATUR PENGINGAT")
        print("="*50)
        
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task.get('completed', False) else "⭕"
            reminder = " 🔔" if task.get('reminder_time') else ""
            print(f"{idx}. {status} {task['title']}{reminder}")
        
        try:
            choice = int(input("\nPilih nomor tugas: "))
            if 1 <= choice <= len(self.tasks):
                task = self.tasks[choice - 1]
                print(f"\n📅 Format: YYYY-MM-DD HH:MM (contoh: 2025-01-28 14:30)")
                reminder_time = input("⏰ Masukkan waktu pengingat: ").strip()
                
                try:
                    datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
                    task['reminder_time'] = reminder_time
                    task['reminded'] = False
                    save_tasks(self.tasks)
                    print("\n✅ Pengingat berhasil diatur!")
                except ValueError:
                    print("❌ Format waktu salah!")
            else:
                print("❌ Nomor tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        input("Tekan Enter untuk melanjutkan...")
    
    def show_statistics(self):
        """Menampilkan statistik"""
        self.clear_screen()
        print("\n" + "="*50)
        print("         🌟 STATISTIK TUGAS")
        print("="*50)
        
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.get('completed', False))
        pending = total - completed
        
        print(f"\n📊 Total tugas: {total}")
        print(f"✅ Selesai: {completed}")
        print(f"⭕ Belum selesai: {pending}")
        
        if total > 0:
            percentage = (completed / total) * 100
            print(f"📈 Persentase selesai: {percentage:.1f}%")
            
            # Progress bar
            filled = int(percentage / 5)
            bar = "█" * filled + "░" * (20 - filled)
            print(f"\n[{bar}] {percentage:.1f}%")
        
        # Motivasi
        if completed == total and total > 0:
            print("\n" + print_dancing_character())
            print("🎉 SEMPURNA! SEMUA TUGAS SELESAI! 🎉")
        elif pending > 0:
            print(f"\n💪 Semangat! Masih ada {pending} tugas yang perlu diselesaikan!")
        
        print("\n" + "="*50)
        input("Tekan Enter untuk melanjutkan...")
    
    def run(self):
        """Menjalankan aplikasi"""
        while True:
            self.clear_screen()
            self.display_menu()
            
            choice = input("Pilih menu (1-8): ").strip()
            
            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.edit_task()
            elif choice == '4':
                self.complete_task()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                self.set_reminder()
            elif choice == '7':
                self.show_statistics()
            elif choice == '8':
                self.reminder_system.active = False
                print("\n👋 Terima kasih telah menggunakan TODO LIST! Sampai jumpa! 👋\n")
                break
            else:
                print("❌ Pilihan tidak valid! Coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

# ==================== MAIN ====================
if __name__ == "__main__":
    app = TodoListApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Aplikasi dihentikan. Sampai jumpa!\n")
        app.reminder_system.active = False
