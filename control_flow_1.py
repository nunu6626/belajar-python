# 1. Uang yang dibawa adalah 5000, jika harga wortel 1000, beli sesuai dengan uang yang dimiliki.
#    tampilkan berapa wortel yang dapat dibeli
# 2. Uang yang dibawa adalah 5000, jika harga wortel diatas 1000, print "wortel mahal"


uang = 5000
harga = 1000
if harga > 1000:
    print( "wortel mahal")
else:
    print("yang dapat di beli sebanyak",round(uang / harga))

