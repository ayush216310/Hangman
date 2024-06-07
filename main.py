import random
from words import *
from hangman import *
print(logo)
guessed=0
word = random.choice(word_list)
lives=6
display=[]
for _ in range(len(word)):
    display.append('_')
i=0
while (lives>0):
    guess = input("Guess a letter : ")
    b=0
    for l in word:
        if guess==l :
            display[b]=guess
            guessed=1
        b+=1
    if guessed == 0 :
        lives-=1
        print(f"Lost a life ! :(\t\tLives left : {lives}")

    else :
        print(f"Correct guess ! :)\t\tLives left : {lives}")
    print(stages[lives])
    guessed=0
    print(" ".join(display))
    i+=1
    if "".join(display)==word:
        print("Congratulations you won the game! :)")
        break
if "".join(display)!=word:
    print("Lives Over. You lose! :(")
print('Game Over.')
