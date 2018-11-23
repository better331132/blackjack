# BlackJack
## Project 설명
BlackJack의 가장 기본적인 룰만을 반영하여 딜러와 플레이어가 1:1로 진행하는 게임에 관한 Python 코딩입니다.  
외부모듈의 사용이 없고 Python의 내장함수를 주로 사용하여 게임의 진행과정을 나타내었습니다.  
Python의 class, method의 정의, inheritance, instance와 for나 while을 활용한 반복구문의 **기초적 학습**에 도움이 될 것입니다.  
  
## Collaborators
#### 김영모, 배준홍
  
## 설치
#### Python 설치 :  
https://www.python.org/ 에 들어가서 download목록에 마우스를 올려놓으면 OS에 적합한 Version이 표시됩니다.  
클릭 후 다운로드 및 설치를 실행합니다.  
해당 파일은 git clone https://github.com/better331132/blackjack.git 을 실행하시면 download가 진행됩니다.  

## 실행방법
커맨드 창에서 파일을 내려받으신 폴더로 이동합니다.  
커맨드 창에 python portpolio_blackjack_KimBae_final.py 라고 입력하시거나  
파일명을 바꾸신 후에 커맨드 창에 python 바꾼파일명.py를 입력하시면 실행됩니다.

## 코드리뷰

### Line 1 
#### Line 1 :
~~~
import random  
~~~
random 모듈에 속한 shuffle 함수를 사용하기 위해 random모듈을 적용합니다.

### Line 3
#### Line 3 :
```
    card_flow = []
```
class Deck의 instance에서 카드를 한 장 뽑아올 때 카드를 잠시 맡겨 놓는 장소입니다.  
class Deck에서 추출된 카드가 잠깐 들르는 곳이라 흘러간다고 느껴져 card_flow라 명명하였습니다.  
어떤 class 의 instance들이라도 연결고리를 유지하기 위해 전역변수로 설정하였습니다.  

### Line 4 ~ 17
#### Line 4 ~ 11 :
```
    class Deck:
        def __init__(self):
            self.cards = []
            self.cardsort = ['Clover','Diamond','Heart','Spade']
            self.cardnum = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            for s in self.cardsort:
                for n in self.cardnum:
                    self.cards.append(s + n)
```
class Deck의 instance 생성과 동시에 실행되는 함수입니다.  
카드의 모양은 self.cardsort라는 list에, 카드의 번호는 self.cardnum이라는 list에 각각 할당합니다.  
s 값에 cardsort에서 하나의 element 들어올 때 n에 cardnum의 모든 element들이 s와 순차적으로 matching됩니다.  
s 값에 cardsort의 모든 element들이 할당될 때까지 위 과정을 반복합니다.  
이런 과정을 통해 카드의 모양과 번호를 조합하여 카드 한 세트를 self.cards에 채워넣습니다.  

#### Line 13 ~ 14 :
```
        def shuffle_cards(self):
            random.shuffle(self.cards)
```
random모듈의 shuffle함수를 이용해 정의한 class Deck의 method입니다.
이 method가 호출되면 self.cards의 elements의 순서가 무작위로 나열됩니다.  
또한 self.cards의 순서는 무작위 나열된 상태로 저장됩니다.

#### Line 16 ~ 17 :
```
        def pop_card(self):
            card_flow.append(self.cards.pop(0))
```
self.cards의 첫번째 element를 뽑아 Line 8의 'card_flow = [ ]'에 저장합니다.

### Line 20 ~ 56
#### Line 20 ~ 22 :
```
    class Person:
        def __init__(self):
            self.pocket =[]
```
class Dealer와 class Player가 상속 받을 상위 class입니다.  
class Dealer의 instance인 dealer와 class Player의 instance인 player가 모두 사람이므로 이 클래스를 Person이라 명명했습니다.  
instance인 dealer와 player가 생성될 때 각 플레이어의 카드보관함 역할을 할 self.pocket이 비어있는 list로 제공됩니다.

#### Line 24 ~ 25 :
```
        def dealt_card(self):
            self.pocket.append(card_flow.pop(0))
```
Line 21 ~ 22 과정을 통해 card_flow에 보관된 카드 한 장을 게임 참여자의 카드보관함으로 이동시킵니다.  
각각의 player에게 분배된 카드를 dealt card라 부르기에 이 method의 이름을 dealt_card라 명명했습니다.

