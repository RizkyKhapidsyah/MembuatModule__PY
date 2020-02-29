import FungsiAritmatika                     #Cara 1 - Mengimport Module
import Judul as BannerSaya                  #Cara 2 - Mengimport Module
from FungsiAritmatika2 import Bagi          #Cara 3 - Mengimport Module (Lebih Spesifik Fungsi Yang Akan Digunakan)
from FungsiAritmatika2 import Kali          #Cara 3 - Mengimport Module (Lebih Spesifik Fungsi Yang Akan Digunakan)
#from FungsiAritmatika2 import Kali, Bagi   #Cara 4 - Mengimport Module (Lebih Spesifik Fungsi Yang Akan Digunakan)
#from FungsiAritmatika2 import *            #Cara 5 - Mengimport Module (Lebih Spesifik Fungsi Yang Akan Digunakan)
from FungsiAritmatika2 import Kali as K     #Cara 5 - Mengimport Module (Lebih Spesifik Fungsi Yang Akan Digunakan)

BannerSaya.Judul1()
FungsiAritmatika.Tambah(7, 2)
FungsiAritmatika.Kurang(9, 4)

BannerSaya.Judul2()
Bagi(8, 2)
Kali(6, 8)
K(7, 2)
