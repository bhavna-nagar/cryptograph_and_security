'''PROBLEM STATEMEMT:Write a program that can encrypt and decrypyt using the Affine Cipher '''
'''AUTHOR:BHAVNA NAGAR'''
'''function to encrypt plain text to cipher text using Key which is array of two keys'''
def affine_encryption(text,key):
    encrypted=""
    #getting letter of cipher text using E(x)=(ax+b)%26
    for i  in range(len(text)):
        char=text[i]
        if(char.isupper()):
            encrypted+=chr(((ord(char)-65)*key[0]+key[1])%26 + 65)
        elif(char.islower()):
            encrypted+=chr(((ord(char)-97)*key[0]+key[1])%26 + 97)
        else:
            encrypted+=char
    return encrypted

#extended euclid theorem
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
#function to find inverse of a correspoinding to m
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
#function to decrypt encrypted text
def affine_decryption(encrypted,key):
    decrypted=""
    key1=modinv(key[0],26)#gettting a inverse
    #getting character of plain text using D(X)=a^(-1)(x-b)mod(26)
    for i in  range(len(encrypted)):
        char=encrypted[i]
        if(char.isupper()):
            decrypted+=chr((key1*(ord(char)-65-key[1]))%26+65)
        elif(char.islower()):
            decrypted+=chr((key1*(ord(char)-97-key[1]))%26+97)
        else:
            decrypted+=char
    return decrypted
def gcd( a,  b):
    if (b == 0):
        return a
    return gcd(b, a % b);
     

def main():
    text=input("enter text: ")
    key1=int(input("enter key1(coprime of 26) for encryption: "))
    if(gcd(key1,26)==1):
         key2=int(input("enter key2 for encryption: "))
         key=list()
         key.append(key1)
         key.append(key2)
         encrypted=affine_encryption(text,key)
         decrypted=affine_decryption(encrypted,key)
         print("****encrypted text is*****")
         print(encrypted)
         print("****decrypted text is*****")
         print(decrypted)
    else:
        print("first key must be coprime to 26")


main()
    
            
            
