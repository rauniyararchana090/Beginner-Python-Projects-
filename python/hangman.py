import random
from words import words 
import string

def get_valid_word(words): #we get word that doesn't have _ or space in it
    word=random.choice(words)
    while '_' in word or ' 'in word:
        word = random.choice(words)
    return word    

def hangman():
    word =get_valid_word(words)   
    word_letters =set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters= set() #keep tracks what the user has gussed
    lives = 6
    #getting user input
    while len(word_letters)>0 and lives >0:
        #letter used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print( 'You have',lives, 'lives left and You have used these letters :',' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word',' '.join(word_list))

        user_letter =input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1    #takes away a life if wrong
                print("letters are not in words")
        elif user_letter in used_letters:
            print('You have already used that character.please try again') 

        else:
            print('Invalid character.Please try again')   

     #gets here when len(word_letter) ==0   
    if lives == 0:
        print ("You are dead, sorr The word was",word)
    else:
        print("You guessed the word",word,"!!")  
hangman()                     


