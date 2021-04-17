import random
def pemilihan():
    print("===" * 15)
    print("    PEMILIHAN KELOMPOK OSPEK JURUSAN")
    print("===" * 15)
    print("")
    kelompok = ["Antasari", "Diponegoro", "Hasanuddin", "Patimura", "Mangkubumi"]
    print("Berikut daftar kelompok Ospek Jurusan:")
    print(kelompok)
    print('')
    pilih = random.choice(kelompok)
    name = input("Nama Lengkap : ")
    nama = name.upper()
    NIM = input("NIM : ")
    nim = NIM.capitalize()
    print("")
    print("Selamat untuk", nama,"dengan NIM", nim, "bergabung dalam kelompok", pilih.upper(),"!!!!")
pemilihan()