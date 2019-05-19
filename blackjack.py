import random
A = 11
J = 11
Q = 11
K = 11
cards = [A,2,3,4,5,6,7,8,9,J,Q,K,A,2,3,4,5,6,7,8,9,J,Q,K,A,2,3,4,5,6,7,8,9,J,Q,K,A,2,3,4,5,6,7,8,9,J,Q,K]

you_hand1 = random.choice(cards)
you_hand2 = random.choice(cards)
print(you_hand1,you_hand2)

dealer_hand1 = random.choice(cards)
dealer_hand2 = random.choice(cards)
print(dealer_hand1,dealer_hand2)

you_add = 0
add = input("カードを追加しますか 1=YES, 2=NO: ")
if int(add) == 1 :
    you_add = random.choice(cards)
    print(you_add)

you_total = int(you_hand1) + int(you_hand2) + int(you_add)
dealer_total = int(dealer_hand1) + int(dealer_hand2)

if you_total > dealer_total:
    if you_total <= 21:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
elif you_total == dealer_total:
    print("DRAW")
else:
    if dealer_total <= 21:
        print("YOU LOSE!")
    else:
        print("YOU WIN!")



