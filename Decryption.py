#decrytion function
def decryption():
    #kunin mo input ni user kung anong dedecrypt niya 
    msg_to_decrpypt = str(input("What is the message you want to decrypt?: "))
    #palitan yung mga symbols ng corresponding letters tapos print mo na output print mo narin output
    print(msg_to_decrpypt.replace("*","a").replace("&","e").replace("#","i").replace("+","o").replace("!","u"))
    

#encryption function
def encryption():
    #kunin mo input ni user kung anong encrypt niya
    msg_to_decrpypt = str(input("What is the message you want to decrypt?: "))
    #palitan yung mga letters ng corresponding symbols tapos print mo na output print mo narin output
    print(msg_to_decrpypt.replace("a","*").replace("e","&").replace("i","#").replace("o","+").replace("u","!"))
    


#tanong kay user kung encryption ba or decryption
user_input_decrypt_encrypt = str(input("Would you like to Decrypt or Encrypt a message? " ))
user_input_list_encrypt = ["e" , "E" , "Encrypt" , "ENCRYPT"]
user_input_list_decrypt = ["d" , "D" , "Decrypt" , "DECRYPT"]

if user_input_decrypt_encrypt in user_input_list_encrypt :
    encryption()
elif user_input_decrypt_encrypt in user_input_list_decrypt:
    decryption()