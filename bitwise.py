a=9
b=5

# bitwise OR (|)
c=a|b
print("==========OR==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("nilai : ",b,", binary : ", format(b,"08b"))
print("-----------------------------------------(|)")
print("nilai : ",c,", binary : ", format(c,"08b"))

# bitwise AND (&)
c=a&b
print("==========AND==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("nilai : ",b,", binary : ", format(b,"08b"))
print("-----------------------------------------(&)")
print("nilai : ",c,", binary : ", format(c,"08b"))

# bitwise XOR (^)
c=a^b
print("==========XOR==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("nilai : ",b,", binary : ", format(b,"08b"))
print("-----------------------------------------(^)")
print("nilai : ",c,", binary : ", format(c,"08b"))

# bitwise NOT (~)
c=~a
print("==========NOT==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("-----------------------------------------(~)")
print("nilai : ",c,", binary : ", format(c,"08b"))

print("MENGUBAH 0 JADI 1 DAN SEBALIKNYA")
# kalau mau diubah 0 jadi 1 dan sebaliknya, pakai XOR
# d = 9
d=0b00001001
e=0b11111111
print("nilai : ",e^d,", binary : ", format(e^d,"08b"))

# SHIFTING (MENGGESER)

# shift right (>>)
c=a>>2
print("==========(>>)==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("-----------------------------------------(~)")
print("nilai : ",c,", binary : ", format(c,"08b"))

# shift left (<<)
c=a<<2
print("==========(<<)==========")
print("nilai : ",a,", binary : ", format(a,"08b"))
print("-----------------------------------------(~)")
print("nilai : ",c,", binary : ", format(c,"08b"))