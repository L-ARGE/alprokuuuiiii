import pandas as pd

def lihat_data_anggota():
    try:
        data_anggota = pd.read_csv("dataAnggotaPerpus.csv")

        if data_anggota.empty:
            print("Belum ada data anggota.")
            return

        print("====== DATA ANGGOTA PERPUSTAKAAN ======")
        print(data_anggota.to_string(index=False))

    except FileNotFoundError:
        print("File data anggota belum tersedia.")
        
lihat_data_anggota()