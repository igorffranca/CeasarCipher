alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def ceasar(text, shift, direction):
    if direction == "encode":
        plain_text = text
        cipher_text = ''
        for letter in plain_text:
            if not letter.isalpha() or letter.isspace():
                cipher_text += letter
                continue
            index = alphabet.index(letter)
            cipher_text += alphabet[index + shift]
    
        print(f"The encoded text is {cipher_text}")
    
    elif direction == "decode":
        plain_text = ''
        cipher_text = text
        for letter in cipher_text:
            if not letter.isalpha() or letter.isspace():
                plain_text += letter
                continue
            index = alphabet.index(letter)
            plain_text += alphabet[index - shift]

        print(f"The decoded text is {plain_text}")
    else:
        print("Invalid option! Try again..")

while True:
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 25

    ceasar(direction=direction, text=text, shift=shift)

    exit_question = input("Would you like to go again? Type 'yes' or 'no'.\n")
    if exit_question != "yes" and exit_question != "no":
        print("Invalid option.")
        while True:
            exit_question = input("Would you like to go again? Type 'yes' or 'no'.\n")
            if exit_question == "yes" and exit_question == "no":
                break
        
    else:
        if exit_question == "yes":
            continue
        else:
            print("Goodbye")
            break

        
        