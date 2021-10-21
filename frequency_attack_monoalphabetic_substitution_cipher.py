'''problem statement:Write a program that can perform a letter frequency attack on any monoalphabetic substitution cipher
   without human intervention. Your software should produce possible plain text in rough order of likelihood.
  It would be good if your user interface allows user to specify " Give me top 10 possible plain texts'''
'''author:bhavna '''

#function to generate 10 plain text correspoinding to given cipher text,take input an encrypted text encrypted by substitution scheme
def frequency_attack(text):
    length=len(text)
    plain_text=[None]*10 #array to store the plaintext generated
    freq=[0]*26      #to store the frequency of each item
    used=[0]*26  #to store used alphabet
    #getting frequency
    for i in range(length):
        if(text[i]!=" "):
            freq[ord(text[i])-65]+=1
    freq_incr=[0]*26
    for i in range(26):
        freq_incr[i]=freq[i]
    #reverse sorting th frequency
    freq_incr.sort(reverse=True)
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    for i in range(10):
        ch = -1
         
        # Iterate over the range [0, 26]
        for j in range(26):
            if freq_incr[i] == freq[j] and used[j] == 0:
                used[j] = 1
                ch = j
                break
             
        if ch == -1:
            break
         
        # Store the numerical equivalent of letter
        # at ith index of array letter_frequency
        x = ord(T[i]) - 65
         
        # Calculate the probable shift used
        # in monoalphabetic cipher
        x = x - ch
         
        # Temporary string to generate one
        # plaintext at a time
        curr = ""
         
        # Generate the probable ith plaintext
        # string using the shift calculated above
        for k in range(length):
             
            # Insert whitespaces as it is
            if text[k] == ' ':
                curr += " "
                continue
             
            # Shift the kth letter of the
            # cipher by x
            y = ord(text[k]) - 65
            y += x
             
            if y < 0:
                y += 26
            if y > 25:
                y -= 26
             
            # Add the kth calculated/shifted
            # letter to temporary string    
            curr += chr(y + 65)
             
        plain_text[i] = curr
     
    # Print the generated 10 possible plaintexts
    print("********possible 10 plain text correspoinding to cipher**************")
    for i in range(10):
        print(plain_text[i])
    
def main():
    print("****enter only Upper case letters****")
    response="yes"
    while response=="yes":
        text=input("enter cipher text: ")
        frequency_attack(text)
        response=input("want another?yes/no")
main()
    
