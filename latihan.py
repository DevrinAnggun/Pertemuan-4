# menentukan wujud air yang berada pada suhu tertentu
suhu = int(input("Masukan besarnya suhu: "))

if(suhu <= 0):
    print("Pada suhu ", suhu ," derajat celcius, air akan berwujud es")
elif(suhu > 0 & suhu < 100):
    print("Pada suhu ", suhu ," derajat celcius, air akan berwujud air")
# else:
    print("Pada suhu ", suhu ," derajat celcius, air akan berwujud gas")


 # menentukan panggilan seseorang dengan kondisi
gender = input("Perempuan atau laki-laki ? (L/P): ")
if(gender == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
if(status == 'Y'):
    print("Hallo Bapak!")
elif(status == 'N'):
    print("Hallo Mas!")
else:
    print("Tidak ada dalam pilihan") 
gender = str(input("Perempuan atau laki-laki"))
status = input("Anda sudah menikah atau belum? (Y/N): ")
if(status == 'Y'):
    print("Hallo Ibu!")
elif(status == 'N'):
    print("Hallo Mba!")
else:
   print("Tidak ada dalam pilihan")


   # mengisi data nama, jenis kelamin, status, dan agama.
print("===========INPUT==========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))

#1=Islam, 2=Protestan, 3=Katolik, 4=Hindu, 5=Budha
if(agama==1):
   agama = "Islam"
elif(agama==2):
   agama = "Protestan"
elif(agama==3):
   agama = "Katolik"
elif(agama==4):
   agama = "Hindu"
elif(agama==5):
   agama = "Budha"
else:
   agama = "Agama tidak ditemukan"

print("==========OUTPUT========")
print("Nama: ",nama)
print("Jenis Kelamin: ",jk)
print("Agama: ",agama)