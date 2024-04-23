#Word Game 4/16/24
import random
word_bank = ["leopard", "lion", "dog", "seal"]

# Counter to keep track of turns
player_one_guesses = 0
player_two_guesses = 0


player_one_wrong_word_guesses = 0
player_two_wrong_word_guesses = 0
guessing_word = random.choice(word_bank)
# print(guessing_word)

# Tell player the length of the word 
print(f"The length of the word is: {len(guessing_word)}")
print(f"The theme is animal")


#First commit here


# keep looping until game is guessed right 
# word_guess = False
# while not word_guess:
#     player_one_letter_guess = input("Guess the letter in the word bank: ")
#     if player_one_letter_guess in guessing_word:
#         occurences_in_guessing_word = guessing_word.count(player_one_letter_guess)
#         print(f"The letter appears in the word {occurences_in_guessing_word}")
#         player_one_guesses += 1
#     elif (player_one_letter_guess not in guessing_word):
#         player_one_guesses += 1
#     if len(player_one_letter_guess) > 1:
#         print(f"You guessed a word, please guess a letter!")


# while not word_guess:
#     player_two_letter_guess = input("Guess the letter in the word bank: ")
#     if player_two_letter_guess in guessing_word:
#         occurences_in_guessing_word = guessing_word.count(player_two_letter_guess)
#         print(f"The letter appears in the word {occurences_in_guessing_word}")
#         player_two_guesses += 1
#     elif (player_two_letter_guess not in guessing_word):
#         player_two_guesses += 1
#     if len(player_two_letter_guess) > 1:
#         print(f"You guessed a word, please guess a letter!")

# Commit 2 