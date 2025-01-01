from playsound import playsound
import time 


morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',     
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',  
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',   
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',     
    'U': '..-',    'V': '...-',  'W': '.--',    'X': '-..-',   'Y': '-.--',  
    'Z': '--..',   '0': '-----', '1': '.----',  '2': '..---',  '3': '...--', 
    '4': '....-',  '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', 
    '9': '----.'
}
text="Happy new year"





def Play_morse(letter):
    morse = morse_code.get(letter.upper(), 'Invalid character')
    for i in morse:
        if i == "-":
            playsound('long.wav')
        elif i == ".":
            playsound('short.wav')



for word in text.split(" "):
    # well get word 
    for letter in word:
        Play_morse(letter)
        time.sleep(1)
    time.sleep(3)

  
