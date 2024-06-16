# OPERASI LOGIKA NOT,OR,XOR


inputUser = float(input("Masukkan Angka: "))
# # Memeriksa Angka kurang dari 3
# isKurangDari = (inputUser<3)
# print("Kurang dari 3 : ",isKurangDari)

# # Memeriksa Angka lebih dari 10
# isLebihDari=(inputUser>10)
# print("Lebih dari 10 : ",isLebihDari)

# isAtau=isKurangDari or isLebihDari
# print("Atau : ",isAtau)


# -------3+++++++10-------
# Memeriksa Angka Lebih Dari 3
# isLebihDari3=(inputUser>3)
# print("Lebih dari 3 : ",isLebihDari3)
# # Memeriksa Angka kurang dari 10
# isKurangDari10=(inputUser<10)
# print("Kurang Dari 10 : ",isKurangDari10)
# # AND
# isAnd= isLebihDari3 and isKurangDari10
# print("And : ",isAnd)

# SOAL NOMOR 1

bagian1= inputUser>0 and inputUser<5
print("Bagian 1 : ", bagian1)
bagian2= inputUser>8 and inputUser<11
print("Bagian 2 : ", bagian2)
nomor1=bagian1 or bagian2
# print("Nomor 1: ", nomor1)
print("Nomor 1: ", bagian1 or bagian2)

# SOAL NOMOR 2

bagian12=inputUser<0
bagian22=inputUser>5 and inputUser<8
bagian32=inputUser>11
nomor2=bagian12 or bagian22 or bagian32
print("Nomor 2: ", nomor2)