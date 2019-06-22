# トランプのカードを用意する
# A-Kの13枚を4組
# ユーザーAがカードからランダムに2枚選択
# 敵がカードからランダムに2枚選択
# ユーザーAか敵どちらが勝ったか判定
# J-Kが10、Aは1または11として、2枚の数字の合計が多い方が勝ち
# ユーザーは手札を何回でも引ける
# ディーラーの手札は最後にわかる
# 21ちょうどで勝った場合は「BlackJack!を表示」
# Aが1か11かは、最後の点数計算の時に適切なものを自動的に計算する

import random

J = 10
Q = 10
K = 10
cards = ["A",2,3,4,5,6,7,8,9,10,J,Q,K] * 4

# ユーザーの手札まとめ
you_hands = []

# ディーラーの手札まとめ
dealer_hands = []


def main():
    """
    メイン関数
    """
    you_bet = input("いくら賭けますか？ 金額を入力してください:")
    print("あなたの賭けた金額 $" + you_bet)

    you_hands.append(cards.pop(get_rand_index(cards)))
    you_hands.append(cards.pop(get_rand_index(cards)))
    print("あたなの手札" + str(you_hands))


    # ディーラーは自分の手持ちのカードの合計が「17」以上になるまでヒットし続ける。
    dealer_total = 0
    while dealer_total <= 17:
        dealer_hands.append(cards.pop(get_rand_index(cards)))
        if "A" in dealer_hands:
           dealer_hands.remove("A")
           dealer_hands.append(11)
        dealer_total = sum(dealer_hands)


    # ユーザーは手札を見ながら何度でもヒットできる
    add = "1"
    while add == "1":
        add = input("カードを追加しますか？ 1-HIT, 2-STAND :")
        if add == "1":
            you_hands.append(cards.pop(get_rand_index(cards)))
        print(you_hands)


    print("ディーラーの手札" + str(dealer_hands))

    # Aが1か11か適切なものを自動的に計算
      # 文字列"A"を取り除く
    if "A" in you_hands:
        A_num = you_hands.count("A")
        for i in range(int(A_num)):
            you_hands.remove("A")
        # 文字列"A"の数分 1 か 11 を追加する
        for j in range(int(A_num)):
            if sum(you_hands) >= 11:
                you_hands.append(1)
            else:
                you_hands.append(11)


    # ディーラーとユーザーの手札の合計
    you_total = sum(you_hands)
    dealer_total = sum(dealer_hands)

    # 勝敗の判定と出力
    if you_total > dealer_total:
        if you_total <= 21:
            if you_total == 21:
                print("Black Jack!")
                bet = int(you_bet) * 2
                print("$" + str(bet) + " GET!")
            print("YOU WIN!")
            bet = int(you_bet) * 2
            print("$" + str(bet) + " GET!")


        else:
            print("YOU LOSE!")
    elif you_total == dealer_total:
        print("DRAW")
        print("払い戻し金 $" + you_bet)
    else:
        if dealer_total <= 21:
            print("YOU LOSE!")
        else:
            print("YOU WIN!")
            bet = int(you_bet) * 2
            print("$" + str(bet) + " GET!")

def get_rand_index(cards):
    """
    cardsの配列からランダムにindex取得
    """
    return random.randint(0, len(cards) - 1)


# pythonコマンドで実行した時に最初に呼ばれる
if __name__ == '__main__':
    main()
