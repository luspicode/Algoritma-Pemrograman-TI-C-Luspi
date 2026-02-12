
#tambah
def tambah (a,b):
  return a+b

#kurang
def kurang (a,b):
  return a-b

#kali
def kali (a,b):
  return a*b

#bagi
def bagi (a,b):
  if b == 0 :
    print("pembagian tidak dapat dilakukan dengan 0")
  
#modulus
def mod (a,b):
  return a%b

#fibonacci
n = 7
fbnc = []
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range (n) :
  fbnc.append(fibonacci(n-i))
print (fbnc)
