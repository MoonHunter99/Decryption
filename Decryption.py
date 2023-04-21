#decrytion function
def decryption():
    print("\033[1;34;40m `"*134)
    #kunin mo input ni user kung anong dedecrypt niya 
    msg_to_decrpypt = str(input("What is the message you want to decrypt?: "))
    #palitan yung mga symbols ng corresponding letters tapos print mo na output print mo narin output
    print(msg_to_decrpypt.replace("*","a").replace("&","e").replace("#","i").replace("+","o").replace("!","u"))
    print("\033[1;34;40m `"*134)
    

#encryption function
def encryption():
    print("\033[1;36;40m `"*134)
    #kunin mo input ni user kung anong encrypt niya
    msg_to_decrpypt = str(input("What is the message you want to decrypt?: "))
    #palitan yung mga letters ng corresponding symbols tapos print mo na output print mo narin output
    print(msg_to_decrpypt.replace("a","*").replace("e","&").replace("i","#").replace("o","+").replace("u","!"))
    print("\033[1;36;40m `"*134)
    


#tanong kay user kung encryption ba or decryption
print("\033[1;33;40m `"*134)
user_input_decrypt_encrypt = str(input("Would you like to Decrypt or Encrypt a message? " ))
user_input_list_encrypt = ["e" , "E" , "Encrypt" , "ENCRYPT"]
user_input_list_decrypt = ["d" , "D" , "Decrypt" , "DECRYPT"]

if user_input_decrypt_encrypt in user_input_list_encrypt :
    encryption()
elif user_input_decrypt_encrypt in user_input_list_decrypt:
    decryption()