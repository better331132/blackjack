import random
cardtotal=[]
cardsort = ['S','C','H','D']
cardnum = [*'23456789FJQKA']
sort=len(cardsort)
num=len(cardnum)
class Card:
    deck=[]
    valuelist=[]
    def __init__(self):
        for i in range(sort):
            for k in range(num):
                cardtotal.append(cardsort[i]+cardnum[k])
                random.shuffle(cardtotal)    

    def cardpick(self):
        self.pick=cardtotal.pop()
        self.cards=self.deck.append(self.pick)    

    def cardpick2(self):
        self.pick2=cardtotal.pop()
        self.cards=self.deck.append(self.pick2)    


    def scoring(self):
        self.sum=0
        for i in range(len(self.deck)):  
            if 'A' in self.deck[i][1]:
                self.point = 11
                self.valuelist.append(self.point)

            elif self.deck[i][1] in ['J','Q','K','F']:
                self.point = 10
                self.valuelist.append(self.point)

            else:
                self.point = int(self.deck[i][1])
                self.valuelist.append(self.point)

            self.sum=self.sum+self.point
            
            
class Player(Card):
    deck=[]
    valuelist=[]
    def __init__(self):
        self.name="당신"

    def asking(self):
        self.cardpick()
        self.scoring()

class Dealer(Card):
    deck=[]
    valuelist=[]
    def __init__(self):    
        self.point=0
        self.name="딜러"
    
    def scoringwace(self):
        for i in range(len(self.deck)):
            if type(self.deck[i]) == int: 
                self.point=self.deck[i]
    
            elif 11 in self.deck[i][1]:
                self.point = 11

            elif self.deck[i][1] in ['J','Q','K','F']:
                self.point = 10

            else:
                self.point = int(self.deck[i][1])
            self.sum=self.sum+self.point

    def asking(self):
            while 11 not in self.valuelist and self.sum <21:
                if self.sum < 17:
                    self.cardpick()
                    self.scoringwace()  
                    print("아",self.deck)
                    if 11 in self.valuelist and self.sum > 21:
                        self.cardpick()
                        self.scoringwace()
                        self.sum=self.sum - self.deck.count(11)*10
                        print("사",self.deck)
                        print("사값",self.sum)
                        
                    elif 11 in self.valuelist and self.sum == 21:
                        print("여기서멈추자")
                        break

                else:
                    print("카",self.deck)
                    break
            
            while 11 in self.valuelist and self.sum != 21:
                if self.sum <= 16:
                    self.cardpick()
                    self.scoringwace()
                    print("쿠",self.deck)


                elif self.sum <21:
                    if 15 <= self.sum <=16:
                        self.cardpick()
                        self.scoringwace()
                        print("라",self.deck)    
                    
                    else:
                        print("다",self.deck)
                        break
                
                elif self.sum > 21:
                    if self.sum - self.valuelist.count(11)*10 > 21:
                        self.sum = self.sum - self.valuelist.count(11)*10
                        print("멈추자")
                        break
                    
                    else:
                        self.cardpick()
                        self.scoringwace    
                        print("마",self.deck)
                        
                elif self.sum == 21:    
                    print("끝끝끄튺ㅌ")
                    break

GameStart = input ("블랙잭 게임을 시작 합니다. 시작하시겠습니까? 아무키나누르세요 종료하기는 'q'버튼을 눌러주세요")

card=Card()
player=Player()
dealer=Dealer()
player.cardpick()
dealer.cardpick()
player.cardpick2()
dealer.cardpick2()



while True:
    if GameStart == 'q':
        exit()
    
    if player.sum < 21 and not 11 in player.valuelist:
        msg= input("딜러의 첫번째 카드는 {}입니다. {}의 현재카드는 {} 입니다. \n 카드를 더 받으시겠습니까?.그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(dealer.pick,player.name,player.deck))
        if msg == 'H':
            player.asking()
            if player.sum < 21 and player.sum > dealer.sum:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("이기셨네요")
                break
                GameStart
                
            
            elif player.sum == 21 and dealer.sum !=21:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("블랙잭입니다. 이기셨습니다.")
                break
                GameStart
                

            else:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("패배하셨습니다다다다다")
                break
                GameStart
                
        
        elif msg =='S':
            if player.sum < 21 and player.sum > dealer.sum:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("이기셨네요")
                break
                GameStart
                
            
            elif player.sum == 21 and dealer.sum !=21:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("블랙잭입니다. 이기셨습니다.")
                break
                GameStart

            else:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("패배하셨습니다다다다다")
                break
                GameStart

    elif 11 in player.valuelist:
        msg= input("딜러의 첫번째 카드는 {}입니다. {}의 현재카드는 {} 입니다. \n 카드를 더 받으시겠습니까?.그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(dealer.pick,player.name,player.deck))
        if msg == 'H':
            player.asking()
            if player.sum < 21 and player.sum > dealer.sum:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("이기셨네요")
                break
                GameStart
                
            
            elif player.sum == 21 and dealer.sum !=21:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("블랙잭입니다. 이기셨습니다.")
                break
                GameStart

            else:
                print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
                print("패배하셨습니다다다다다")
                break
                GameStart

        elif msg == 'S':
            if player.valuelist.count(11) >= 1:
                    qmsg=input("에이스가 {} 개 있네요. 무엇으로 하시겠습니까? '1' 또는 '11'을 차례대로 입력해주세요!\n 'AA'일 경우 '11,11' 혹은 '1,1 (콤마로구분)".format(player.valulist.count(11))
                    acechoice=qmsg.split(',')
                    for i in range(len[acechoice]):
                        choiceassign=[]
                        choiceassign=choiceassign.append(acechoice[i-1])
                        if '11' in choiceassign:
                            result=player.sum - 10*int(choiceassign.count('11'))
                        else:
                            result=player.sum

                    if player.sum < 21 and player.sum > dealer.sum:
                            print("이기셨네요")
                            GameStart
                    
                    elif player.sum == 21 and dealer.sum !=21:  
                            print("이기셨습니다.")
                            break
                            GameStart
                    else:
                        print("패배하셨습니다다다다다")
                        break
                        GameStart

    # if player.sum >21 and not 11 in player.valuelist:
    #     MSG1=print("딜러의 카드는 {} 이고 값은 {}입니다/n 당신의카드는 {}이고 값은 {}입니다".format(dealer.deck,dealer.sum,player.deck,player.sum))
    #     MSG2=print("패배하셨습니다")
            

