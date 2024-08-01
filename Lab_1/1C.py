text = "I am learning information security"
text = text.lower()

encrypt=[]
decrypt=[]
encrypt_char=""
decrypt_char=""
k1=15
k2=20

for i in text:
    if(i==" "):
        encrypt_char+=" "
        continue
    x=(((ord(i)-97)*k1)+k2)%26
    encrypt.append(x)
    encrypt_char+=(chr(x+97))
    
print(encrypt)
print("Encrpyted Text :" + encrypt_char)

for i in encrypt_char:
    if(i==" "):
        decrypt_char+=" "
        continue
    x=(((ord(i)-97)-k2)*pow(k1,-1,26))%26
    decrypt.append(x)
    decrypt_char+=(chr(x+97))
    
print(decrypt) 
print("Decrpyted Text :" + decrypt_char)