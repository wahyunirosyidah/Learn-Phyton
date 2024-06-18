
## ngecek komponen

#startswith() 
cek_start="Sajangnim Oppa".startswith("Sajangnim")
print("start = "+str(cek_start))

#endswith()
cek_end="Sajangnim Oppa".endswith("Oppa")
print("end = "+str(cek_end))

##penggabungan komponen 

#join() -> menggabungkan
pisah=['aku','sayang','kamu']
gabung=' ehm '.join(pisah)
print(pisah)
print(gabung)

#spilt() -> memisahkan
gabungan="akuehmsayangehmkamu"
print(gabungan.split("ehm"))

#alokasi karakter
#rjust() -> right justify = rata kanan
kanan="wahyuni".rjust(10) #mengambil 10 karakter termasuk wahyuni (7 char) + 3 char kosong
print("'"+kanan+"'")

kanan="kanan".rjust(10) #mengambil 10 karakter termasuk kanan (5 char) + 5 char kosong
print("'"+kanan+"'")

#ljust() -> left justify 
kiri="wahyuni".ljust(10) #mengambil 10 karakter termasuk wahyuni (7 char) + 3 char kosong
print("'"+kiri+"'")

kiri="kiri".ljust(10) #mengambil 10 karakter termasuk kiri (4 char) + 6 char kosong
print("'"+kiri+"'")

#center()
tengah="wahyuni".center(11,"-") #mengambil 10 karakter termasuk wahyuni (7 char) + 3 char kosong
print("'"+tengah+"'")

tengah="tengah".center(10,"-") #mengambil 10 karakter termasuk kiri (4 char) + 6 char kosong
print("'"+tengah+"'")

#kebalikan/menghilangkan tanda -> strip
tengah2=tengah.strip("-") #menghilangkan tanda "-"
print("'"+tengah2+"'")

kiri="kiri".ljust(10) #mengambil 10 karakter termasuk kiri (4 char) + 6 char kosong
print("'"+kiri+"'")
kiri=kiri.strip()
print("'"+kiri+"'")
