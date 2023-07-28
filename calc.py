angka1 = int(input("masukan angka pertama : "))

angka2 = int(input("masukan angka kedua : "))

operator = input("masukan operator +,*,/,- : ")

# hasil = angka1 operator angka2
# print(hasil)

if operator == "+":
    
    hasil = angka1+angka2

elif operator == "-":

    hasil = angka1-angka2

elif operator == "*":

    hasil = angka1*angka2

elif operator == "/":

    hasil = angka1/angka2

else:

    print("operator tak diketahui")


print("hasil :",hasil)
