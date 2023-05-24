import re

def check_password(password):
    length = len(password)

    if length < 8 or length > 32:
        return "Kata sandi harus memiliki panjang antara 8 hingga 32 karakter."

    if password[0].isdigit():
        return "Karakter awal tidak boleh angka."

    if not any(ini.isdigit() for ini in password):
        return "Kata sandi harus memiliki minimal satu angka."

    if not any(ini.islower() for ini in password) or not any(ini.isupper() for ini in password):
        return "Kata sandi harus memiliki huruf kapital dan huruf kecil."

    return "Kata sandi valid."


input1 = "5andiwara"
output1 = check_password(input1)
print(output1)

input2 = "sandiwar4"
output2 = check_password(input2)
print(output2)

input3 = "Sandiwar4"
output3 = check_password(input3)
print(output3)
