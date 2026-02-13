class Vehicle:
  def __init__ (self, jenis, merk, tahun_rilis):
    self.jenis = jenis
    self.merk = merk
    self.tahun_rilis = tahun_rilis
    
  def Sound (self, jenis):
    return f"Suara {jenis}"
  

class Mobil (Vehicle):
  def __init__ (self, jenis, merk, tahun_rilis, asal):
    super().__init__(jenis, merk, tahun_rilis)
    self.__asal = asal
    
  def get_asal_mobil(self):
    return self.__asal
    
class Motor (Vehicle):
  def __init__ (self, jenis, merk, tahun_rilis, asal):
    super().__init__(jenis, merk, tahun_rilis)
    self.__asal = asal

  def get_asal_motor(self):
    return self.__asal
  
  
kendaraan = Vehicle("Sport", "Honda", "2010")
motor = Motor("Sport", "Honda", "2010", "Amerika")
mobil = Mobil("Sport", "Honda", "2010", "Eropa")

print (motor.get_asal_motor())
print (mobil.get_asal_mobil())

