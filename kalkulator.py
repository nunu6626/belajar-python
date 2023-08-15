# Buat program kalkulator sederhana untuk menghitung ongkos pengiriman barang berdasarkan berat dan tujuan pengiriman. Biaya pengiriman dihitung berdasarkan beberapa kriteria:
# Jika berat barang kurang dari atau sama dengan 1 kg, biaya pengiriman adalah 5000 rupiah.
# Jika berat barang lebih dari 1 kg dan kurang dari atau sama dengan 5 kg, biaya pengiriman adalah 10000 rupiah.
# Jika berat barang lebih dari 5 kg dan kurang dari atau sama dengan 10 kg, biaya pengiriman adalah 20000 rupiah.
# Jika berat barang lebih dari 10 kg, biaya pengiriman adalah 30000 rupiah.
# Jika tujuan pengiriman dalam kota (misalnya kode kota "A"), tambahkan 5000 rupiah ke biaya pengiriman.
# Jika tujuan pengiriman antar kota dalam provinsi (misalnya kode kota "B"), tambahkan 10000 rupiah ke biaya pengiriman.
# Jika tujuan pengiriman antar provinsi (misalnya kode kota "C"), tambahkan 20000 rupiah ke biaya pengiriman.





berat_barang = 6
kota_tujuan = "B"
biaya = 0
ongkir = 0
if berat_barang <= 1 : 
    biaya = 5000
elif berat_barang > 1 & berat_barang <= 5:
    biaya = 10000
elif berat_barang > 5 & berat_barang <= 10:
    biaya = 20000
else :
    biaya = 30000

if kota_tujuan == "A":
    ongkir = 5000
elif kota_tujuan == "B":
    ongkir = 1000
else :
    ongkir = 20000

print("harganya:",biaya + ongkir)
    
# else :
#     print("")
#     if berat_barang >= 90 :
#         print(f"nilai {berat_barang} = ")
#     elif berat_barang >= 80 :
#         print(f"nilai {berat_barang} = ")
#     elif berat_barang >= 70 :
#         print(f"nilai {berat_barang} = ")
#     elif berat_barang >= 60 :
#         print(f"nilai {berat_barang} = ")
#     else:
#         print(f"nilai {berat_barang} = ") 


