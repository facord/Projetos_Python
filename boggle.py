from random import choice
import time
from nltk.corpus import words

def dice():
    dice1 = ["N","E","E","H","G","W"]
    face1 = choice(dice1)
    print (" ----- "," -----","  ----- "," ----- ")
    print ("| ",face1," |", end =" " )
    
    dice2 = ["T","M","I","O","V","C"]
    face2 = choice(dice2)
    print ("| ",face2," |", end =" " )
    
    dice3 = ["Y","T","L","E","T","R"]
    face3 = choice(dice3)
    print ("| ",face3," |", end =" " )
    
    dice4 = ["N","L","N","H","R","Z"]
    face4 = choice(dice4)
    print ("| ",face4," |")
    print (" ----- "," -----","  ----- "," ----- ")
    print()
    
    print (" ----- "," -----","  ----- "," ----- ")
    dice5 = ["W","T","O","O","A","T"]
    face5 = choice(dice5)
    print ("| ",face5," |", end =" " )
    

    dice6 = ["I","U","N","E","E","S"]
    face6 = choice(dice6)
    print ("| ",face6," |", end =" " )
    
    dice7 = ["H","S","P","A","C","O"]
    face7 = choice(dice7)
    print ("| ",face7," |", end =" " )
    
    dice8 = ["S","S","O","I","E","T"]
    face8 = choice(dice8)
    print ("| ",face8," |")
    print (" ----- "," -----","  ----- "," ----- ")
    print()
    
    print (" ----- "," -----","  ----- "," ----- ")
    dice9 = ["B","A","O","B","O","J"]
    face9 = choice(dice9)
    print ("| ",face9," |", end =" " )
    
    dice10 = ["R","Y","V","D","E","L"]
    face10 = choice(dice10)
    print ("| ",face10," |", end = " ")

    dice11 = ["Q","U","M","H","N","I"]
    face11 = choice(dice11)
    print ("| ",face11," |", end =" " )
    
    dice12 = ["I","E","R","L","D","X"]
    face12 = choice(dice12)
    print ("| ",face12," |")
    print (" ----- "," -----","  ----- "," ----- ")
    print()
    
    print (" ----- "," -----","  ----- "," ----- ")
    dice13 = ["N","E","E","G","A","A"]
    face13 = choice(dice13)
    print ("| ",face13," |", end =" " )
    
    dice14 = ["F","P","S","A","K","F"]
    face14 = choice(dice14)
    print ("| ",face14," |", end =" " )
    
    dice15 = ["S","T","I","T","Y","P"]
    face15 = choice(dice15)
    print ("| ",face15," |", end =" " )

    dice16 = ["W","R","E","T","V","H"]
    face16 = choice(dice16)
    print ("| ",face16," |")
    print (" ----- "," -----","  ----- "," ----- ")
    print()
    print("You have 2 minuts to form words.")
    
def palavras():
    tentativas = []
    certas = []
    pontos = 0
    timeout = 120   # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        palavra = input ("Please enter a word: ")
        if palavra in(tentativas):
                print("You already tried that letter!")
                continue
        else:
            tentativas.append(palavra)
            load_words()
            if __name__ == '__main__':
                if len(palavra)>=3:
                    english_words = load_words()
                    existe = palavra in english_words
                    if existe == True:
                        certas.append(palavra)
                        if len(palavra)<=4: pontos = pontos+1
                        elif len(palavra)==5: pontos = pontos+2
                        elif len(palavra)==6: pontos = pontos+3
                        elif len(palavra)==7: pontos = pontos+5
                        elif len(palavra)>=8: pontos = pontos+11
    print("Time out...")
    print(certas)
    print("Your total: ", pontos)


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

dice()
palavras()
