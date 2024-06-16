data = "ini adalah string"
print(data)
print(type(data))

#1. Cara membuat string

'''
    1. dengan menggunakan single quote
'''

data='Menggunakan Single Quote'
print(data)
print('"Halo, apa kabar?"')
data="Menggunakan Double Quote"
print(data)
print("'Halo, apa kabar?'")

#agar bisa memasukkan tanda kutip ' di dalam
#cara 1
print("ini adalah hari jum'at")
#cara 2 
print('ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

#agar bisa memasukkan backslash (\) di dalam
print("C:\\user\\Ayu")

#tab
print("ayu \twahyuni, tab")

#backspace
print("ayu \bwahyuni, backspace")

#newline
#LF -> Line Feed, u/ unix, MacOS, linux
print("baris pertama, \nbaris kedua")
#CR -> carriage return, u/ commodore,acorn
print("baris pertama, \rbaris kedua")
#CRLF -> Line Feed carriage return. u/ windows
print("baris pertama, \r\nbaris kedua")

#3. String Literal atau raw

#hati-hati
#print('C:\new\Ayu') -> kalau kayak gini kan harus manual \\
#cara agar otomatis
print(r'C:\new\Ayu')

#Multiline String
print(""""
      Nama :  Wahyuni
      Kelas : 3 SD
      
      """)

#menggabungkan 
#multiline literal string dan RAW
print(r""""
      Nama :  Wahyuni
      Kelas : 3 SD
      website : C:\new\Ayu
      """)