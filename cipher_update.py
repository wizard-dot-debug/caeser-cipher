def encrypt_decrypt(a,b,c):
    x = 'abcdefghijklmnopqrstuvwxyz'
    cipher_plain = ' '
    
    for i in a:
        if i != ' ':
            index = x.find(i)
            if index == -1:
                cipher_plain += i
            else:
                new_index = index+(b*c)
                if new_index >=26:
                    new_index = new_index % len(x)
                    cipher_plain += x[new_index]
                else:
                    cipher_plain += x[new_index]
        else:
            cipher_plain += i
    return cipher_plain 

print()   
print('Welcome To Caesar Cipher Program')    
print()  

a = 'You want to encrypt or decrypt?'    
print(a.title()) 
print()  
b = str(input('Encrypt/Decrypt:\n')).lower()  
  
if b == 'encrypt':
    print('Encryptiopn mode is activated')
    print()
    k = input('Give your Text: ').lower()
    y = int(input('Shift number: '))
    d = 1
    print(f'Your Encryption is finished.\nHere is your message: {encrypt_decrypt(k,y,d)}')
else:
    print('Decryptiopn mode is activated')
    print()
    k = input('Give your Text: ').lower()
    y = int(input('Shift number: '))
    d = -1
    print(f'Your Decryption is finished.\nHere is your message: {encrypt_decrypt(k,y,d)}')

