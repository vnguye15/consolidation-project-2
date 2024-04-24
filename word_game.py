#Word Game 4/16/24
import random
import os
def word_game():

    word_bank = ["leopard", "lion", "dog", "seal"]

    # Counter to keep track of turns
    player_one_guesses = 0
    player_two_guesses = 0


    player_one_wrong_word_guesses = 0
    player_two_wrong_word_guesses = 0
    guessing_word = random.choice(word_bank)

    #Display list to hold for letters guessed for player 1 & 2
    p1_correct_letter_bank = []
    p1_incorrect_letter_bank = []

    p2_correct_letter_bank = []
    p2_incorrect_letter_bank = []

    #Scores for player 1 & 2
    p1_score = 0
    p2_score = 0

    # print(guessing_word)

    # Tell player the length of the word 
    print(f"The length of the word is: {len(guessing_word)}")
    print(f"The theme is animal")


    # keep looping until game is guessed right 
    word_in_bank = False
     # while word isn't guessed yet 
    while (not word_in_bank):
        #whenever p1 guesses letter, increase p1 score
        p1_letter_guess = input("Player one it is now your turn, guess the letter: ")
        p1_score += 1
        #if letter guessed is in the word
        if (p1_letter_guess in guessing_word):
                # show letter bank with letter guessed 
                p1_correct_letter_bank.append(p1_letter_guess)
                #then ask if they want to try guessing again <-- will lines 43-45 result in letter being asked again?
                print(p1_correct_letter_bank)
                ask_letter = input("Would you like to guess letter again? (y/n): ")

                
                if (ask_letter == 'n'):
                    #if player doesn't want to guess letter again, give them option to guess word
                    ask_word = input ("Would you like to guess the word? (y/n): ")
                #  if player chose yes
                    if (ask_word == 'y'):
                        p1_word_guess = input("Guess the word: ")
                        #if correct word is guessed, set to win. (Set word_in_bank to true to end loop)
                        if (p1_word_guess == guessing_word):
                            word_in_bank = True
                            print("Congrats you won")
                        #otherwise increase their number of wrong guesses by 1
                        else:
                            print("you guessed wrong try again")
                            player_one_wrong_word_guesses += 1
        #if player one gets 3 word guesses wrong than game ends
        if (player_one_wrong_word_guesses >= 3):
            print("You ran out of guesses, game over!")
            break

        #Otherwise if player 1 did not guess correct letter, keep track of times letter is guessed & add score                
        else:
            p1_incorrect_letter_bank.append(p1_letter_guess)
            print(p1_incorrect_letter_bank)
            p1_score += 1
            

    word_game()
    