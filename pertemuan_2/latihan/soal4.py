def pangkat_rekursif(a,b):
  if a == 0:
    return 0
  if b == 0:
      return 1
  return a * pangkat_rekursif(a,b-1)

print(pangkat_rekursif(2,5))