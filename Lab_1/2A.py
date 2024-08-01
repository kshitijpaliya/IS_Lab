text = "the house is being sold tonight"
key ="dollars"
encrypt =[]
decrypt =[]
encrpyt_char=""
decrypt_char=""


for i in range(0,len(text)):
    j=0
    if(text[i]==" "):
        encrpyt_char+=" "
        continue
    p=ord(text[i])-97
    
    k=ord(key[j%len(key)])-97
    j+=1
    x=(p+k)%26
    encrypt.append(x)
    encrpyt_char+=(chr(x+97))
    
print(encrypt)
print("Encrpyted Text :" + encrpyt_char)

