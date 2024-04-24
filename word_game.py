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
    player_one_word_bank = []
    player_two_word_bank = []


    # print(guessing_word)

    # Tell player the length of the word 
    print(f"The length of the word is: {len(guessing_word)}")
    print(f"The theme is animal")


    # keep looping until game is guessed right 
    p1_word_guess = False
     # while word isn't guessed yet and player 1 has up to 3 guesses
    while (not p1_word_guess):
        print("Player one's turn now")
        player_one_letter_guess = input("Guess the letter in the word bank: ")
        if player_one_letter_guess in guessing_word:

            # Section here covers if letter is properly guessed in
            occurences_in_guessing_word = guessing_word.count(player_one_letter_guess)
            print(f"The letter appears in the word {occurences_in_guessing_word} times")
            print(player_one_word_bank.append(player_one_letter_guess))
            player_one_guesses += 1
            
            #ask if player would like to guess again
            ask_question = input("Would you like to guess again? (y/n): ")
        #Repeat the task   
        if (ask_question == 'y'):
            
            
        elif (player_one_letter_guess not in guessing_word):
            player_one_guesses += 1        
        if len(player_one_letter_guess) > 1:
            print(f"You guessed a word, please guess a letter!")
        if player_one_guesses == 3:
            print("You ran out of guesses, game over")
            p1_word_guess = True
    



    # p2_word_guess = False
    # while not p2_word_guess:
    #     # while word isn't guessed yet and player 1 has up to 3 guesses
    #     print("Player two's turn now")
    #     player_two_letter_guess = input("Guess the letter in the word bank: ") 
    #     if player_two_letter_guess in guessing_word:
    #         occurences_in_guessing_word = guessing_word.count(player_two_letter_guess)
    #         print(f"The letter appears in the word {occurences_in_guessing_word} times")
    #         player_two_guesses += 1
    #         player_two_letter_guess += 1
    #     elif (player_two_letter_guess not in guessing_word):
    #         player_two_guesses += 1
    #     if len(player_two_letter_guess) > 1:
    #         print(f"You guessed a word, please guess a letter!")
    #     if player_two_guesses == 3:
    #         print("You ran out of guesses, game over")
    #         p2_word_guess = True
        

    
    word_game()
    # Commit 2 