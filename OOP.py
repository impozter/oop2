class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties (nama, skor = 0, koin = 0, is_running = True)
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari (cetak pesan dan ubah is_running menjadi True)
        self.is_running = True
        print(f"{self.nama} berlari kencang!")

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin dan berikan output informasi
        self.koin += jumlah
        self.skor += jumlah * 10
        print(f"{self.nama} berhasil mendapatkan {jumlah} koin! Total koin: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False dan cetak pesan game over
        self.is_running = False
        print("GAME OVER!")

    def info_player(self):
        # TODO 5: Cetak status terkini (nama, skor, jumlah koin, dan status berlari)
        print("=== STATUS PLAYER ===")
        print(f"Nama           : {self.nama}")
        print(f"Skor           : {self.skor}")
        print(f"Jumlah koin    : {self.koin}")
        print(f"Berlari        : {self.is_running}")
        print("----------------------------------------")


# --- PENGUJIAN OBJEK ---
# Perbaikan: Menggunakan "KarakterSurfer" dan "ambil_koin"
player1 = KarakterSurfer("Jake")
player1.info_player()
print()

player1.berlari()
player1.ambil_koin(5)
print()

player1.info_player()
print()

player1.tabrak_rintangan()
player1.info_player()