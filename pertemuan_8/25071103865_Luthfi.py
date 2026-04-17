# ===Bagian A=== (Fungsi Inti)

def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
  """Fungsi ini berisi decision untuk menentukan siapa yang menang"""
  if pilihan_pemain == pilihan_komputer:
    return 'seri'
  elif pilihan_pemain == 'gunting' and pilihan_komputer == 'kertas':
    return 'pemain'
  elif pilihan_pemain == 'kertas' and pilihan_komputer == 'batu':
    return 'pemain'
  elif pilihan_pemain == 'batu' and pilihan_komputer == 'gunting':
    return 'pemain'
  else:
    return 'komputer'

def main_satu_giliran(nomor_giliran):
  """Fungsi ini untuk main (termasuk perulangan berapa kali mau main)"""
  nomor_ronde = 0
  nama_pemain = input('masukkan nama anda : ')
  pemain = 0
  komputer = 0
  
  while (pemain <3) and (komputer <3):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_ronde % len(DAFTAR_PILIHAN)] 
    pilihan_pemain = input('pilih (batu/gunting/kertas) : ')
    print('pilihan pemain | pilihan komputer')

    if (pilihan_pemain == 'gunting') or (pilihan_pemain == 'batu') or (pilihan_pemain == 'kertas'):
      print(f'{pilihan_pemain:<13}  |  {pilihan_komputer}')
      
    else:
      print('pilihan tidak valid, pilih lagi (batu/gunting/kertas) : ')
      continue

    riwayat_per_giliran = main_satu_ronde(nama_pemain, pilihan_pemain, pilihan_komputer, pemain, komputer)
    nomor_ronde += 1
    pemain = riwayat_per_giliran[1]
    komputer = riwayat_per_giliran[2]

  return riwayat_per_giliran
def main_satu_ronde(nama_pemain, pilihan_pemain, pilihan_komputer, pemain, komputer):
  """mainin satu ronde, panggil fungsi tentukan pemenang"""

  hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
  if hasil == 'pemain':
    pemain += 1
  elif hasil == 'komputer':
    komputer += 1
  else:
    pass
  return [nama_pemain, pemain, komputer]


# ===Bagian B=== (Matriks)
def tampilkan_riwayat(data_lengkap):
  """tampilkan riwayat"""
  print('====================')
  print(f'|  Nama   |  Skor  |')
  print('====================')

  for i in data_lengkap:
    print(f'|  {i[0]:<6} |    {i[1]}   |')
    print('====================')




# ===Bagian C=== (Leaderboard)
def bubble_sort_riwayat(data_lengkap):
  """buat ngesort riwayat (leaderboard)"""
  for i in range(len(data_lengkap)):
    for j in range(0, len(data_lengkap)-i-1):
      if data_lengkap:
        pass

def tampilkan_leaderboard(p):
  """nampilkan liderbord"""



nomor_giliran = 1
DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", "gunting", "kertas", "gunting", "batu"] 
data_lengkap = []
data_lengkap.append(main_satu_giliran(nomor_giliran))

while True:
  pilihan = input('masih mau main? ketik "ya" kalau mau : ').lower()
  if pilihan != 'ya':
    break
  data_lengkap.append(main_satu_giliran(nomor_giliran))

tampilkan_riwayat(data_lengkap)