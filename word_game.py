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
        # ** SECTION COVERS PLAYER GUESSES LETTER CORRECTLY ** 
        #whenever p1 guesses letter, increase p1 score
        p1_letter_guess = input("Player one it is now your turn, guess the letter: ")
        p1_score += 1
        #if letter guessed is in the word
        if (p1_letter_guess in guessing_word):
            #if the letter guessed IS NOT already in the word bank then add it
            if (p1_letter_guess not in p1_correct_letter_bank):
                # show letter bank with letter guessed & add score
                p1_correct_letter_bank.append(p1_letter_guess)
                print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                p1_score += 1
            #otherwise ignore the same guessed letter and just add score by 1     
            else:
                print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                p1_score += 1

        # ** SECTION COVERS PLAYER GUESSES LETTER INCORRECTLY ** 
         #Otherwise if player 1 did not guess correct letter, keep track of times letter is guessed & add score                
        if (p1_letter_guess not in guessing_word):
            #if the guessed letter is not in incorrect letter bank, add onto the letter bank
            if (p1_letter_guess not in (p1_incorrect_letter_bank)):
                p1_incorrect_letter_bank.append(p1_letter_guess)
                print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                p1_score += 1
            else: # already guessed ignore
                print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                p1_score += 1

        #After each guess, ask if they want to guess letter again    
        ask_letter = input("Would you like to guess letter again? (y/n): ")

        #if player doesn't want to guess letter again, give them option to guess word
        ask_word = input ("Would you like to guess the word? (y/n): ")
        if (ask_letter == 'n'):
            #if they asked no continue
            continue
            # if player chose yes
            if (ask_word == 'y'):
                p1_word_guess = input("Guess the word: ")
                #if correct word is guessed, set to win. (Set word_in_bank to true to end loop)
                if (p1_word_guess == guessing_word):
                    word_in_bank = True

                    #Show p1 their score along with congrats
                    print(f"*** Congrats! P1 won with score: {p1_score} ***")
                #otherwise increase their number of wrong guesses by 1
                else:
                    player_one_wrong_word_guesses += 1
                    print(f"You guessed wrong try again ! [Tries: {player_one_wrong_word_guesses}]")
            #Player decides not to guess word, go back and guess letter        
            elif (ask_word == 'n'):
                p1_letter_guess = input("Player one it is now your turn, guess the letter: ")
                p1_score += 1

        #if player one gets 3 word guesses wrong than game ends
        if (player_one_wrong_word_guesses >= 3):
            print("You ran out of guesses, game over!")
            break
       
            
#####################################################################################


# #Player Two section
#     while (not word_in_bank):
#         #whenever p1 guesses letter, increase p1 score
#         p2_letter_guess = input("Player one it is now your turn, guess the letter: ")
#         p2_score += 1
#         #if letter guessed is in the word
#         if (p2_letter_guess in guessing_word):
#             #if the letter guessed IS NOT already in the word bank then add it
#             if (p2_letter_guess not in p1_correct_letter_bank):
#                 # show letter bank with letter guessed & add score
#                 p2_correct_letter_bank.append(p2_letter_guess)
#                 print(f"Correct Letter Bank: {p2_correct_letter_bank}")
#                 p2_score += 1
#             #otherwise ignore the same guessed letter and just add score by 1     
#             else:
#                 print(f"Correct Letter Bank: {p2_correct_letter_bank}")
#                 p2_score += 1
#             #After each guess, ask if they want to guess letter again    
#             ask_letter = input("Would you like to guess letter again? (y/n): ")


#         #if player doesn't want to guess letter again, give them option to guess word
#         if (ask_letter == 'n'):
#             ask_word = input ("Would you like to guess the word? (y/n): ")
#             # if player chose yes
#             if (ask_word == 'y'):
#                 p2_word_guess = input("Guess the word: ")
#                 #if correct word is guessed, set to win. (Set word_in_bank to true to end loop)
#                 if (p2_word_guess == guessing_word):
#                     word_in_bank = True

#                     #Show p1 their score along with congrats
#                     print(f"*** Congrats! P1 won with score: {p2_score} ***")
#                 #otherwise increase their number of wrong guesses by 1
#                 else:
#                     player_two_wrong_word_guesses += 1
#                     print(f"You guessed wrong try again ! [Tries: {player_two_wrong_word_guesses}]")
#         #if player one gets 3 word guesses wrong than game ends
#         if (player_two_wrong_word_guesses >= 3):
#             print("You ran out of guesses, game over!")
#             break
#         #Otherwise if player 1 did not guess correct letter, keep track of times letter is guessed & add score                
#         elif (p2_letter_guess not in guessing_word):
#             #if the guessed letter is not in incorrect letter bank, add onto the letter bank
#             if (p2_letter_guess not in (p2_incorrect_letter_bank)):
#                 p2_incorrect_letter_bank.append(p2_letter_guess)
#                 print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
#                 p2_score += 1
#             else: # otherwise its not so we just ignore it 
#                 print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
#                 p2_score += 1
#             ask_word = input ("Would you like to guess the word? (y/n): ")



word_game()

    