#### Line 27 ~ 36 : 
```
        def value_assign(self):
            self.sum_t = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] in ['0', 'J', 'Q', 'K']:
                    card_value = 10
                elif self.pocket[i][-1] in 'A':
                    card_value = 11
                else:
                    card_value = int(self.pocket[i][-1])
                self.sum_t = self.sum_t + card_value
```
각각의 카드 보관함에 있는 카드를 점수로 변환하고 합산하여 도출한 임시점수입니다.  
Sum_t는 temporary sum의 의미이고 초기값을 0으로 주었습니다.  
카드 보관함 [i]번째 element의 마지막 글자를 기준으로 각각의 카드에 점수를 할당합니다.  
for구문에서 순차적으로 배출되는 카드 각각의 점수를 합산합니다.  

#### Line 38 ~ 47 :
```
        def howmanya(self):
            self.quant_a = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] == 'A':
                    exist_a = 1
                else:
                    exist_a = 0
                self.quant_a = self.quant_a + exist_a
            print("\n당신의 카드목록입니다.>> ",self.pocket)
            print("\n당신은 A를 {}개 보유하고 있습니다.".format(self.quant_a))
```
개인 카드 보관함의 Ace개수를 파악하고 카드 목록과 A의 개수를 표시해주는 method입니다.  
Ace의 수를 파악하는 method임에 착안해 how many a라 명명했습니다.
Ace의 수를 나타내는 attr는 quant_a로 명명하고 초기값은 역시 0으로 설정합니다.  
카드 보관함의 카드 수만큼 for구문 내부의 명령을 반복실행하여 Ace가 발견되면 1을, Ace가 발견되지 않으면 0을 주어 합산합니다.  
합산된 결과가 각각의 보관함에 있는 A의 수입니다.  
또한 카드현황과 목록에 포함된 Ace의 수를 합니다.

#### Line 49 ~ 55 :
```
        def trans_a(self):
            self.final_score = 0
            if self.quant_a == 0:
                self.final_score = self.sum_t #A 카드가 없다면 임시합이 현재 카드 목록의 최종합
            else:
                q = input("\n1점으로 간주할 A의 개수를 선택해주세요. {}개까지 가능합니다.(숫자로 입력) >> ".format(self.quant_a))
                self.final_score = self.sum_t - 10 * int(q)
```
발견된 Ace중 점수를 치환할 Ace의 개수를 선택하는 method입니다.  
trans_a 는 Ace의 값을 치환(transpose)한다는 의미를 생각하여 차용했습니다.
Ace의 점수를 하나로 특정하고나면 현재 카드현황의 최종 점수합을 도출해 낼 수 있습니다.  
Ace의 점수 치환과정까지 모두 마친 카드현황의 최종 점수합을 final_score라는 attr로 명명하였고 초기값을 0으로 할당합니다.  
Ace가 없다면 입력창은 나타나지 않고 임시합(sum_t)이 최종 점수합(final_score)이 됩니다.  
Ace가 1개 이상이라면 선택한 Ace의 개수에 따라 임시합이 조정되고 최종 점수합이 도출됩니다.

### Line 57 ~ 66
#### Line 57 ~ 66 :
```
    class Player(Person):
        def add_card(self):
            print("\n당신의 현재 점수는 {}점 입니다.\n".format(self.final_score))
            hos = input("카드를 더 받으시겠습니까?(y/n) >> ")
            self.det = 'hit'
            if hos == 'y':
                self.det = 'hit'
            else:
                self.det = 'stay'
            print("\n-----------------------------------------------------------")
```
class Person의 상속을 받는 하위 class입니다.  
따라서 class Person에 속한 method들을 class Player(Person)의 instance가 호출할 수 있습니다.  
카드 추가 여부를 입력값을 통해 결정하는 method를 추가합니다.  
이 method의 이름은 저것밖에 생각이 안났습니다.
한편 class Player의 상속을 받는 하위 class가 없기 때문에 이 method는 class Player의 instance만이 호출할 수 있습니다.  

### Line 68 ~ 93
#### Line 68 ~ 76 :
```
    class Dealer(Person):
        def howmanya(self):
            self.quant_a = 0
            for i in range(len(self.pocket)):
                if self.pocket[i][-1] == 'A':
                    exist_a = 1
                else:
                    exist_a = 0
                self.quant_a = self.quant_a + exist_a
          ~~print("\n당신의 카드목록입니다.>> ",self.pocket)~~
          ~~print("\n당신은 A를 {}개 보유하고 있습니다.".format(self.quant_a))~~
```
class Person의 상속을 받는 하위 class입니다.  
따라서 class Person에 속한 method들을 class Dealer(Person)의 instance가 호출할 수 있습니다.  
class Dealer(Person)의 howmanya method는 class Dealer(person)의 instance가 갖는 카드현황과 Ace 수를 보이지 않게 해야합니다.
Line 38 ~ 47중 Line 38 ~ 45까지는 동일하나 카드현황과 Ace의 개수를 출력하지 않아야 하므로 Line 46, 47는 삭제하였습니다.

