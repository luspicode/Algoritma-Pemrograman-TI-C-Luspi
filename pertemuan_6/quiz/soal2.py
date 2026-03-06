data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]

for buku in range(len(data)):
  print(f'{buku+1}. Nama Buku : {data[buku][0]}')
  print(f'   Denda Keterlambatan Buku : {data[buku][1]}')


judul_buku = []

while True:
  pilihan = int(input('masukkan nomor buku 1/2/3/4/5 (0 untuk keluar) : '))
  if pilihan == 0:
    break
  
  lama_pinjam = int(input('berapa hari ingin meminjam? : '))
  judul_buku.append([data[pilihan][0], lama_pinjam, data[pilihan][1]])
  

print('daftar buku yang anda pinjam dan denda terlambat sehari')
for i in range(len(judul_buku)):
  print(f'{i+1}. {judul_buku[i][0]}, Denda : {judul_buku[i][2]} ')
  
