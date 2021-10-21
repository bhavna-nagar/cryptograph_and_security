'''problem statement:Write a program that can encrypt and decrypt using a 2 X 2 Hill Cipher.'''
'''author:bhavna nagar'''
'''function to encrypt text using key
   key:2*2 matrix
   text:user input(only upper case letter)
   E(x)=KP(mod26) where x is letter of plain text,K is key matrix and P IS PLAINTEXT MATRIX'''

def hill_cipher(text,key):
    length=len(text)
    encrypted=""
    #if text has odd number of letters
    if length%2!=0:length=length-1
    #looping through text taking pair of characters
    for i in range(0,length,2):
        a=ord(text[i])-65 #converting into number in range 0 to 25
        b=ord(text[i+1])-65 #converting into number in range 0 to 25
        #each letter of encrypted text is element of product of matrix K and p and applying mod 26
        encrypted+=chr((key[0][0]*a+key[0][1]*b)%26+65) 
        encrypted+=chr((key[1][0]*a+key[1][1]*b)%26 +65)
    return encrypted


#extended eculid theorem
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


#function to get inverse of a correspoinding to mod m
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  
    else:
        return x % m
    
'''function to decrypt text using key
   key:2*2 matrix
   text:encrypted text(only upper case letter)
   D(x)=K_inverse*P(mod26) where x is letter of encrypted text,K is key matrix,k_invers is multiplicative inverse of K
   and P IS Encrypted MATRIX'''

def decryption(encrypted,key):
    length=len(encrypted)
    decrypted=""
    #if text has odd number of letters
    if length%2!=0 : length=length-1
    #computing determinant of K matrix
    det=key[0][0]*key[1][1]-key[1][0]*key[0][1]
    det=modinv(det,26) #finding inverse of det correspoinding to mod 26
    #altering K to convert into inverse of K
    key[0][0],key[1][1]=key[1][1],key[0][0]
    key[1][0]=-key[1][0]
    key[0][1]=-key[0][1]
    for i in range(0,length,2):
        a=ord(encrypted[i])-65 #converting letters of cipher into numbers in range 0-25
        b=ord(encrypted[i+1])-65#converting letters of cipher into numbers in range 0-25
        #each letter of encrypted text is element of product of matrix K and p and applying mod 26
        decrypted+=chr(((key[0][0]*a+key[0][1]*b)*det)%26+65)
        decrypted+=chr(((key[1][0]*a+key[1][1]*b)*det)%26 +65)
    return decrypted
        
    

def main():
    response="yes"
    print("*******enter only upper case letter(no spaces,no number,no symbol******")
    print("****if it is taking hard to get key use key:3 3 2 5 *****")
    #enter only upper_case letter
    while(response=="yes"):
         text=input("enter text to encrypt(only uppercase letter): ")
         l=len(text)
         key=list()
         '''get key'''
         for i in range(2):
            temp=list()
            for j in range(2):
                a=int(input("enter value (in integer for key): "))
                temp.append(a)
            key.append(temp)
       #computing determinant to check choosen key is valid or not
         det=key[0][0]*key[1][1]-key[1][0]*key[0][1]
         det=modinv(det,26)
         if det==None:
             print("Key Invalid")
         else:
             encrypted=hill_cipher(text,key)
             print("****encrypted text****")
             if(len(text)%2!=0):
                 print(encrypted+text[l-1])
             else:
                 print(encrypted)
             decrypted=decryption(encrypted,key)
             print("****decrypted text****")
             if(len(text)%2!=0):
                 print(decrypted+text[l-1])
             else:
                 print(decrypted)
         response=input("want another?yes/no")

main()
        
        
        
        
