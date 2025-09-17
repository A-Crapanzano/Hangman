
#user_input = input("Enter a word: ")

#def lose(penality):
#    if penality >= 12:
#        print("You lose!")

#lose(12)

#import random

#def aleatoire():

# my_set = {1,2,3,4,5,6} 

# print("An element from the set:" , random.choice(list(my_set)))

#aleatoire()

#import random

#from english_words import english_words_set

#def english_random():
#  my_set = english_words_set
#  print("An element from the set:" , random.choice(list(my_set)))

#english_random()


#// ASSEMBLAGE POUR LE PROGRAMME PENDU //

#// Consignes //
#Players have to guess a word with a minimum of penalties.
#Each turn, a player suggests a letter:
#✓ if the word contains it, each occurrence of the letter is revealed;
#✓ if the word does not contain it, the player gets 1 penalty.
#At any time, the player can propose a full word:
#✓ if the word is the one to be guessed, the player wins:
#✓ else, the player gets 5 penalties.
#If the number of penalties exceeds 12, the player looses.

#//consignes //


import random

from english_words import english_words_set

def english_random():
  my_set = english_words_set
  word = random.choice(list(my_set))
  return word


random_word = english_random()

print (random_word)

n = len(random_word)

#penalite = 1
#max(penalite) = 12

def spaces(random_word):
    n = len(random_word)
    result = ["_ "] * n
    return (result)

hidden = spaces(random_word)
print (" ".join(hidden))


user_input = input("Enter a word or letter: ").lower()


def check_letter(random_word, user_input, hidden):
    if len(user_input) != 1:
        print("Enter a single letter")
        return hidden

    for i in range(len(random_word)):
        if random_word[i] == user_input:
            hidden[i] = user_input

    print(" ".join(hidden))

    
    while "_" in hidden:
        user_input = input("Enter a word or letter: ").lower()
        hidden = check_letter(random_word, user_input, hidden)

    return hidden

	



#def penality(current_penalties user_input, random_word):
#    if random_word[i] != user_input :
#        current_penalties += 1
#    print (current_penalties)

def check_word(random_word, user_input):
	if random_word == user_input:
		print ("win")
	else:
		print ("false")

hidden = check_letter(random_word, user_input, hidden)
check_word(random_word, user_input)

#   (rajouter penalité avec else)







#def penality(current_penalties, check_word):

   # if check_word return False
  #      current_penalties += 5
  #  return current_penalties


#def lose(current_penalties):
 #    if current_penalties >= 12:
  #       print("You lose!")


     