#### Line 78 ~ 86 :
```
        def trans_a(self):
            self.final_score = 0
            if self.sum_t >= 17:
                while self.sum_t > 21 and self.quant_a >= 1:
                    self.quant_a = self.quant_a - 1
                    self.sum_t = self.sum_t - 10
                self.final_score = self.sum_t
            else :
                self.final_score = self.sum_t
```
class Person의 method와 이름과 목적은 같지만 구조는 상이합니다.  
class Dealer(Person)의 instance가 trans_a method를 호출하면 해당 method가 호출됩니다.  
최종 점수합(final_score)의 초기값에 0을 할당합니다.  
임시합(sum_t)이 17보다 클 때, 임시합(sum_t)이 21보다 크며 개인 카드 보관함에 Ace의 개수가 하나 이상이면 Ace의 점수를 11점에서 1점으로 치환하며 Ace의 개수를 한장씩 차감합니다.  
임시합이 21보다 작아지거나 Ace의 수가 0개가 되면 Ace의 점수를 치환할 이유가 없거나 치환 자체가 불가능해지므로 while loof를 빠져나오고 조정된 임시합을 최종 점수합에 할당하게 됩니다.  

#### Line 88 ~ 93 :
```
        def add_card(self):
            self.disc ='hit'
            if self.final_score < 17:
                self.disc = 'hit'
            else:
                self.disc = 'stay'
```
class Player의 method와 이름과 목적만 같습니다. 구조는 역시 상이합니다.
class Dealer의 instance의 카드 추가는 class Player의 intance와는 달리 따로 입력하는 값 없이 최종 점수합을 기준으로 결정됩니다.  
class Dealer의 instance가 카드 추가 여부를 판별하는데 쓰이는 attr의 이름은 수학에서의 판별식 discriminant에서 따왔습니다.  
disc의 초기값은 hit으로 주었고 class Dealer의 instance의 최종 점수합이 17보다 작으면 disc에 hit을 할당하고 17보다 크거나 같으면 stay를 할당합니다.  
stay는 Line 115 ~ 117에 영향을 미칩니다.  

### Line 95, 152 ~ 158
#### Line 95, 152 ~ 158
~~~
while True:  
~~~
```
reset = input("\n게임을 더 하시겠습니까?(y/n)>> ")  
if reset == 'y':  
  print("\n=======================================================")  
  continue  
if reset == 'n':  
  print("\n게임이 종료되었습니다.")  
  break  
```
한 차례의 게임이 끝나면 재시작 여부를 확인하는 코드입니다.  
input함수를 통해 입력된 값은 reset에 할당되고 if조건에 따라 게임이 재시작 되거나 종료문구 출력 후 게임이 종료됩니다.  
\n은 output의 위치를 강제로 한 칸 내려줍니다.

### Line 96 ~ 98
#### Line 96 ~ 98 :
```
    start = input("게임을 시작하시려면 아무 키나 입력해주세요.")
    if start == '':
        pass
```
준비가 되면 Enter키를 눌러 게임을 시작합니다.  
아무 키나 입력하라고 써놨지만 결국 Enter키를 입력해야 합니다.  
input함수에 입력한 값이 변수 start에 저장되고 저장된 값이 if조건을 충족하면 다음 코드를 진행합니다.  

### Line 100 ~ 107
#### Line 100 :
```
    deck = Deck()
``` 
class Deck의 instance인 deck을 생성합니다.  
생성과 동시에 카드를 52장 순서대로 생성하여 list 형태로 deck.cards에 보관합니다.  
또한 class Deck의 method를 호출할 수 있게 됩니다.  

#### Line 101 :
```
    deck.shuffle_cards()
```
deck.cards에 생성된 카드들(elements)의 순서를 무작위로 나열하는method를 호출합니다.  

#### Line 102 :
```
    dealer = Dealer()
```
dealer가 게임에 참여합니다. (class Dealer(Person)의 intance인 dealer가 생성됩니다.)  
카드 보관함인 dealer.pocket을 비어 있는 list의 형태로 지급받습니다.  

#### Line 103 :
```
    player = Player()
```
player가 게임에 참여합니다. (class Player(Person)의 instance인 player가 생성됩니다.)
카드 보관함인 player.pocket을 비어 있는 list의 형태로 지급받습니다.

#### Line 104 :
```
    deck.pop_card()
```
deck.cards에서 가장 앞에 위치한 카드를 1장 추출하여 card_flow에 담는 method를 호출합니다.
 
