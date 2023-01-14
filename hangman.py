import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list).lower()
display = []


print(hangman_art.logo)
# for testing
#print(f"chosen word:{chosen_word}")

for ltr in chosen_word:
    display.append("_")
print(display)
lives = 6
print(hangman_art.stages[lives])
end_game = False
while not end_game:
    guess = input("Guess a word :")
    if guess in display:
        print("You've already typed this.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print("Letter is not in the word.")
        lives -= 1
        print(hangman_art.stages[lives])
    if "_" not in display:
        print("You win!")
        end_game = True
    if lives <= 0:
        print("Game over.You Lose.")
        print("The word is",chosen_word)
        end_game = True
