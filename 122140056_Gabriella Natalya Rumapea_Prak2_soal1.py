class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def method_1(self):
        return len(self.__nama)

    def method_2(self):
        return f"MHS{self.__nim} - {self.angkatan}"

    def method_3(self):
        if self.isMahasiswa:
            return "Mahasiswa aktif"
        else:
            return "Bukan mahasiswa aktif"

nim_mahasiswa1 = input("Masukkan NIM mahasiswa 1: ")
nama_mahasiswa1 = input("Masukkan nama mahasiswa 1: ")
angkatan_mahasiswa1 = int(input("Masukkan angkatan mahasiswa 1: "))
is_mahasiswa1 = input("Apakah benar masih menjadi mahasiswa aktif (y/n)? ").lower() == 'y'

nim_mahasiswa2 = input("Masukkan NIM mahasiswa 2: ")
nama_mahasiswa2 = input("Masukkan nama mahasiswa 2: ")
angkatan_mahasiswa2 = int(input("Masukkan angkatan mahasiswa 2: "))

mahasiswa1 = Mahasiswa(nim_mahasiswa1, nama_mahasiswa1, angkatan_mahasiswa1, is_mahasiswa1)
mahasiswa2 = Mahasiswa(nim_mahasiswa2, nama_mahasiswa2, angkatan_mahasiswa2)

print("Mahasiswa 1")
print("Panjang nama:", mahasiswa1.method_1())
print("NIM dengan awalan MHS:", mahasiswa1.method_2())
print("Status mahasiswa:", mahasiswa1.method_3())

print("\nMahasiswa 2")
print("Panjang nama:", mahasiswa2.method_1())
print("NIM dengan awalan MHS:", mahasiswa2.method_2())
print("Status mahasiswa:", mahasiswa2.method_3())