#### Line 105 :
```
    player.dealt_card()
```
card_flow에 담긴 한 장의 카드를 player.pocket으로 옮기는 method를 호출합니다.  

#### Line 106 :
```
    deck.pop_card()
```
Line 104 와 동일합니다.

#### Line 107 :
```
    dealer.dealt_card()
```
card_flow에 담긴 한 장의 카드를 dealer.pocket으로 옮기는 method를 호출합니다.  

### Line 109 ~ 117
#### Line 109, 115 ~ 117 :
```
    while True: 
```
```
        dealer.add_card()
        if dealer.disc == 'stay':    
            break
```
카드 추가 절차를 수차례 반복합니다.  
점수에 따라 카드를 추가할지 여부를 판단 후에 카드를 추가해야하면 Line 110으로 돌아가고 추가하지 않으면 while loof를 바로 빠져나옵니다.

#### Line 110 :
```
        deck.pop_card()
```
Line 104과 동일합니다.

#### Line 111 :
```
        player.dealt_card()
```
Line 107과 동일합니다.

#### Line 112 :
```
        dealer.value_assign()
```
현재 dealer가 보유한 카드들 각각에 점수를 할당한 후 임시합을 계산하는 method를 호출합니다.

#### Line 113 :
```
        dealer.howmanya()
```
dealer가 가진 Ace 수를 파악하는 method를 호출합니다.  

#### Line 114 :
```
        dealer.trans_a()
```
dealer의 임시합을 기준으로 Ace 점수를 치환할 수 있는 method를 호출합니다.

### Line 119 ~ 129
#### Line 119, 125 ~ 129 :
```
    while True:
```
```
        if player.final_score > 21:
            break
        player.add_card()
        if player.disc == 'stay':
            break
```
카드 추가 절차를 수차례 반복합니다.  
while loof 반복 중에 Ace의 점수 치환을 마친 최종 점수가 21보다 클 경우 while loof를 즉시 빠져나옵니다.  
while loof에서 강제로 이탈하지 않은 경우에만 카드 추가 여부를 결정합니다.

#### Line 120 :
```
        deck.pop_card()
```
Line 104와 동일합니다.

#### Line 121 :
```
        player.dealt_card()
```
Line 105와 동일합니다.

#### Line 122 :
```
        player.value_assign()
```
Line 112와 동일합니다.

#### Line 123 :
```
        player.howmanya()
```
player가 가진 Ace 수를 파악하고 카드현황과 Ace 수를 표시하는 method를 호출합니다.

#### Line 124 :
```
        player.trans_a()
```
player가 가진 Ace의 점수를 Ace 수 이내에서 선택하여 입력하여 치환할 수 있는 method를 호출합니다.

### Line 131 ~ 138
#### Line 131 ~ 138 :
```
    print("Player ♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠")
    print("당신의 카드목록입니다.>> ",player.pocket)
    print("\n당신의 최종 점수는 {}점 입니다.".format(player.final_score))
    print("♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n")
    print("Dealer ♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤")
    print("딜러의 카드목록입니다.>> ",dealer.pocket)
    print("\n딜러의 최종 점수는 {}점 입니다.".format(dealer.final_score))
    print("♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤♤\n")
```
게임 참여자 각각의 카드 현황과 최종 점수합을 출력합니다.

### Line 140 ~ 150
#### Line 140 ~ 150 :
```
    if player.final_score > 21:
        print("21점을 초과하였습니다.\n\n당신은 패배하셨습니다.")
    elif player.final_score <= 21 and dealer.final_score > 21 :
        print("딜러의 점수가 21점을 초과하였습니다.\n\n당신은 승리하셨습니다.")
    else:
        if player.final_score > dealer.final_score:                                 
            print("당신의 점수가 딜러의 점수보다 높습니다.\n\n당신은 승리하셨습니다.")   
        elif player.final_score == dealer.final_score:                              
            print("당신의 점수가 딜러의 점수와 같습니다.\n\n무승부입니다.") 
        else :                                                                      
            print("당신의 점수가 딜러의 점수보다 낮습니다.\n\n당신은 패배하셨습니다.")
```
각 경우의 승패를 판정합니다.
player가 21을 초과할 경우 dealer의 점수와 상관 없이 player는 패배합니다.  
dealer만 21점을 초과한 경우에 player는 승리합니다.  
player와 dealer의 점수가 모두 21 이하인 경우에 한해서 점수를 비교합니다.  
player와 dealer의 점수가 같을 때는 무승부로 처리합니다.  
비교하여 더 높은 점수를 가진 쪽이 승리합니다.
