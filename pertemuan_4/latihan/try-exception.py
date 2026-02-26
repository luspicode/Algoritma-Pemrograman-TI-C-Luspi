try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

else:
    print("Perhitungan berhasil dilakukan.")

finally:
    print("Program selesai dijalankan.")