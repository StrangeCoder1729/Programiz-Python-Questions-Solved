# Q30] Python Program to Shuffle Deck of Cards

import random

lst_numbers = []
for i in range(0,4):
    lst_numbers.append(random.randint(1,11))

# lst_numbers_set = set(lst_numbers)
lst_cards = ['Spade','Heart','Diamond','Club']


lst_cards_random = []
# lst_cards = list(set(lst_cards))

for i in range(0,len(lst_cards)):
    rand = random.randint(0,3)
    # print(f"rand : {rand}")
    lst_cards_random.append(lst_cards[rand])
# print(lst_cards_random)
 
for i in range(0,len(lst_cards)):
    print(lst_numbers[i],lst_cards[i])
