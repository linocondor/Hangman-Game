import random
import figures_hungman
import word_hangman
from replit import clear

print(figures_hungman.logo)

word_list = word_hangman.word_list
word = random.choice(word_list)

print(word)



spaces=[]
for n in range(0, len(word)):
        spaces += "_"

end_of_game = False
lives = 6

while not end_of_game:

    
    print(f"Lives: {lives}")
    print(f"{' '.join(spaces)}")
    print(figures_hungman.stages[lives])

    
    Guess = input("Guess a letter: ").lower()
    clear()
      
    if Guess in word and Guess not in spaces:
        print(f"You choose the letter {Guess}, this letter is in the word")
        for n in range(0, len(word)):
            if Guess == word[n]:
                spaces[n] = Guess
    
    elif Guess in word:
        print(f"You alredy choose the letter {Guess}")
        lives -= 1 
    else:
        lives -= 1 
        print(f"You choose the letter {Guess}, this letter is not in the word")       
        
        
    

    if "_" not in spaces:
        end_of_game = True
        print(f"{' '.join(spaces)}")
        print(figures_hungman.stages[lives])
        print("You win")
    if lives == 0:    
        end_of_game = True
        print(f"{' '.join(spaces)}")
        print(figures_hungman.stages[lives])
        print("You loose")

    

