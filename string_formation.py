#Input Kalimat
kalimat = input("masukan sebuah kata : ")
#Hitung Jumlah Karakter
print("panjang kata %s: adalah %s " % (kalimat, len(kalimat)))

#mengubah huruf kecil jadi besar
kata = "ainun"
kata_besar = kata.upper()
print(kata_besar)

#mengubah huruf besar jadi kecil
kata="AINUN"
print(kata.lower())

#mengganti huruf jadi *

kata = input("masukkan sebuah kalimat : ")
# kalimat =kata.lower()
result = kata.replace("a","*").replace("N","*")
print(result)

                      
