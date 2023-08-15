#Looping array
student_marks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in student_marks:
    i=4
    if (i % 2 == 0):
        if (i % 4 == 0):
            print(i, "merupakan bilangan genap dan habis di bagi 4")
        else:
            print(i, "merupakan bilangan genap")   
    else:
        print(i, "merupakan bilangan ganjil")
   

    