# #mendefinisikan class
# class Persegi_Panjang_184220031:
#       # atibut statis
#       counter = 0
      
#       def __init__(self, p, l): #object 
#             # menaikan nilai atibur statis
#             Persegi_Panjang_184220031.counter += 1
#             # atribut - atribut nnon statis
#             self.panjang = p 
#             self.lebar = l
      
#       def ubah_Panjang(self,p):
#             self.panjang = p 
      
#       def ubah_Lebar(self, l):
#             self.lebar = 1
      
#       def hitung_Luas(self):
#             return self.panjang * self.lebar
      
#       def hitung_Keliling(self):
#             return 2 * (self.panjang + self.lebar)
      
#       def cetak_Luas(self):
#             print('Luas persegi panjang = %.2f' % self.hitung_Luas())
      
#       def cetak_Keliling(self):
#             print('Keliling persegi panjang = % .2f' % self.hitung_Keliling())
      
#       # Membuat tiga object dari kelas PersegiPanjang
#       obj_1 = Persegi_Panjang_184220031(10,5)
#       obj_2 = Persegi_Panjang_184220031(8,6)
#       obj_3 = Persegi_Panjang_184220031(3,5)
     
#      #memanggil atribut counter melalui class
#     print(Persegi_Panjang_184220031.counter)
    
#     # output 3
#     print(obj_1.counter)
   
#    #output 3
#    print(obj_2.counter)
   
#    #output 3
#    print(obj_3.counter)      
   
#    obj_4 = Persegi_Panjang_184220031(212,129)
#    print(Persegi_Panjang_184220031.counter)
   
#    #output 4
#    print(obj_1.counter, obj_2.counter, obj_3.counter, obj_4.counter)
   

# class Aritmatika_184220031 : 
#     @staticmethod
#     def tambah(a, b):
#      return a + b
    
#     @staticmethod
#     def kurang(a, b):
#      return a - b
    
#     @staticmethod
#     def kali(a, b):
#      return a*b
    
#     @staticmethod
#     def bagi(a, b):
#      return a / b
    
#     @staticmethod
#     def bagi_Integer (a, b):
#      return a // b
    
#     @staticmethod
#     def sisa_bagi(a, b):
#      return a % b
    
#     @staticmethod
#     def pangkat(a, b):
#      return a**b
# print(Aritmatika_184220031.tambah(15,5))
# #output 20

# print(Aritmatika_184220031.kurang(25,5))
# #output 20

# print(Aritmatika_184220031.kali(13,27))
# #output 351

# print(Aritmatika_184220031.bagi_Integer(10,5))
# #output 2

# print(Aritmatika_184220031.sisa_bagi(10, 5))
# #output 0

# print(Aritmatika_184220031.pangkat(8,6))
# #output 262144

# #membuat objek dari kelas Aritmatika
# object = Aritmatika_184220031()
# print(object.tambah(2210,35))
# #output 2245
# print(object.sisa_bagi(2210,35))
# #Output 5

#Membuat Pewarisan turunan dari class List
class String_List_184220031 (list):
    def ___init___(self):
        self.data = []
    
    def __repr__(self):
        return str(self.data)
    
    #override metode append()
    def append(self, object):
        if not isintance(object, str):
            raise TypeError('Objek harus bertipe string')
        self.data.append(object)
    
    # override metode insert()
    def insert(self, indeks, object):
        if indeks >= len(self.data) or \
            indeks < -len(Self.data):
                raise IndexError('Indeks di luar rentang')
        if not isintace(object, str):
            # override metode append()
            raise TypeError('Object harus bertipe string')
        self.data.insert(indeks, object)