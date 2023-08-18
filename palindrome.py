# program untuk memeriksa apakah variable merupakan palindrome atau bukan
x = ['katak','bubur','malam']
for kata in x:
    print(kata)
    if kata == kata[::-1]:
        print("ini palindrum ")
    else :
        print("ini bukan palindrum")

# program untuk menghitung ada berapa palindrome dalam sebuah array.
total_palindrum = 0
    
x = ['malam', 'katak', 'bubur', 'civic', 'mobil', 'rotor']
for kata in x:
    print(kata)
    if kata == kata[::-1]:
        print("ini palindrum ")
        total_palindrum += 1
    else :
        print("ini bukan palindrum")

print(total_palindrum)




