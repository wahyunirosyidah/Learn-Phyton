#FORMAT STRING 

#string
nama="wahyuni"
format_str=f"hello {nama}"
print(format_str)

#boolean
boolean=False
format_str=f"boolean = {boolean}"
print(format_str)

#angka
angka=2005.6
format_str=f"angka={angka}"
print(format_str)

#bilangan bulat
bilbul=20
format_str=f"bilangan bulat={bilbul}"
print(format_str)

#bilangn dengan ordo ribuan
bilbulr=20000000000
format_str=f"jutaan ={bilbulr:,}" #20,000,000
print(format_str)

#bilangan desimal
bildes=2005.54321
format_str=f"desimal={bildes:.4f}" #4f-> 4 angka di belakang koma
print(format_str)

#menampilkan loading zero
bildes=2005.54321
format_str=f"desimal={bildes:011.4f}" #011 -> mengubah hasil print angka desimal menjadi 11 karakter 
print(format_str)

#menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus=f"minus={angka_minus:+d}"
format_plus=f"plus={angka_plus:2f}"
print(format_minus)
print(format_plus)




