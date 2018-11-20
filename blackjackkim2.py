import random


cardsort = ['S','C','H','D']
cardnum = [*'23456789FJQKA']
sort=len(cardsort)
num=len(cardnum)
cardtotal=[]
class Card:
    def __init__(self):
       for i in range(sort):
            for k in range(num):
                cardtotal.append(cardsort[i]+cardnum[k])
                random.shuffle(cardtotal)    

    def cardpick(self):
        self.pick=cardtotal.pop()
        self.cards=self.deck.append(self.pick)    

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
         while 'A' not in self.deck:
            msg=input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(self.sum))
            if msg == 'H':
                self.cardpick()
                self.scoring()
                continue

            elif msg == 'S': 
                
                if self.sum < 21 and self.result > dealer.sum:
                    break

                elif self.result == 21 and dealer.sum !=21:
                    break

                elif self.result > 21:
                    break
                
                else:
                    continue
        
    def askingwoace(self):
        while 'A' in self.deck:
            msg= input("카드를 더 받으시겠습니까? 현재값은 {} 입니다.\n 그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(player.sum))
            if msg == 'H':
                self.cardpick()
                self.scoring()

            elif msg == 'S':
                if self.deck.count(11)>2:
                    question=input("에이스가 {} 개 있네요. 무엇으로 하시겠습니까? '1' 또는 '11'을 차례대로 입력해주세요!\n 'AA'일 경우 '11,11' 혹은 '1,1 (콤마로구분)".format(self.deck.count(11)))
                    acechoice=question.split(',')
                    for i in range(len[acechoice]):
                        choiceassign=[]
                        choiceassign=choiceassign.append(acechoice[i-1])
                        if '11' in choiceassign:
                            p_result=self.sum - 10*int(choiceassign.count('11'))
                        else:
                            p_result=self.sum
                else:
                    p_result=self.sum


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
    
            elif 'A' in self.deck[i][1]:
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


card=Card()
player=Player()
dealer=Dealer()
player.cardpick()
dealer.cardpick()
player.cardpick()
dealer.cardpick()
player.scoring()
dealer.scoring()
# player.asking()
dealer.asking()

# while True:
#     if player.sum >21 and not 11 in dealer.valuelist:
#         print("패배하셨습니다")

#     elif player.sum < 21 and not 11 in dealer.valuelist:
#         msg= input("딜러의 첫번째 카드는 {}입니다. {}의 현재카드는 {} 입니다. \n 카드를 더 받으시겠습니까?.그만받기는 'S' 받으시려면 'H' 를 눌러주세요".format(dealer.sum[0],player.name,player.deck))
#         if msg == 'H'


print(dealer.valuelist)
print(dealer.deck)
print(dealer.sum)