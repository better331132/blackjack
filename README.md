# BlackJack
## Project 설명
BlackJack 게임의 가장 기본적인 룰만을 반영하여 딜러와 플레이어가 1:1로 진행하는 게임에 관한 Python 코딩입니다.  
외부모듈의 사용이 없고 Python의 내장함수를 주로 사용하여 게임의 진행과정을 나타내었습니다.  
Python의 함수정의, class, inheritance, for나 while을 활용한 반복구문의 **기초적 학습**에 도움이 될 것입니다.  
  
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

#### Line 1 :  
~~~
import random  
~~~
random 모듈에 속한 shuffle 함수를 사용하기 위해 random모듈을 적용합니다.

#### Line 3, Line 152 ~ 158 :  
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

### Line 4 ~ 6 :
```
    start = input("게임을 시작하시려면 아무 키나 입력해주세요.")
    if start == '':
        pass
```
준비가 되면 Enter키를 눌러 게임을 시작합니다.  
input함수에 입력한 값이 변수 start에 저장되고  
저장된 값이 if조건을 충족하면 다음 코드를 진행합니다.

### Line 8 :
```
    card_flow = []
```
class Deck의 instance에서 카드를 한 장 뽑아올 때 카드를 잠시 맡겨 놓는 장소입니다.  

### Line 9 ~ 22 :
#### Line 9 ~ 16 :
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
카드의 모양과 번호를 조합하여 카드 한 세트를 self.cards에 채워넣습니다.  

#### Line 18 ~ 19 :
```
        def shuffle_cards(self):
            random.shuffle(self.cards)
```
self.cards에 순서대로 생성된 카드를 random모듈의 shuffle함수를 통해 self.cards의 elements의 순서를 무작위로 나열합니다.  
함수가 호출된 이후에 self.cards의 순서는 무작위 나열된 상태로 저장됩니다.

#### Line 21 ~ 22 :
```
        def pop_card(self):
            card_flow.append(self.cards.pop(0))
```
self.cards의 첫번째 element를 뽑아 Line 8의 'card_flow = []'에 저장합니다.

### Line 25 ~ 61 :
#### Line 25 ~ 27 :
```
    class Person:
        def __init__(self):
            self.pocket =[]
```
class Dealer와 class Player가 상속 받을 상위 class입니다.  
Dealer의 instance인 dealer와 Player의 instance인 player 모두 사람이므로 이 클래스를 Person이라 명명했습니다.  
instance인 dealer와 player가 생성될 때 각 플레이어의 카드보관함 역할을 할 self.pocket이 비어있는 list로 제공됩니다.

#### Line 29 ~ 30 :
```
        def dealt_card(self):
            self.pocket.append(card_flow.pop(0))
```
Line 21 ~ 22 과정을 통해 card_flow에 보관된 카드 한 장을 게임 참여자의 카드보관함으로 이동시킵니다.

#### Line 32 ~ 41 : 
