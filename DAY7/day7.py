import random 

words = (History, After, Today, Cruel)

chosen_word = random.choice(words)
print(chosen_word)  # Output: random word from the tuple
guess = input("guess a aletter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print(Wrong)
        