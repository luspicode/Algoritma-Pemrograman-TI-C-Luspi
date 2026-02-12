prima = [2]

def bilangan_prima(n):
  for i in range (3, n+1) :
    apakah_prima = True
    for j in range (2, i) :
      if i % j == 0 :
        apakah_prima = False
    if apakah_prima :
      prima.append(i)

bilangan_prima(50)
print (prima)