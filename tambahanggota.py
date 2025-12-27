import csv


def tambah_anggota():
    print("======MENAMBAHKAN ANGGOTA======")
    
    username = str(input("Masukkan nama lengkap Anggota Baru Perpustakaan: "))
    password = str(input("Masukkan Password dari Anggota baru (Diawali dengan angka 2 dan bejumlah 5 digit): "))
    
    if not (password.isdigit() and len(password) == 5 and password[0] == "2"):
        print("Password tidak valid, harus berjumlah 5 digit dan diawali angka 2")
        return
    
    alamat = str(input("Masukkan Alamat tempat tinggal Anggota baru: "))
    nomer_hp = int(input("Masukkan nomer handphone yang bisa dihubungi: "))
    
    with open("dataAnggotaPerpus.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            username,
            password,
            alamat,
            nomer_hp,
        ])
    
    print(f"Anggota baru sudah ditambahkan, dengan nama {username}")
    
    tambah_lagi = str(input("Apakah ingin menambahkan Anggota Perpustakaan lainnya?(yes/no): " ))
    if tambah_lagi == "yes":
        tambah_anggota()
    else:
        login()
    return
tambah_anggota()