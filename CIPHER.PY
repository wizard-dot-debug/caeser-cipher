def encrypt(a,b):
    x = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ' '
    
    for i in a:
        if i != ' ':
            index = x.find(i)
            if index == -1:
                cipher += i
            else:
                new_index = index+b
                if new_index >=26:
                    new_index = new_index % len(x)
                    cipher += x[new_index]
                else:
                    cipher += x[new_index]
        else:
            cipher += i
    return cipher 

def decrypt(a,b):
    x = 'abcdefghijklmnopqrstuvwxyz'
    plain = ' '
    for j in a:
        if j != ' ':
            index = x.find(j)
            if index == -1:
                plain += j
            else:
                new_index = index - b
                if new_index < 0:
                    new_index += (len(x)-(index+b))
                    plain += x[new_index]
                else:
                    plain += x[new_index]
        else:
            plain += j
    return plain
                    
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
    k = input('Give your PLAIN Text to encrypt: ').lower()
    y = int(input('Shift number: '))
    print(f'Your Encryption is finished.\nHere is your message: {encrypt(k,y)}')
else:
    print('Decryptiopn mode is activated')
    print()
    x = input('Give your CIPHER Text to decrypt: ').lower()
    y = int(input('Shift number: '))
    print(f'Your Decryption is finished.\nHere is your message: {decrypt(x,y)}')
 
# this program is called Caesar Cipher Program.
# This is the most bacis method for message encrypting and decrypting.
# Here each letter of the message is replaceed by the new index latter. 
# The new index is found by the summation of current latter index and the shift number.watch line 11
# This is how the encrypting algorithm works.
#For decrypting a message the new index will be the result of substracting the shift number from the index of the latter.watch line 28
#the encrypted text is called cypher text and the decrypted text is called plain text
