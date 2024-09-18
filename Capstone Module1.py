import getpass
from tabulate import tabulate
from colorama import init, Fore

# Inisialisasi colorama
init(autoreset=True)

# Database pasien sebagai list of dictionaries
pasien_db = [
    {'id': 1001, 'nama': 'Rafli', 'umur': 20, 'jenis kelamin': 'M', 'golongan darah': 'A'},
    {'id': 1002, 'nama': 'Kevin', 'umur': 45, 'jenis kelamin': 'M', 'golongan darah': 'B'},
    {'id': 1003, 'nama': 'Tiara', 'umur': 50, 'jenis kelamin': 'F', 'golongan darah': 'O'},
    {'id': 1004, 'nama': 'Grace', 'umur': 40, 'jenis kelamin': 'F', 'golongan darah': 'AB'},
    {'id': 1005, 'nama': 'Agung', 'umur': 27, 'jenis kelamin': 'M', 'golongan darah': 'B'}
]


def print_table(data):
    headers = ['ID', 'Nama', 'Umur', 'Jenis Kelamin', 'Golongan Darah']
    table = [[i['id'], i['nama'], i['umur'], i['jenis kelamin'], i['golongan darah']] for i in data]
    print(tabulate(table, headers, tablefmt='pretty'))

def find_patient(patient_id):
    for i in pasien_db:
        if i['id'] == patient_id:
            return i
    return None

def validate_jenis_kelamin(jenis_kelamin):
    jenis_kelamin = jenis_kelamin.upper()
    if jenis_kelamin not in ['M', 'F']:
        raise ValueError("Jenis kelamin harus M atau F.")
    return jenis_kelamin

def validate_golongan_darah(golongan_darah):
    golongan_darah = golongan_darah.upper()
    valid_golongan = ['A', 'B', 'AB', 'O']
    if golongan_darah not in valid_golongan:
        raise ValueError(Fore.RED + "Golongan darah tidak valid. Harus salah satu dari A, B, AB, O.")
    return golongan_darah


# 1. Read
def view_patients():
    while True:
        print("1. Lihat semua data pasien")
        print("2. Lihat data pasien berdasarkan ID")
        choice = input("Pilih opsi (1-2): ").strip()
        if choice == '1':
            if pasien_db:
                print_table(pasien_db)
            else:
                print(Fore.RED + "Tidak ada data pasien!")
            break
        elif choice == '2':
            try:
                patient_id = int(input("Masukkan ID Pasien: "))
                patient = find_patient(patient_id)
                if patient:
                    print_table([patient])
                else:
                    print(Fore.RED + "Pasien tidak ditemukan!")
                break
            except ValueError:
                print(Fore.RED + "Input tidak valid! Pastikan ID adalah angka.")
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan pilih antara 1-2.")


# 2. Create
def add_patient():
    while True:
        try:
            new_id = int(input("Masukkan ID Pasien: "))
            if find_patient(new_id):
                print(Fore.RED + "ID sudah ada. Masukkan ID lain.")
                continue
            new_nama = str(input("Masukkan Nama Pasien: ").strip().capitalize())
            new_umur = int(input("Masukkan Umur Pasien: "))
            new_jenis_kelamin = validate_jenis_kelamin(input("Masukkan Jenis Kelamin Pasien (M/F): ").strip())
            new_golongan_darah = validate_golongan_darah(input("Masukkan Golongan Darah Pasien: ").strip())
            
            new_patient = {
                'id': new_id,
                'nama': new_nama,
                'umur': new_umur,
                'jenis kelamin': new_jenis_kelamin,
                'golongan darah': new_golongan_darah
            }
            pasien_db.append(new_patient)
            print(Fore.GREEN + "Pasien berhasil ditambahkan!")
            break
        except ValueError as e:
            print(Fore.RED + f"Error: {e}")


# 3. Update 
def update_patient():
    while True:
        try:
            patient_id = int(input("Masukkan ID Pasien yang akan diupdate: "))
            patient = find_patient(patient_id)
            if not patient:
                print(Fore.RED + "Pasien tidak ditemukan!")
                continue
            
            print("Masukkan data baru (tekan Enter untuk tetap dengan data lama):")
            new_nama = str(input(f"Nama ({patient['nama']}): ").strip()) or patient['nama']
            new_umur = int(input(f"Umur ({patient['umur']}): ").strip())
            new_jenis_kelamin = input(f"Jenis Kelamin ({patient['jenis kelamin']}): ").strip()
            new_golongan_darah = input(f"Golongan Darah ({patient['golongan darah']}): ").strip()
            
            if new_umur:
                patient['umur'] = int(new_umur)
            if new_jenis_kelamin:
                patient['jenis kelamin'] = validate_jenis_kelamin(new_jenis_kelamin)
            if new_golongan_darah:
                patient['golongan darah'] = validate_golongan_darah(new_golongan_darah)
            
            patient['nama'] = new_nama
            print(Fore.GREEN + "Data pasien berhasil diupdate!")
            break
        except ValueError as e:
            print(Fore.RED + f"Error: {e}")

# 4. Delete  
def delete_patient():
    while True:
        try:
            patient_id = int(input("Masukkan ID Pasien yang akan dihapus: "))
            patient = find_patient(patient_id)
            if not patient:
                print(Fore.RED + "Pasien tidak ditemukan!")
                continue
            
            pasien_db.remove(patient)
            print(Fore.GREEN + "Pasien berhasil dihapus!")
            break
        except ValueError:
            print(Fore.RED + "Input tidak valid! Pastikan ID adalah angka.")

# Fitur password
def admin_login():
    password = getpass.getpass("Masukkan password admin: ")
    return password == "admin123"  # Ganti dengan password admin yang diinginkan

# Menu Utama dan Sub-menu Admin dan Visitor 
def main():
    while True:
        print("\n----- Sistem Data Pasien Rumah Sakit -----")
        print("1. Lihat Data Pasien (Visitor)")
        print("2. Masuk sebagai Admin")
        print("3. Keluar")

        choice = input("Pilih opsi (1-3): ").strip()
        if choice == '1':
            view_patients()
        elif choice == '2':
            if admin_login():
                while True:
                    print("\n----- Menu Admin -----")
                    print("1. Lihat Data Pasien")
                    print("2. Tambah Data Pasien")
                    print("3. Update Data Pasien")
                    print("4. Hapus Data Pasien")
                    print("5. Keluar")

                    admin_choice = input("Pilih opsi (1-5): ").strip()
                    if admin_choice == '1':
                        view_patients()
                    elif admin_choice == '2':
                        add_patient()
                    elif admin_choice == '3':
                        update_patient()
                    elif admin_choice == '4':
                        delete_patient()
                    elif admin_choice == '5':
                        print(Fore.GREEN + "Keluar dari menu admin.")
                        break
                    else:
                        print(Fore.RED + "Pilihan tidak valid. Silakan pilih antara 1-5.")
            else:
                print(Fore.RED + "Password salah!")
        elif choice == '3':
            print(Fore.GREEN + "  ----- Terima kasih! ----- \nBerhasil keluar dari program!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid. Silakan pilih antara 1-3.")

if __name__ == "__main__":
    main()
