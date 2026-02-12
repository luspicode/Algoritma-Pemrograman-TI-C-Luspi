nilai = [80, 75, 90, 60, 85]
def hitung (nilai):
  if len(nilai) == 0 :
    return "Data Kosong"
  return sum(nilai)/len(nilai)

ratarata = hitung(nilai)
print(ratarata)