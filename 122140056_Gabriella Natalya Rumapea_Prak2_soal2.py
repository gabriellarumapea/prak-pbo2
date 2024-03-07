def log_method_execution(method):
    def wrapper(self, *args, **kwargs):
        print(f"Executing {method.__name__}")
        result = method(self, *args, **kwargs)
        print(f"Execution of {method.__name__} completed")
        return result
    return wrapper

class KebunBinatang:
    @log_method_execution
    def __init__(self):
        self.daftar_hewan = []

    @log_method_execution
    def tambah_hewan(self, nama, jenis):
        self.daftar_hewan.append({"nama": nama, "jenis": jenis})
        return f"{nama} (jenis: {jenis}) berhasil ditambahkan ke dalam kebun binatang."

    @log_method_execution
    def tampilkan_informasi(self):
        if not self.daftar_hewan:
            print("Kebun binatang kosong.")
        else:
            print("Daftar hewan dalam kebun binatang:")
            for hewan in self.daftar_hewan:
                print(f"{hewan['nama']} - Jenis: {hewan['jenis']}")

    @log_method_execution
    def __del__(self):
        print("Keluar dari informasi kebun binatang.")

if __name__ == "__main__":
    kebun_binatang = KebunBinatang()

    while True:
        print("\nPilih :")
        print("1. Tambah Hewan")
        print("2. Tampilkan Informasi Kebun Binatang")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            nama_hewan = input("Masukkan nama hewan: ")
            jenis_hewan = input("Masukkan jenis hewan: ")
            kebun_binatang.tambah_hewan(nama_hewan, jenis_hewan)
        elif pilihan == '2':
            kebun_binatang.tampilkan_informasi()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")