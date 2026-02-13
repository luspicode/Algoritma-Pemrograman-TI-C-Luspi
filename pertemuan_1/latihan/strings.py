#Strings
print ('''test, ini adalah string multiline
       jadi kita bisa kasih jarak gini tanpa buat print baru''')
"""
-didalam string (') dan (") sama
-untuk menggunakan multiline string, kita harus menggunakan tanda petik tiga kali seperti dicontoh
------------------------------------------------------------------------------------------------------
"""

#Slicing Strings
nama = "Luspi"
print (nama[2:5]) #cetak spi
print (nama[:5]) #cetak Luspi
print (nama[2:]) #cetak spi
print (nama[-5:-2]) #cetak Luspi
"""
-----------------------------------------------------------------------------------------------------
"""

#Modify Strings
#Upper Case
nama = 'lUsPi GaNtEnG '
print (nama.upper()) #mengkapitalkan semua huruf yang ada di variabel "nama"
print (nama.lower()) #menghufurkecilkan semua huruf yang ada di variabel "nama"
print (nama.strip()) #menghapuskan semua space yang ada di depan maupun belakang (ujung)
print (nama.replace("U", "O")) #mengganti huruf (replace)
print (nama.split(" ")) #memisahkan bagian yang terletak diantara " "
"""
----------------------------------------------------------------------------------------------------
"""

#Menghubungkan Strings
umur = '18'
print ("haloo umurku " + umur + " tahun") #menggunakan tanda tambah
print (f"haloo umurku {umur} tahun") #menggunakan format
"""
---------------------------------------------------------------------------------------------------
"""

#Escape Charcter
"""
kasih (\) sebelumnya
'	      Single Quote
\	      Backslash
n	      New Line
r	      Carriage Return
t	      Tab
b	      Backspace
f	      Form Feed
ooo	   Octal value
xhh	   Hex value
"""
"""
--------------------------------------------------------------------------------------------------
"""
#String Method
"""
capitalize()	   Converts the first character to upper case
casefold()	      Converts string into lower case
center()    	   Returns a centered string
count()     	   Returns the number of times a specified value occurs in a string
encode()	         Returns an encoded version of the string
endswith()	      Returns true if the string ends with the specified value
expandtabs()	   Sets the tab size of the string
find()	         Searches the string for a specified value and returns the position of where it was found
format()	         Formats specified values in a string
format_map()	   Formats specified values in a string
index()	         Searches the string for a specified value and returns the position of where it was found
isalnum()	      Returns True if all characters in the string are alphanumeric
isalpha()	      Returns True if all characters in the string are in the alphabet
isascii()	      Returns True if all characters in the string are ascii characters
isdecimal()	      Returns True if all characters in the string are decimals
isdigit()	      Returns True if all characters in the string are digits
isidentifier()	   Returns True if the string is an identifier
islower()	      Returns True if all characters in the string are lower case
isnumeric()	      Returns True if all characters in the string are numeric
isprintable()	   Returns True if all characters in the string are printable
isspace()	      Returns True if all characters in the string are whitespaces
istitle()	      Returns True if the string follows the rules of a title
isupper()	      Returns True if all characters in the string are upper case
join()	         Joins the elements of an iterable to the end of the string
ljust()	         Returns a left justified version of the string
lower()	         Converts a string into lower case
lstrip()	         Returns a left trim version of the string
maketrans()	      Returns a translation table to be used in translations
partition()	      Returns a tuple where the string is parted into three parts
replace()	      Returns a string where a specified value is replaced with a specified value
rfind()	         Searches the string for a specified value and returns the last position of where it was found
rindex()	         Searches the string for a specified value and returns the last position of where it was found
rjust()	         Returns a right justified version of the string
rpartition()	   Returns a tuple where the string is parted into three parts
rsplit()	         Splits the string at the specified separator, and returns a list
rstrip()	         Returns a right trim version of the string
split()	         Splits the string at the specified separator, and returns a list
splitlines()	   Splits the string at line breaks and returns a list
startswith()	   Returns true if the string starts with the specified value
strip()	         Returns a trimmed version of the string
swapcase()	      Swaps cases, lower case becomes upper case and vice versa
title()	         Converts the first character of each word to upper case
translate()	      Returns a translated string
upper()	         Converts a string into upper case
zfill()	         Fills the string with a specified number of 0 values at the beginning
"""
"""
-----------------------------------------------------------------------------------------------
"""