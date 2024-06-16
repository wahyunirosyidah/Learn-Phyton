print("Hello2")
def tampil():
    print("Data =", data_int, "Type: " , type(data_int))
# Casting
data_int = 9
tampil()

# Ubah dari int ke float
data_float=float(data_int)
print("Data =", data_int, "Type: " , type(data_float))

# Ubah dari int ke string
data_string=str(data_int)
print("Data =", data_int, "Type: " , type(data_string),"")

# Ubah dari int ke boolean
data_bool=bool(data_int)
print("Data =", data_int, "Type: " , type(data_bool),"\n")

print("====FLOAT====")
data_float=1
print("Data =", data_float, "Type: " , type(data_float))
data_int = int(data_float)
print("Data =", data_int, "Type: " , type(data_int))
data_string=str(data_float)
print("Data =", data_string, "Type: " , type(data_string))
data_bool=bool(data_float)
print("Data =", data_bool, "Type: " , type(data_bool),"\n")


