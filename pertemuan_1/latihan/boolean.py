#Boolean
#True
print(bool(10 > 9))
print(bool(-1))
print(bool('Hy all'))
print(bool(' '))
listberisi = [0]  # list, tuple, set (), [], {}
print(bool(listberisi))
"""
-----------------------------------------------------------------------------------------------
"""
# False
print(bool(False))
print(bool(0))
print(bool(""))
listkosong = []  # list, tuple, set (),[],{}
print(bool(listkosong))
print(bool(()))
print(bool([]))
print(bool({}))
"""
-----------------------------------------------------------------------------------------------
"""
# Fungsi bisa mengembalikann nilai boolean
def myFunc():
    return True
print(myFunc())
"""
-----------------------------------------------------------------------------------------------
"""
# fungsi isinstance
# Menentukan apakah sebuah objek merupakan tipe data teretentu
# isintance(objek, data type)
y = 200
print(isinstance(y, int))
print(isinstance(y, float))
"""
-----------------------------------------------------------------------------------------------
"""