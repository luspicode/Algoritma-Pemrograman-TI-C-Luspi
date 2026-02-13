#If Statement

#Banyak statement dalam if
nilai = 85
if nilai >= 75:
    print("Lulus")          # Pernyataan pertama
    print("Nilai mantapp")    # Pernyataan kedua
    print("Selamattt")       # Pernyataan ketiga
"""
-------------------------------------------------------------------
"""
#Elif
nilai = 70
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")
elif nilai <60:
    print("Nilai E")
"""
-------------------------------------------------------------------
"""
#Gabungkan if, elif, dan else
nilai = 20
if nilai >= 90:
    print("Nilai A")
elif nilai >= 80:
    print("Nilai B")
elif nilai >= 70:
    print("Nilai C")
elif nilai >= 60:
    print("Nilai D")
else:
    print("Nilai E")
"""
-------------------------------------------------------------------
"""
#Nested if
umur = 20
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Boleh nyetir")      # if di dalam if
    else:
        print("Umur cukup, tapi belum punya SIM")
else:
    print("Belum cukup umur")
    """
-------------------------------------------------------------------
"""