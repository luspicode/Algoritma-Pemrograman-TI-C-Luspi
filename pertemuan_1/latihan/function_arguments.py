# Informasi dapat dikirim ke fungsi sebagai argumen, ditulis dalam tanda kurung setelah nama fungsi, dan dipisahkan koma.
def my_function(nama):
    print(nama + " anak hebat")

my_function("wellin")
my_function("fazl")
my_function("radit")

# Parameter vs Argument
# Parameter adalah variabel dalam definisi fungsi
# Argument adalah nilai nyata yang dikirim saat fungsi dipanggil
def greet(nama):  # nama adalah parameter
    print("Hello", nama)
greet("Emil")  # Emil adalah argumen
"""
-----------------------------------------------------------------------------------------------
"""
# Jumlah argumen harus sesuai
def full_name(namadepan, namabelakang):
    print(namadepan + " " + namabelakang)

full_name("fazl", "wilmar")
"""
-----------------------------------------------------------------------------------------------
"""
# Default parameter values
def my_function(nama = "friend"):
  print("Hello", nama)

my_function("Emil")
my_function("Tobias")
my_function() #kalo kosong gini yang dipake yang default/ yang ssama dengan diatas
my_function("Linus")
"""
-----------------------------------------------------------------------------------------------
"""
# Keyword arguments
def my_function(hewan, nama):
  print("I have a", hewan)
  print("My", hewan + "'s name is", nama)
my_function(hewan = "cat", nama = "bobo")  # urutan tidak masalah
"""
-----------------------------------------------------------------------------------------------
"""
# Positional arguments
def my_function(hewan, nama):
  print("I have a", hewan)
  print("My", hewan + "'s name is", nama)
my_function("cat", "bobo")
# urutan penting dalam positional argument
"""
-----------------------------------------------------------------------------------------------
"""
# Campuran positional dan keyword arguments
def my_function(hewan, nama, age):
  print("I have a", age, "year old", hewan, "named", nama)
my_function("cat", nama = "bobo", age = 5)
"""
-----------------------------------------------------------------------------------------------
"""
# Mengirim berbagai tipe data
# Misalnya mengirim list sebagai argumen:
def my_function(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits = ["durian", "pisang", "pepaya"]
my_function(my_fruits)
"""
-----------------------------------------------------------------------------------------------
"""
# Return values
# Fungsi dapat mengembalikan nilai dengan menggunakan pernyataan return:
def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result)
"""
-----------------------------------------------------------------------------------------------
"""
# Fungsi dapat mengembalikan tipe data apa saja seperti list, tuple, dictionari, dll.
# Return list
def my_function():
  return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
"""
-----------------------------------------------------------------------------------------------
"""
# Return tuple
def my_function():
  return (10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)
"""
-----------------------------------------------------------------------------------------------
"""
# Positional-only arguments (gunakan /)
def my_function(nama, /):
  print("Hello", nama)
my_function("Emil")
"""
-----------------------------------------------------------------------------------------------
"""
# Keyword-only arguments (gunakan tanda *)
def my_function(*, nama):
  print("Hello", nama)
my_function(nama = "Emil")
"""
-----------------------------------------------------------------------------------------------
"""
# Kombinasi positional-only dan keyword-only
def my_function(a, b, /, *, c, d):
  return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)
"""
-----------------------------------------------------------------------------------------------
"""