#1. Menyambung string (concatenate)
nama_pertama="Wahyuni"
nama_tengah="D"
nama_akhir="Rosyidah"
nama_lengkap=nama_pertama+" "+nama_tengah+"'"+nama_akhir
print(nama_lengkap)

#2. Menghitung panjang string
panjang=len(nama_lengkap)
print("panjang dari "+nama_lengkap+" : "+str(panjang))

#3. Operator String

#mengecek apakah ada komponen char atau strinh di string

d="d"
status=d in nama_lengkap
print("string "+d+" ada di "+nama_lengkap+": "+str(status))

D="D"
status=d not in nama_lengkap
print("string "+D+" tidak ada di "+nama_lengkap+": "+str(status))

#mengulang string
print("wk"*10)
print(5*"wk")

#indexing
print("index ke-0 : "+nama_lengkap[0])
print("index ke-(-1) : "+nama_lengkap[-1])
#mengambil nilai index ke 0 sampai 2, 3 tidak diambil
print("index ke-[0:3] : "+nama_lengkap[0:3])
#mengambil nilai index ke 0,2,3,4,8 (loncat 2)
print("index ke-[0,2,4,6,8,10] : "+nama_lengkap[0:11:2])
#[0:10:2] -> ambil nilai index 0-10 loncat 2

#item paling kecil, spasi paling kecil sebelum a
print("paling kecil : "+min(nama_lengkap))
#item paling besar, huruf paling terakhir di alfabet
print("paling besar : "+max(nama_lengkap))

#iitem besar kecil diambil sesuai dengan ASCII code
#cek ASCII code
ascii_code=ord(" ")
print("ASCII code dari spasi : "+str(ascii_code))
data=117
print("char untuk ASCII code "+str(data)+" : "+chr(data))

#4. operator dalam bentuk method


data="Wahyuni Fajrin Rosyidah"
jumlah = data.count("o")
print("jumlah o pada "+data+" : "+str(jumlah))


















