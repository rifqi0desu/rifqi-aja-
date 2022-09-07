list_integer = [1, 2, 3,10,100 ,250]
list_string = ["ambatukam", "farhan kebab", "reza kecap", "fu'ad racing mandalika"]
list_mix = [20, "hooh tenan", True, "niger"]

print("data string sebelum diubah:", list_string)
print("data mix sebelum diubah", list_mix)
list_string[1] = "aku juga mau"
list_string[2] = "avin sedih"
list_mix[0] = 30
list_mix[1] = "bunda rahma"
list_mix[2] = False
list_mix[3] = "orang kulit putih"
print("data string setelah diubah", list_string)
print("data mix setelah diubah", list_mix)

# Perulangan For

for i in list_integer:
    print(i)

print("\n")
for s in list_string:
    print(s)

print("\n")
for m in list_mix:
    print(m)
