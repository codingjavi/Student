import string
import random
#get a random word
words = ["bird", "turd", "herd", "python", "chair", "glass", "mop", "shoes", "dog", "mat", "cat", "hereditary", "television", "sousaphone"]
word = random.choice(words)
loop = 0
win = False

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

blank_board = []
x = 0
for i in word:
     #inserting a blank space for every index
    blank_board.insert(x, " ")
    x = x+1

#function to make the letter board
def word_board():
    board = []
    x = 0
    for i in word:
        board.insert(x, i)
        x=x+1
    return(board)

#function to make a blank board that matches the random word
"""def hidden_board():
    blank_board = []
    x = 0
    for i in word:
        #inserting a blank space for every index
        blank_board.insert(x, " ")
        x = x+1
    #its adding an extra space so we remove it
    #blank_board.pop(len(blank_board)-1)
    return blank_board"""
    
#can't use global for blank_board because blank_board is in another function SO we have to call the function hidden_board()
def check_guess(guess):
    global loop
    global blank_board


    #checks all the letters in word
    check = False
    for i in word:
        if i == guess:
            #finding where in the letter guess equals i using .index()
            placing = word.index(guess)
            
            #inserting the users guess into the blank board
            #inserting method doesn't work, we have to replace the blank space with the guess
            blank_board[placing] = guess
            check = True
    if check == False:
        loop = loop + 1
        print("Sorry, that letter isn't in the word")
            
    return (blank_board)

#function to show hang man
def hangman_board_add(turn):
    hangman_board={
        0:
        """
        +---+
        |   |
            |
            |
            |
            |
        =========""",
        1:
        """ 
        +---+
        |   |
        o   |
            |
            |
            |
        =========""",
        2:
        """
        +---+
        |   |
        o   |
        |   |
        |   |
            |
        =========""",
        3:
        """
         +---+
         |   |
         o   |
        \|   |
         |   |
             |
        =========""",
        4:
        """
         +---+
         |   |
         o   |
        \|/  |
         |   |
             |
        =========""",
        5:
        """ 
         +---+
         |   |
         o   |
        \|/  |
         |   |
        /    |
        =========""",
        6:"""
         +---+
         |   |
         o   |
        \|/  |
         |   |
        / \  |
        ========="""
    }
    return hangman_board[turn]

def check_win():
    global win
    if word_board() == blank_board:
        win = True
    return win

#to check word with guess
def play():
    global alphabet_list
    global word
    global loop
    #while loop to keep playing until limbs = sixth or word is good
    while loop < 6:
        #print board
        print(hangman_board_add(loop))

        #print word board
        print(blank_board)

        #how to end the game if we won


        #get users input
        check = False
        while check == False:
            user_guess = input("Guess a letter ")
            if user_guess not in alphabet_list:
                print("Sorry, type in a valid letter")
                continue
            else:
                check = True
         
        #making it lowercase in case user puts in an upper case letter
        print(check_guess(user_guess.lower()))

        if check_win() is True:
            break

        #checkwin function?    
    #check guess with word
    if check_win() is True:
        print("Congrats you win!!!!")
    else:
        print("You lose!!!")
        print(hangman_board_add(6))
        print("The word was " + str(word_board()))
    #adds limb or letter
    
    
play()
