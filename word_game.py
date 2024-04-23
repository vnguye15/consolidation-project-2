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
