
# # mencari nilai max dan min
a = [1, 10, 9, 8]

print(a)
print('Nilai terbesar:', max(a))
print('Nilai terkecil:', min(a))


# # menggabungkan 2 list
def append_lists():
    x = [1,2,3]
    y = [4,5,6]
    
    for i in y:
        x.append(i)
    print(x)

append_lists()



# Menghitung rata rata dari deretan angka
n = int(input("\nBanyaknya Data: "))

print() 
data = []
jum = 0

for i in range(0, n):
    temp = int(input("Masukkan data ke-%d: " % (i+1)))
    data.append(temp)
    jum += data[i]
    rata2 = round(jum / n)
print(data)
print(jum)
print(rata2)
print(f"rata-rata = {rata2} " )
# print("\nRata-rata  = "  rata2)

