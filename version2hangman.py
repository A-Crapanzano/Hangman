import random

with open("aleatoire.txt", encoding="utf-8") as f:
    mots = [ligne.strip() for ligne in f]

def save_score(score):
    with open("score.txt", "a", encoding="utf-8") as fichier:
        fichier.write(str(score) + "\n")

def best_score():
    try:
        with open("score.txt", "r", encoding="utf-8") as f:
            scores = [int(line) for line in f if line.strip().isdigit()]
            return max(scores) if scores else 0
    except FileNotFoundError:
        return 0


def french_random():
    my_set = mots
    word = random.choice(list(my_set))
    print (word)  
    return word

random_word = french_random()
print(random_word)

nb_penalites = 0
user_score = 0 

def spaces(random_word):
    n = len(random_word)
    result = ["_"] * n
    return result

print(spaces(random_word))
hidden = spaces(random_word)
print("".join(hidden))

def check_letter(random_word, user_input, hidden, nb_penalites, user_score):
    found = False
    for i, ch in enumerate(random_word):
        if ch == user_input and hidden[i] == "_": 
            hidden[i] = user_input
            user_score += 1
           
            found = True


    if not found:  
        nb_penalites += 1
        print ("Pénalités =", nb_penalites)
    else:
        user_score += 1
        print ("score:", user_score)
      
    return hidden, nb_penalites, user_score

def check_word(random_word, user_input, hidden, nb_penalites, user_score):
    if random_word == user_input:
        hidden = list(random_word)
        user_score += 12
        return hidden, nb_penalites, user_score   
    else:
        nb_penalites += 5             
        print("Pénalités =", nb_penalites)
        return hidden, nb_penalites, user_score

while "_" in hidden and nb_penalites < 12:
    user_input = input("Enter a word or letter: ").lower()
    if len(user_input) == 1:
        hidden, nb_penalites, user_score = check_letter(random_word, user_input, hidden, nb_penalites, user_score)
    else: 
        hidden, nb_penalites, user_score = check_word(random_word, user_input, hidden, nb_penalites, user_score)
        print("".join(hidden))

if "_" not in hidden:
    print("you won")
else:
    print("you lost")



save_score(user_score)
print("Votre score :", user_score)
print("Meilleur score actuel :", best_score())