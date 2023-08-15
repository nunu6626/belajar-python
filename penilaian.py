# Buat program untuk memberikan penilaian siswa:
# Buat dua buah variable, nilai_ujian dan kehadiran.
# Variable nilai_ujian berisi nilai ujian siswa, dan kehadiran berisi nilai kehadiran siswa.

# Jika kehadiran dibawah 75, maka print "Grade: E (Tidak Lulus karena Kehadiran Rendah)"
# Jika kehadiran diatas 75 dan:
# 2.1. Jika nilai ujian diatas atau sama dengan 90, print "Grade: A"
# 2.2. Jika nilai ujian diatas atau sama dengan 80, print "Grade: B"
# 2.3. Jika nilai ujian diatas atau sama dengan 70, print "Grade: C"
# 2.4. Jika nilai ujian diatas atau sama dengan 60, print "Grade: D"
# 2.5. Jika nilai ujian dibawah 60, print "Grade: E (Tidak Lulus)"

nilai_kehadiran = 75
nilai_ujian = 75
if nilai_kehadiran < 75 : 
    print("tidak lulus karena kehadiran rendah")
else :
    print("lulus pengecekan kehadiran")
    if nilai_ujian >= 90 :
        print(f"nilai {nilai_ujian} = grade A")
    elif nilai_ujian >= 80 :
        print(f"nilai {nilai_ujian} = grade B")
    elif nilai_ujian >= 70 :
        print(f"nilai {nilai_ujian} = grade C")
    elif nilai_ujian >= 60 :
        print(f"nilai {nilai_ujian} = grade D")
    else:
        print(f"nilai {nilai_ujian} = grade E") 
