'''problem statement:Write a program that can encrypt  and decrypt using the Additive Cipher.'''
'''author:bhavna nagar'''

'''function to encrypt text using key'''
def additive_encryption(text,key):
    encrypted=""
    #looping through text to get cipher text E(X)=(x+KEY)%26
    for i  in range(len(text)):
        char=text[i]
        if(char.isupper()):
            encrypted+=chr(((ord(char)-65)+key)%26 + 65)
        elif(char.islower()):
            encrypted+=chr(((ord(char)-97)+key)%26 + 97)
        else:
            encrypted+=char
    return encrypted
'''function to decrypt ciper using key'''
def additive_decryption(encrypted,key):
    decrypted=""
    #looping through text to get plain text D(X)=(x-KEY)%26
    for i in  range(len(encrypted)):
        char=encrypted[i]
        if(char.isupper()):
            decrypted+=chr(((ord(char)-65)-key)%26+65)
        elif(char.islower()):
            decrypted+=chr(((ord(char)-97)-key)%26+97)
        else:
            decrypted+=char
    return decrypted

def main():
    text=input("enter text: ")
    key=int(input("enter key for encryption: "))
    encrypted=additive_encryption(text,key)
    decrypted=additive_decryption(encrypted,key)
    print("****encrypted text is*****")
    print(encrypted)
    print("****decrypted text is*****")
    print(decrypted)


main()
    
            
            
