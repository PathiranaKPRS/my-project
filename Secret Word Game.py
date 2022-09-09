#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
words = ["Germany","Canada","Denmark","Finland","Austria"]
word = random.choice(words)
trys = 10
Sec_word = word[0] + "_" * (len(word) - 1)
game_over = False
print("Clue : Countries")

while not game_over:
    print("Attempts Left.." + str(trys))
    print(Sec_word)
    guess = input("Guess a letter..")
    
    g = 0
    if guess in word:
        while word.find(guess, g) != -1:
            g = word.find(guess, g)
            Sec_word = Sec_word[:g] + guess + Sec_word[g + 1:]
            g += 1
            trys -= 1
        print("Correct Guess")
    else:
        print("Wrong Guess")
        trys -= 1
    if word == Sec_word:
        print("You won !! Secret Word.. " + word)
        game_over = True
    if trys == 0:
        print("Oops, You lost !")
        game_over = True   

