MORSE_ALPHABET = {'a':'o-','b':'-ooo','c':'-o-o','d':'-oo','e':'o','f':'oo-o','g':'--o',
                  'h':'oooo','i':'oo','j':'o---','k':'-o-','l':'o-oo','m':'--','n':'-o',
                  'o':'---','p':'o--o','q':'--o-','r':'o-o','s':'ooo','t':'-','u':'oo-',
                  'v':'ooo-','w':'o--','x':'-oo-','y':'-o--','z':'--oo'}

def converter(word:str):
    morse_code = ""
    for letter in word:
        if letter in MORSE_ALPHABET:
            morse_code += f"{MORSE_ALPHABET[letter]} "
        elif letter == " ":
            morse_code += "   "
        else:
            print(f"Ignored character: {letter}")
    return morse_code
    
if __name__ == "__main__":
    word_input = input("Type your message to be converted to Morse code: \n").lower()
    converted = converter(word_input)
    print(converted)
