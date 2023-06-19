nilai = int(input("Masukkan bilangan bulat: "))
if (nilai > 0):
       print("Bilangan", nilai, " merupakan bilangan positif")
elif (nilai < 0):
       print("Bilangan", nilai, " merupakan bilangan negatif")
else:
       print("Bilangan nol")

       
       hh = int(input("Jam : "))
mm = int(input("Menit : "))
ss = int(input("Detik : "))
totalDetik = (hh*360) + (mm*60) + (ss*1)
print(mm,' Jam + ',mm,' Menit + ',ss,' Detik adalah :')
print(totalDetik,' Detik')


huruf = str(input("Masukkan huruf: "))
if(huruf == 'a','i','u','e','o'):
    print("Huruf", huruf, "Adalah huruf vokal")
else:
    print("Huruf", huruf, "Bukanlah huruf vokal")


bilangan = int(input("Masukkan bilangan yang akan dibagi : "))
pembagi = int(input("Masukkan bilangan pembagi : "))

if(pembagi == 0):
    print("Pembagi tidak boleh 0", )
else:
    print(bilangan / pembagi)


# Tahun Kabisat
tahun = int(input("Masukkan Tahun Kabisat: "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print ("Tahun Kabisat")
        else:
            print ("Bukan Tahun Kabisat")
    else:
        print ("Tahun Kabisat")
else:
    print ("Bukan Tahun Kabisat")