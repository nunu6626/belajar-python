# dik
number = 50

# dit
f = 0
c = 0

# peny
f=(number*9/5)+32
c = 5 * (number- 32)/ 9

print("hasil celcius ke fahrenheit:", f)
print("hasil fahrenheit ke celcius:", c)

loop = []
for x in range(10):
  loop.append(x +1)
 
print(loop)

loop2 = []
for x in range(100):
  loop2.append(str(x+1))

separator = ', '
my_string = separator.join(loop2)
print(my_string)