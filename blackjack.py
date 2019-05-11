import random
cards = ["A",2,3,4,5,6,7,8,9,"J","Q","K","A",2,3,4,5,6,7,8,9,"J","Q","K","A",2,3,4,5,6,7,8,9,"j","Q","K","A",2,3,4,5,6,7,8,9,"J","Q","K"]
print(random.choice(cards))
print(random.choice(cards))
add = input("カードを追加しますか(1=YES, 2=NO):")
if int(add) == 1 :
    print(random.choice(cards))
else:
    break