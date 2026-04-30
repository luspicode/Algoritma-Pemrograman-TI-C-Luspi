struktur = {
    "Skripsi_Aku": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    indent = "   " * level
    
    print(indent , nama)

    for item, isi in folder.items():
        if isinstance(isi, dict):  
            tampilkan_tree(isi, item, level + 1)
        else:  
            print("   " * (level + 1) + f"{item} ({isi} KB)")



def total(struktur):
  global ukuran
  global banyak
  global daftar
  for j, i in struktur.items():
    if isinstance(i, int):
      ukuran += i
      banyak += 1
      daftar.append([j, i])
    if isinstance(i, dict):
      total(i)


def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j][1] > arr[j+1][1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

ukuran = 0
banyak = 0
daftar = []


total(struktur)
bubble_sort(daftar)
print('ukuran :', ukuran)
print('jumlah file :', banyak)
print(f'file dengan ukuran terbesar : {daftar[-1][0]} ({daftar[-1][1]} KB)')

for nama_folder, isi_folder in struktur.items():
    tampilkan_tree(isi_folder, nama_folder)

