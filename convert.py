kalimat = input("masukkan sebuah kata : ")

operator = int(input("pilih operator : 1.lowercase, 2.uppercase (masukkan nomor operator, misal 1) : "))

if operator == 1 :
    print(kalimat.lower())
elif operator == 2 :
    print(kalimat.upper())
else:
    print("operator tak diketahui")



