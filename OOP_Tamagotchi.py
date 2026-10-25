class KucingHantu:
    def __init__(self, nama):

        self.nama = nama
        self.energi = 100
        self.level_seram = 10
        self.status_gentayangan = True

    def beri_makan(self):
        # makan
        self.energi += 20
        print(f"👻 {self.nama} enak! Energi bertambah (Energi: {self.energi})")

    def menakuti_warga(self):
        # menakuti
        if self.energi > 15:
            self.level_seram += 15
            self.energi -= 15
            print(f"😱 {self.nama} wow! Warga lari ketakutan! Level Seram naik: {self.level_seram}")
        else:
            print(f"😴 {self.nama} terlalu lemas untuk menakuti warga, istirahat dulu!")

    def istirahat(self):
        # tidur
        self.energi = 100
        print(f"💤 {self.nama} tidur nyenyak di bawah pohon kamboja. Energi penuh!")

    def info_peliharaan(self):
        # status
        print("=== STATUS KUCING HANTU ===")
        print(f"Nama Kucing        : {self.nama}")
        print(f"Energi             : {self.energi}")
        print(f"Level Seram        : {self.level_seram}")
        print(f"Status Gentayangan : {self.status_gentayangan}")
        print("---------------------------")


# uji
peliharaan1 = KucingHantu("Cimol (The Ghost)")

peliharaan1.info_peliharaan()
print()

peliharaan1.menakuti_warga()
peliharaan1.beri_makan()
print()

peliharaan1.info_peliharaan()
print()

peliharaan1.istirahat()
peliharaan1.info_peliharaan()