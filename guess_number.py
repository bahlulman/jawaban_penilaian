"""
Created on Wed Nov 13 09:43:25 2024

Creator : Abiyyu Daffa Hidastya
Kelas   : IK-1B
"""

def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3
    
    while guess < guess_limit:
        user = int(input("masukkan angka > "))
        if user == secret_number:
            print("selamat, anda berhasil menemukan angkanya")
            break
        else:
            print("salah")
            guess += 1
    else:
        print(f"anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")