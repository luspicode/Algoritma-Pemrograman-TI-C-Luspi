#Variables

#Python Variables
x = 6
y = "luspi"
"""
-variabel digunakan untuk menampung nilai
-untuk menambahkan nilai berupa string, gunakan petik (")
----------------------------------------------------------------------------
"""

#Variable Names
angkaku = 6
angka_ku = 6
_angka_ku = 6
angkaKu = 6
ANGKAKU = 6
angkaku1 = 6
"""
-diawali dengan huruf atau underscore (_)
-tidak bisa diawali angka
-nama variabel hanya bisa berisi huruf (a-z), angka (0-9), dan underscore (_)
-huruf besar dan kecil berbeda
-nama variabel ga boleh sama dengan sintaks python
-----------------------------------------------------------------------------
"""

#Assign Multiple Value
x,y,z = 5,6,7
a=b=c="buah"
buah = ["durian", "anggur", "pepaya"]
k,l,m = buah
"""
untuk melakukan assign pada variabel, dapat dilakukan dengan cara diatas
-----------------------------------------------------------------------------
"""


#Output Variables
x = 5
print (x)
x = "luthfi"
y = "krishna"
z = "haryadi"
print (x,y,z)
"""
output variabel dapat dilakukan dengan print variabel tersebut
----------------------------------------------------------------------------
"""

#Global Variable
x = "mantap"
def fungsi ():
  print ("python" + x) #output python mantap
  
fungsi ()
print ("python" + x) 
#-----------------------

def fungsi ():
  global x
  x = "hebat"
  print ("python" + x) #output python hebat
  
fungsi ()
print ("python" + x) #output python hebat
"""
-variabel global adalah variabel yang mewakili semua (terletak diluar)
-jika ingin menjadikan global suatu variabel didalam suatu fungsi, gunakan perintah "global"
"""
