import random
from words import words

def division(x):
    print("-="*len(x) + "-")

doll = [
 ' +--+\n |  |\n |    \n |      \n |     \n |\n=======',
 ' +--+\n |  |\n |  O \n |      \n |     \n |\n=======',
 ' +--+\n |  |\n |  O \n |  |   \n |     \n |\n=======',
 ' +--+\n |  |\n |  O \n |  |\ \n |     \n |\n=======',
 ' +--+\n |  |\n |  O \n | /|\ \n |     \n |\n=======',
 ' +--+\n |  |\n |  O \n | /|\  \n | /   \n |\n=======',
 ' +--+\n |  |\n | (x)\n | /|\  \n | / \ \n |\n=======']


hangman_continue = True

while hangman_continue != False:

    

    word = words[random.randint(0, len(words))].upper() #Word é escolhida dentre de varias outras 
    guess_word = "- "*(len(word)) 
    life = 0
    letter_used = []
    wrong_letter_guessed = "   [Wrong letter used]:"


    division("THE HANGMAN GAME")
    print("THE HANGMAN GAME!".center(33))
    division("THE HANGMAN GAME")

    while True:
        if guess_word.split() == list(word): #condição para a vitoria guess_word == word
            division(word)
            print(f"The word was {word}\nYou Won Pog\n")
            break
        if life == len(doll)- 1: # O jogo acaba se life == ao ultimo boneco que é a representação do ultimo hp do jogador
            division(word)
            print(doll[life]) # mostra o boneco morto 
            division(word)
            print(f"The word was {word}\nGame Over FeelsBadMan\n")
            break
        print(doll[life]) # mostar o boneco correspondente a vida do jogador
        
        print(guess_word, wrong_letter_guessed,"\n") #mostra a palavra a ser adivinhada na forma ex: "_ _ _ _" --> "T _ _  _"  até a palavra ser adivinhada no caso "T E S T"


        letter = input('Tell me a letter: ').upper().strip() # Jogador escolhe uma letra

        while letter in letter_used or letter == "" or len(letter) > 1:
            if letter in letter_used:
                letter = input('Tell me a letter NOT USED: ').upper().strip()
            else:
                letter = input('Tell me a VALID! letter: ').upper().strip()


        if letter in word:  #se a letra escolhida estiver em word, então guess_word vai ser alterado com a letra no exato lugar onde ela pertence (isso funciona com letras repetidas)
            for iten in range(len(word)): ## iten será usado como index para alterar o elemento correspondente 
                if letter == word[iten]:
                    guess_word = guess_word.split() ## transforma isso "_ _ _ _ " em ["_","_","_","_"]
                    guess_word[iten] = letter ## adiciona a letra no seu lugar na lista ["T","_","_","_"]
                    guess_word = " ".join(guess_word) ## transfoma a lista em string "T _ _ _"  DEPOIS O LOOP WHILE CONTINUA
        else:
            wrong_letter_guessed = wrong_letter_guessed + " " +  str(letter) + " "
            life +=1
        letter_used.append(letter)

    x = input ('Do You Want To Continue? ? [S/N]: ')

    x = str(x)

    if len(x) > 0:
        if x[0].strip().upper() == "N":
            hangman_continue = False
