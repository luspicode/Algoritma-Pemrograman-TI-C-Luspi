#Match (switch di C)

day = 11
match day:
  case 1:
    print("Senin")
  case 2:
    print("Selasa")
  case 3:
    print("Rabu")
  case 4:
    print("Kamis")
  case 5:
    print("Jumat")
  case 6:
    print("Sabtu")
  case 7:
    print("Minggu")
  case _:
    print("hari ga valid")
"""
-------------------------------------------------------------------
"""
#gabungkan beberapa nilai
angka = 4
match angka:
  case 1 | 3 | 5 | 7 | 9:
    print("angka genap dibawah sepuluh")
  case 0 | 2 | 4 | 6 | 8:
    print("angka genap dibawah sepuluh!")
    """
-------------------------------------------------------------------
"""