# print("PROGRAM KONVERSI TEMPERATURE/n")

# celcius=float(input("Masukkan suhu dalam celcius: "))
# print("suhu adalah ",celcius," Celcius")

# # Celcius -> Reamur
# reamur=(4/5)*celcius
# print("suhu adalah ",reamur," Reamur")

# # Celcius -> Fahrenheit
# fahrenheit=((9/5)*celcius) + 32
# print("suhu adalah ",fahrenheit," Fahrenheit")

# # Celcius -> Kelvin
# kelvin = celcius+273
# print("suhu adalah ",kelvin," Kelvin \n")

print("FAHRENHEIT -> KELVIN\n")
fahrenheit=float(input("Masukkan suhu dalam fahrenheit: "))
fkelvin= ((5/9)*(fahrenheit-32))+273
print("suhu adalah ",fkelvin," Kelvin \n")

print("KELVIN -> FAHRENHEIT\n")
kelvin=float(input("Masukkan suhu dalam kelvin: "))
jeje=kelvin-273
kfahrenheit= (9/5*jeje)+32
print("suhu adalah ",kfahrenheit," Fahrenheit \n")