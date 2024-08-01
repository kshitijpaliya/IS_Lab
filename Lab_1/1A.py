# Input
text = "I am learning information security"
text = text.lower()

encrypt=[]
decrypt=[]
encrypt_char=""
decrypt_char=""

# for i in text:
#     if (i==" "):
#         continue
#     asc=ord(i)
#     c=asc-97
#     x=(c+20)%26
#     encrypt.append(x)
    
# print(encrypt)

# for i in encrypt:
#     i+=97
#     ch=chr(i)
#     encrypt_char+=ch
    
# print("Encrpyted Text :" + encrypt_char)

# print(encrypt)
# print(encrypt_char)


# for i in encrypt:
#     x=(i-20)%26
#     decrypt.append(x)
    
# print(decrypt)

# for i in decrypt:
#     i+=97
#     ch=chr(i)
#     decrypt_char+=ch
    
# print("Decrpyted Text :" + decrypt_char)

for i in text:
    if(i==" "):
        encrypt_char+=" "
        continue
    x=((ord(i)-97)+20)%26
    encrypt.append(x)
    encrypt_char+=(chr(x+97))
    
print(encrypt)
print("Encrpyted Text :" + encrypt_char)

for i in encrypt_char:
    if(i==" "):
        decrypt_char+=" "
        continue
    x=((ord(i)-97)-20)%26
    decrypt.append(x)
    decrypt_char+=(chr(x+97))
    
print(decrypt)
print("Decrpyted Text :" + decrypt_char)