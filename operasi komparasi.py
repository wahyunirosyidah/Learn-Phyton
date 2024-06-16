# literal, a=4, literalnya 4


# Membandingkan nilai literal pakai ==
# a==4

# Membandingkan variabel dan variabel pakai object identity "is"
a = 4
b = 4
print(hex(id(a)))
print(hex(id(b)))
# kalau angkanya sama, idnya sama
# 
hasil = a is b
print(hasil)
 
hasil = a is not b
print(hasil)

