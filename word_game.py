#Word Game (Started - 4/16/24, Finished - 5/5/24)


import random
import os
def word_game():
    
    game_is_over = False
    while (not game_is_over):

        word_bank = ["leopard", "lion", "dog", "seal", "cat", "snake", "wolf", "sheep", 
                     "cheetah", "rat", "pig", "shark", "octopus", "hamster", "horse"]

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
        p1_word_in_bank = False
        # while word isn't guessed yet 
        while (not p1_word_in_bank):
            # ** SECTION COVERS PLAYER GUESSES LETTER CORRECTLY ** 
            #whenever p1 guesses letter, increase p1 score
            print("---------------------------------")
            p1_letter_guess = input("Player one it is now your turn, guess the letter: ")
            if " " in p1_letter_guess: 
                print("No spaces. Try again")
            p1_score += 1
            #if letter guessed is in the word
            if (p1_letter_guess in guessing_word):
                #if the letter guessed IS NOT already in the word bank then add it
                if (p1_letter_guess not in p1_correct_letter_bank):
                    # show letter bank with letter guessed & add score
                    p1_correct_letter_bank.append(p1_letter_guess)
                    print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                    p1_score += 1
                #otherwise ignore the same guessed letter and just add score by 1     
                else:
                    print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                    p1_score += 1

            # ** SECTION COVERS PLAYER GUESSES LETTER INCORRECTLY ** 
            #Otherwise if player 1 did not guess correct letter, keep track of times letter is guessed & add score                
            if (p1_letter_guess not in guessing_word):
                #if the guessed letter is not in incorrect letter bank, add onto the letter bank
                if (p1_letter_guess not in (p1_incorrect_letter_bank)):
                    p1_incorrect_letter_bank.append(p1_letter_guess)
                    print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                    p1_score += 1
                else: # already guessed ignore
                    print(f"Correct Letter Bank: {p1_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p1_incorrect_letter_bank}")
                    p1_score += 1

            #After each guess, ask if they want to guess letter again   
            #If player wants to guess letter again, prompt question 
            ask_letter = input("Would you like to guess letter again? (y/n): ")
            if (ask_letter == 'n'):
                # Player chooses no to letter, ask if they want to guess word
                ask_word = input("Would you like to guess the word? (y/n): ")
                # Player wants to guess word
                if (ask_word == 'y'):
                    p1_word_guess = input("Guess the word: ")
                    #if correct word is guessed, set to win. (Set word_in_bank to true to end loop)
                    if (p1_word_guess == guessing_word):
                        word_in_bank = True
                        #Show p1 their score along with congrats
                        print(f"*** Congrats! P1 won with score: {p1_score} ***")
                    #Player guessed word wrong, increase score
                    else:
                        player_one_wrong_word_guesses += 1
                        print(f"You guessed wrong try again ! [Tries: {player_one_wrong_word_guesses}]") 
                    #Player decides not to guess word, go back and guess letter by skipping over (continue)     
                elif (ask_word == 'n'):
                    continue
            #if player one gets 3 word guesses wrong than game ends
            if (player_one_wrong_word_guesses >= 3):
                print("You ran out of guesses, game over!")
                print("---------------------------------")
                break
        
                
    #####################################################################################
    # Section covers p2 turn now 

        print(f"The length of the word is: {len(guessing_word)}")
        print(f"The theme is animal")
        p2_word_in_bank = False

    # while word isn't guessed yet 
        while (not p2_word_in_bank):
            # ** SECTION COVERS PLAYER GUESSES LETTER CORRECTLY ** 
            #whenever p1 guesses letter, increase p1 score
            print("---------------------------------")
            p2_letter_guess = input("Player two it is now your turn, guess the letter: ")
            p2_score += 1
            if " " in p1_letter_guess: 
                print("No spaces. Try again")
            #if letter guessed is in the word
            if (p2_letter_guess in guessing_word):
                #if the letter guessed IS NOT already in the word bank then add it
                if (p2_letter_guess not in p2_correct_letter_bank):
                    # show letter bank with letter guessed & add score
                    p2_correct_letter_bank.append(p2_letter_guess)
                    print(f"Correct Letter Bank: {p2_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
                    p2_score += 1
                #otherwise ignore the same guessed letter and just add score by 1     
                else:
                    print(f"Correct Letter Bank: {p2_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
                    p2_score += 1

            # ** SECTION COVERS PLAYER GUESSES LETTER INCORRECTLY ** 
            #Otherwise if player 1 did not guess correct letter, keep track of times letter is guessed & add score                
            if (p2_letter_guess not in guessing_word):
                #if the guessed letter is not in incorrect letter bank, add onto the letter bank
                if (p2_letter_guess not in (p2_incorrect_letter_bank)):
                    p2_incorrect_letter_bank.append(p2_letter_guess)
                    print(f"Correct Letter Bank: {p2_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
                    p2_score += 1
                else: # already guessed ignore
                    print(f"Correct Letter Bank: {p2_correct_letter_bank}")
                    print(f"Incorrect Letter Bank: {p2_incorrect_letter_bank}")
                    p2_score += 1

            #After each guess, ask if they want to guess letter again   
            #If player wants to guess letter again, prompt question 
            ask_letter = input("Would you like to guess letter again? (y/n): ")
            if (ask_letter == 'n'):
                # Player chooses no to letter, ask if they want to guess word
                ask_word = input("Would you like to guess the word? (y/n): ")
                # Player wants to guess word
                if (ask_word == 'y'):
                    p2_word_guess = input("Guess the word: ")
                    #if correct word is guessed, set to win. (Set word_in_bank to true to end loop)
                    if (p2_word_guess == guessing_word):
                        word_in_bank = True
                        #Show p1 their score along with congrats
                        print(f"*** Congrats! P2 won with score: {p2_score} ***")
                        break
                    #Player guessed word wrong, increase score
                    else:
                        player_two_wrong_word_guesses += 1
                        print(f"You guessed wrong try again ! [Tries: {player_two_wrong_word_guesses}]") 
                    #Player decides not to guess word, go back and guess letter by skipping over (continue)     
                elif (ask_word == 'n'):
                    continue
            #if player one gets 3 word guesses wrong than game ends
            if (player_two_wrong_word_guesses >= 3):
                print("You ran out of guesses, game over!")
                break
            
        

        # SECTION COVERS SCORES 
        if (p1_score < p2_score):
            print(f"Player One Won with Score: {p1_score}")
            game_is_over = True
        elif (p2_score < p1_score):
            print(f"Player two won with Score: {p2_score}")
            game_is_over = True
        else:
            print("It's a tie!")
            game_is_over = True
    #Game Over is printed         
    print("GAME OVER ")
word_game()

