import random


word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for i in range(word_length):
    placeholder += "_"

print(placeholder)
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter:").lower()
    display = ""
    for i in chosen_word:
        if guess == i:
            display += i
            correct_letters.append(i)
        elif i in correct_letters:
            display += i
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Current lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win")
