import random

import hangman_words
import hangman_art

print(hangman_art.logo)
print("This is a hangman game")
#test word list
#word_list = ["ardvark", "baboon", "camel"]

#randlonly choose work from list from file
choosen_word = random.choice(hangman_words.word_list)
word_length = len(choosen_word)

#Testing code
print(f'Pssst, the solution is {choosen_word}.')

#have a place to hold correct guesses and set the number of lives/false guesses to 6
hold_guesses = ["_"] * word_length 
end_of_game = False
lives = 6


def win() :         
    print("You solved the puzzle")
    print("Congratulations!")
    print(hold_guesses)  
    end_of_game = True

def lose() :
    print(f"You lose.  The answer is {choosen_word}") 
    print(hold_guesses)
    end_of_game = True


# Keep asking for guesses until the puzzle is solved or there are no more lives left
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    # check if the letter is in the choosen word
    # and update the blanks of the hidden word

    exists_count = choosen_word.count(guess)
    if exists_count > 0: 
        x = range(0, word_length)
        for i in x:        
            if (choosen_word[i] == guess) :
                hold_guesses[i] = guess
        print(hold_guesses)
        if (hold_guesses.count("_") == 0):
            win()
            break 
    else:
        lives = lives -1
        print(f" You have {lives} lives remaining.\n") 
        if (lives == 0):
            lose()
            break
               

#alternate solution
    #Check guessed letter
    #for position in range(word_length):
    #    letter = chosen_word[position]
    #    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    #    if letter == guess:
    #       display[position] = letter
    



