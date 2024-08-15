import random
name = input("Enter your name: ")
word_list = ["hello", "duck", "bye", "no"]
print("Hello", name, "to the game:")
word = random.choice(word_list)
print("Word to guess:", word)
tries = 12
guess = ''

while tries > 0:
    Guess = input("Enter any alphabet: ")
    guess += Guess
    
    if Guess not in word:
        tries -= 1
        print("Wrong")
    
    for char in word:
        if char in guess:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()  

print("Game Over")
