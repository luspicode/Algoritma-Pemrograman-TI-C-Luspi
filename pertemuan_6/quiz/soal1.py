data = [["Algoritma", 2000], ["Basis Data", 2500], ["C", 3000], ["List", 3500], ["Dicti", 1000]]

for buku in range(len(data)):
  print(f'{buku+1}. Nama Buku : {data[buku][0]}')
  print(f'   Denda Keterlambatan Buku : {data[buku][1]}')
  
pilihan = int(input('masukkan nomor buku 1/2/3/4/5 : '))

if pilihan == 1:
  print(f'Nama Buku : {data[0][0]}')
  print(f'Denda Keterlambatan Buku : {data[0][1]}')

elif pilihan == 2:
  print(f'Nama Buku : {data[1][0]}')
  print(f'Denda Keterlambatan Buku : {data[1][1]}')
  
elif pilihan == 3:
  print(f'Nama Buku : {data[2][0]}')
  print(f'Denda Keterlambatan Buku : {data[2][1]}')
  
elif pilihan == 4:
  print(f'Nama Buku : {data[3][0]}')
  print(f'Denda Keterlambatan Buku : {data[3][1]}')
  
elif pilihan == 5:
  print(f'Nama Buku : {data[4][0]}')
  print(f'Denda Keterlambatan Buku : {data[4][1]}')
  
else:
  print('nomor tidak valid')