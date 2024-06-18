# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a=5 # adalah assignment
print("nilai a= ", a)

a += 1 #artinya a = a+1
print("nilai a += 1 adalah ", a)

a -= 2 #artinya a = a-2
print("nilai a -= 2 adalah ", a)

a *= 2 #artinya a = a*2
print("nilai a *= 2 adalah ", a)

a /= 2 #artinya a = a/2
print("nilai a /= 2 adalah ", a)

b=10
print("nilai b :	",b)

b %= 3
print("nilai b %= 3 adalah ", b)

#Floor Division
b=10
b //= 3
print("nilai b //= 3 adalah ", b)

a=5
a **= 3
print("nilai a **= 5 adalah ", a)

#Operasi bitwise 

#or
c=True 
print("\nNilai c = ", c)
c |= False
print("Nilai c |= False adalah  ", c)

c = False
print("\nNilai c = ", c)
c |= True
print("Nilai c |= True adalah ", c)


#and
d=True 
print("\nNilai d = ", d)
d &= False
print("Nilai d &= False adalah  ", d)

d = True
print("\nNilai d = ", d)
d |= True
print("Nilai d &= True adalah ", d)

#xor
d=True
print("\nNilai d = ", d)
d ^= False
print("Nilai d ^= False adalah  ", d)

d = True
print("\nNilai d = ", d)
d ^= True
print("Nilai d ^= True adalah ", d)


#not tidak bisa
#d = True
#print("\nNilai d = ", d)
#d ~= True
#print("Nilai d &= True adalah ", d)

#d = False
#print("\nNilai d = ", d)
#d ~= False
#print("Nilai d ~= True adalah ", d)

#SHIFTING
d=0b0100
print("\nNilai d = ", d)
print ("Nilai d dalam bit = ", format(d,"04b"))
d >>= 2
print ("Nilai d >>= 2 ", format(d,"04b"))
d <<= 1
print ("Nilai d <<= 1 ", format(d,"04b"))












