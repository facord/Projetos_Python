from random import choice

#Jogo
perguntarNovamente = True
game_on = True

def desenho(erros):
        if (erros == 0):
            print()
            print("|----- ")
            print("|    | ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("|      ")
            print("_      ")
            print()
        else:
            if erros == 1:
                 print()
                 print("|----- ")
                 print("|    | ")
                 print("|    O ")
                 print("|      ")
                 print("|      ")
                 print("|      ")
                 print("_      ")
                 print()
            else:
                if erros == 2:
                    print()
                    print("|----- ")
                    print("|    | ")
                    print("|    O ")
                    print("|    | ")
                    print("|      ")
                    print("|      ")
                    print("_      ")
                    print()
                else:
                    if erros == 3:
                        print()
                        print("|----- ")
                        print("|    | ")
                        print("|    O ")
                        print("|   /| ")
                        print("|      ")
                        print("|      ")
                        print("_      ")
                        print()
                    else:
                        if erros == 4:
                            print()
                            print("|----- ")
                            print("|    | ")
                            print("|    O ")
                            print("|   /|\\")
                            print("|      ")
                            print("|      ")
                            print("_      ")
                            print()
                        else:
                            if erros == 5:
                                print()
                                print("|----- ")
                                print("|    | ")
                                print("|    O ")
                                print("|   /|\\")
                                print("|   /  ")
                                print("|      ")
                                print("_      ")
                                print()
                            else:
                                if erros == 6:
                                    print()
                                    print("|----- ")
                                    print("|    | ")
                                    print("|    O ")
                                    print("|   /|\\")
                                    print("|   / \\")
                                    print("|      ")
                                    print("_      ")
                                    print()

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


while game_on:
    objects = ["computer","television"]
    palavra = choice(objects)
    palavra = (list(palavra))
    wordcount = len(palavra)
    answer = ["_"]*wordcount
    tentativas = []
    chances = 6
    
    #Começo do jogo
    erros = 0
    while perguntarNovamente:
        desenho(erros)
        letter = input ("Please enter a letter:")
        if letter in palavra:
            if letter in(tentativas):
                print("You already tried that letter!")
                continue
            else:
                print ("Correct!")
                letterPlace = findOccurences(palavra,letter)
                for i in letterPlace:
                    answer[i] = letter
                print (*answer)
                tentativas.append(letter)
        else:
            if letter in(tentativas):
                print("You already tried that letter!")
                continue
            else:
                print ("Wrong!")
                tentativas.append(letter)
                erros +=1
                continue
            
        if answer == palavra :
            print ("You guessed it! Well Done!")
            break
            #end here


