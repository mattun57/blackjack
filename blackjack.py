# トランプのカードを用意する
# A-Kの13枚を4組
# ユーザーAがカードからランダムに2枚選択
# 敵がカードからランダムに2枚選択
# ユーザーAか敵どちらが勝ったか判定
# J-Kが10、Aは1または11として、2枚の数字の合計が多い方が勝ち
# ユーザーは手札を何回でも引ける
# ディーラーの手札は最後にわかる
# 21ちょうどで買った場合は「BlackJack!を表示」

import random

# A = 11
J = 10
Q = 10
K = 10
cards = ["A",2,3,4,5,6,7,8,9,10,J,Q,K] * 4


def main():
    """
    メイン関数
    """
    you_hand1 = cards.pop(get_rand_index(cards))
    you_hand2 = cards.pop(get_rand_index(cards))
    print("あたなの手札" + str(you_hand1),str(you_hand2))

    dealer_hand1 = cards.pop(get_rand_index(cards))
    if dealer_hand1 == "A":
        dealer_hand1 = "11"
    dealer_hand2 = cards.pop(get_rand_index(cards))
    if dealer_hand2 == "A":
        dealer_hand2 = "11"

    # Aを1か11か選ぶ（1回目)
    if you_hand1 == "A":
        A_choice = input("Aの数字はどうしますか？ 1 or 11 :")
        if A_choice == "1":
            you_hand1 = "1"
        elif A_choice == "11":
            you_hand1 = "11"
    
    if you_hand2 == "A":
        A_choice = input("Aの数字はどうしますか？ 1 or 11 :")
        if A_choice == "1":
            you_hand2 = "1"
        elif A_choice == "11":
            you_hand2 = "11"

    you_add = 0
    add = input("カードを追加しますか 1=YES, 2=NO: ")
    if int(add) == 1 :
        you_add = random.choice(cards)
        print("追加されたカード" + str(you_add))

    # Aを1か11か選ぶ（2回目)
    if you_add == "A":
        A_choice = input("Aの数字はどうしますか？ 1 or 11 :")
        if A_choice == "1":
            you_add = "1"
        elif A_choice == "11":
            you_add = "11"

    print("ディーラーの手札" + str(dealer_hand1),str(dealer_hand2))

    you_total = int(you_hand1) + int(you_hand2) + int(you_add)
    dealer_total = int(dealer_hand1) + int(dealer_hand2)

    if you_total > dealer_total:
        if you_total <= 21:
            if you_total == 21:
                print("Black Jack!")
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

def get_rand_index(cards):
    """
    cardsの配列からランダムにindex取得
    """
    return random.randint(0, len(cards) - 1)


# pythonコマンドで実行した時に最初に呼ばれる
if __name__ == '__main__':
    main()
