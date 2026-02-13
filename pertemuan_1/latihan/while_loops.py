# While loops menjalankan perintah selama kondisinya terpenuhi
i = 0
while i < 5:
   print(i)
   i += 2
print('') #ngasih endline
"""
-----------------------------------------------------------------------------------------------
"""
# BREAK statement
# dengan BREAK kita dapat menghentikan loop bahkan saat kondisinya terpenuhi
j = 1
while j < 6:
   print(j)
   if j == 3:
      break
   j += 1
print('\n')
"""
-----------------------------------------------------------------------------------------------
"""
#CONTINUE statement
# dengan CONTINUE, kita dapat memberhentikan iterasi saat ini dan melanjutkan yang selanjutnya
k = 0
while k < 6:
   k += 1
   if k == 3:
      continue
   print(k)
print('\n')
"""
-----------------------------------------------------------------------------------------------
"""
# ELSE statement
# menjalankan blok code saat kondisi tidak terpenuhi
l = 2
while l < 9:
   print(l)
   l+= 1
else:
   print("sudah melebihi batas")
# blok ELSE ga akan dieksekusi kalau loop berhenti dengan BREAK statement
"""
-----------------------------------------------------------------------------------------------
"""