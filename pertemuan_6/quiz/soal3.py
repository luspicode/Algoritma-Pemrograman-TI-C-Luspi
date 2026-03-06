
data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]


while True:
  pilihan = int(input('masukkan nomor buku 1/2/3/4/5 (0 untuk keluar) : '))
  if pilihan == 0:
    break
  terlambat = int(input('berapa lama anda terlambat?: '))
  
  print(f'Buku yang dipinjam : {data[pilihan-1][0]}')
  print(f'Terlambat : {terlambat} hari')
  print(f'Denda : {terlambat*data[pilihan-1][1]}')