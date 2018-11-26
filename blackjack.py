from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
import random

run = 0
yourscore = 0
dealerscore = 0

class cardback(Sprite):
    cardback = ImageAsset("gray_back.png")
    def __init__(self,  position):
        super().__init__(cardback.cardback, position)


#hearts

class H2(Sprite):
    H2 = ImageAsset("2H.png")
    def __init__(self,  position):
        super().__init__(H2.H2, position)
class H3(Sprite):
    H3 = ImageAsset("3H.png")
    def __init__(self,  position):
        super().__init__(H3.H3, position)
class H4(Sprite):
    H4 = ImageAsset("4H.png")
    def __init__(self,  position):
        super().__init__(H4.H4, position)
class H5(Sprite):
    H5 = ImageAsset("5H.png")
    def __init__(self,  position):
        super().__init__(H5.H5, position)
class H6(Sprite):
    H6 = ImageAsset("6H.png")
    def __init__(self,  position):
        super().__init__(H6.H6, position)
class H7(Sprite):
    H7 = ImageAsset("7H.png")
    def __init__(self,  position):
        super().__init__(H7.H7, position)
class H8(Sprite):
    H8 = ImageAsset("8H.png")
    def __init__(self,  position):
        super().__init__(H8.H8, position)
class H9(Sprite):
    H9 = ImageAsset("9H.png")
    def __init__(self,  position):
        super().__init__(H9.H9, position)
class H10(Sprite):
    H10 = ImageAsset("10H.png")
    def __init__(self,  position):
        super().__init__(H10.H10, position)
class JH(Sprite):
    JH = ImageAsset("JH.png")
    def __init__(self,  position):
        super().__init__(JH.JH, position)
class QH(Sprite):
    QH = ImageAsset("QH.png")
    def __init__(self,  position):
        super().__init__(QH.QH, position)
class KH(Sprite):
    KH = ImageAsset("KH.png")
    def __init__(self,  position):
        super().__init__(KH.KH, position)
class AH(Sprite):
    AH = ImageAsset("AH.png")
    def __init__(self,  position):
        super().__init__(AH.AH, position)


#diamonds
class D2(Sprite):
    D2 = ImageAsset("2D.png")
    def __init__(self,  position):
        super().__init__(D2.D2, position)
class D3(Sprite):
    D3 = ImageAsset("3D.png")
    def __init__(self,  position):
        super().__init__(D3.D3, position)
class D4(Sprite):
    D4 = ImageAsset("4D.png")
    def __init__(self,  position):
        super().__init__(D4.D4, position)
class D5(Sprite):
    D5 = ImageAsset("5D.png")
    def __init__(self,  position):
        super().__init__(D5.D5, position)
class D6(Sprite):
    D6 = ImageAsset("6D.png")
    def __init__(self,  position):
        super().__init__(D6.D6, position)
class D7(Sprite):
    D7 = ImageAsset("7D.png")
    def __init__(self,  position):
        super().__init__(D7.D7, position)
class D8(Sprite):
    D8 = ImageAsset("8D.png")
    def __init__(self,  position):
        super().__init__(D8.D8, position)
class D9(Sprite):
    D9 = ImageAsset("9D.png")
    def __init__(self,  position):
        super().__init__(D9.D9, position)
class D10(Sprite):
    D10 = ImageAsset("10D.png")
    def __init__(self,  position):
        super().__init__(D10.D10, position)
class JD(Sprite):
    JD = ImageAsset("JD.png")
    def __init__(self,  position):
        super().__init__(JD.JD, position)
class QD(Sprite):
    QD = ImageAsset("QD.png")
    def __init__(self,  position):
        super().__init__(QD.QD, position)
class KD(Sprite):
    KD = ImageAsset("KD.png")
    def __init__(self,  position):
        super().__init__(KD.KD, position)
class AD(Sprite):
    AD = ImageAsset("AD.png")
    def __init__(self,  position):
        super().__init__(AD.AD, position)


#spades
class S2(Sprite):
    S2 = ImageAsset("2S.png")
    def __init__(self,  position):
        super().__init__(S2.S2, position)
class S3(Sprite):
    S3 = ImageAsset("3S.png")
    def __init__(self,  position):
        super().__init__(S3.S3, position)
class S4(Sprite):
    S4 = ImageAsset("4S.png")
    def __init__(self,  position):
        super().__init__(S4.S4, position)
class S5(Sprite):
    S5 = ImageAsset("5S.png")
    def __init__(self,  position):
        super().__init__(S5.S5, position)
class S6(Sprite):
    S6 = ImageAsset("6S.png")
    def __init__(self,  position):
        super().__init__(S6.S6, position)
class S7(Sprite):
    S7 = ImageAsset("7S.png")
    def __init__(self,  position):
        super().__init__(S7.S7, position)
class S8(Sprite):
    S8 = ImageAsset("8S.png")
    def __init__(self,  position):
        super().__init__(S8.S8, position)
class S9(Sprite):
    S9 = ImageAsset("9S.png")
    def __init__(self,  position):
        super().__init__(S9.S9, position)
class S10(Sprite):
    S10 = ImageAsset("10S.png")
    def __init__(self,  position):
        super().__init__(S10.S10, position)
class JS(Sprite):
    JS = ImageAsset("JS.png")
    def __init__(self,  position):
        super().__init__(JS.JS, position)
class QS(Sprite):
    QS = ImageAsset("QS.png")
    def __init__(self,  position):
        super().__init__(QS.QS, position)
class KS(Sprite):
    KS = ImageAsset("KS.png")
    def __init__(self,  position):
        super().__init__(KS.KS, position)
class AS(Sprite):
    AS = ImageAsset("AS.png")
    def __init__(self,  position):
        super().__init__(AS.AS, position)


#clubs
class C2(Sprite):
    C2 = ImageAsset("2C.png")
    def __init__(self,  position):
        super().__init__(C2.C2, position)
class C3(Sprite):
    C3 = ImageAsset("3C.png")
    def __init__(self,  position):
        super().__init__(C3.C3, position)
class C4(Sprite):
    C4 = ImageAsset("4C.png")
    def __init__(self,  position):
        super().__init__(C4.C4, position)
class C5(Sprite):
    C5 = ImageAsset("5C.png")
    def __init__(self,  position):
        super().__init__(C5.C5, position)
class C6(Sprite):
    C6 = ImageAsset("2C.png")
    def __init__(self,  position):
        super().__init__(C6.C6, position)
class C7(Sprite):
    C7 = ImageAsset("7C.png")
    def __init__(self,  position):
        super().__init__(C7.C7, position)
class C8(Sprite):
    C8 = ImageAsset("8C.png")
    def __init__(self,  position):
        super().__init__(C8.C8, position)
class C9(Sprite):
    C9 = ImageAsset("9C.png")
    def __init__(self,  position):
        super().__init__(C9.C9, position)
class C10(Sprite):
    C10 = ImageAsset("10C.png")
    def __init__(self,  position):
        super().__init__(C10.C10, position)
class JC(Sprite):
    JC = ImageAsset("JC.png")
    def __init__(self,  position):
        super().__init__(JC.JC, position)
class QC(Sprite):
    QC = ImageAsset("QC.png")
    def __init__(self,  position):
        super().__init__(QC.QC, position)
class KC(Sprite):
    KC = ImageAsset("KC.png")
    def __init__(self,  position):
        super().__init__(KC.KC, position)
class AC(Sprite):
    AC = ImageAsset("AC.png")
    def __init__(self,  position):
        super().__init__(AC.AC, position)

money = input("How much money would you like to start with?")


showing = []

t = 3

print("press space to begin")
print("Press r for the rules")

def rules(event):
    print("The game has mostly standard rules of blackjack. You may not split. You may not surrender.")
def pauseplay(event):
    global q, dealerscore, yourscore, r, a, b, cards, money, o, p, yb, db, bet, ace, t, showing, n
    if t == 3:
        t = 2
        m = 2
        for p in showing:
            p.visible = False
        yourscore = 0
        n = 2
        bet = input("What is your bet?")
        yb = 0
        db = 0
        ace = 0
        #set up deck
        cards = [H2, H3, H4, H5, H6, H7, H8, H9, H10, JH, QH, KH, AH, D2, D3, D4, D5, D6, D7, D8, D9, D10, JD, QD, KD, AD, S2, S3, S4, S5, S6, S7, S8, S9, S10, JS, QS, KS, AS, C2, C3, C4, C5, C6, C7, C8, C9, C10, JC, QC, KC, AC]
        #reset visible stuff
        random.shuffle(cards)

        #starting cards
        e = cardback((150, 25))
        e.scale = .1
        yourscore = 0
        dealerscore = 0
        s = cards[0]
        a = s((50,150))
        a.scale = 0.1
        
        cards.pop(0)
        
        b = cards[0]
        c = b((150,150))
        c.scale = 0.1
        
        cards.pop(0)
        
        q = cards[0]
        w = q((50,25))
        w.scale = .1
        
        cards.pop(0)
        r = cards[0]
        cards.pop(0)
        
        r = cards[0]
        cards.pop(0)
        print("Press H to hit or S to stay")
        
        if q == H2:
            dealerscore += 2
        elif q == S2:
            dealerscore += 2
        elif q == D2:
            dealerscore += 2
        elif q == C2:
            dealerscore += 2
        elif q == H3:
            dealerscore += 3
        elif q == S3:
            dealerscore += 3
        elif q == D3:
            dealerscore += 3
        elif q == C3:
            dealerscore += 3
        elif q == H4:
            dealerscore += 4
        elif q == S4:
            dealerscore += 4
        elif q == D4:
            dealerscore += 4
        elif q == C4:
            dealerscore += 4
        elif q == H5:
            dealerscore += 5
        elif q == C5:
            dealerscore += 5
        elif q == D5:
            dealerscore += 5
        elif q == S5:
            dealerscore += 5
        elif q == H6:
            dealerscore += 6
        elif q == S6:
            dealerscore += 6
        elif q == D6:
            dealerscore += 6
        elif q == C6:
            dealerscore += 6
        elif q == H7:
            dealerscore += 7
        elif q == C7:
            dealerscore += 7
        elif q == S7:
            dealerscore += 7
        elif q == D7:
            dealerscore += 7
        elif q == D8:
            dealerscore += 8
        elif q == C8:
            dealerscore += 8
        elif q == S8:
            dealerscore += 8
        elif q == H8:
            dealerscore += 8
        elif q == D9:
            dealerscore += 9
        elif q == H9:
            dealerscore += 9
        elif q == S9:
            dealerscore += 9
        elif q == C9:
            dealerscore += 9
        elif q == AH:
            dealerscore += 1
        elif q == AS:
            dealerscore += 1
        elif q == AC:
            dealerscore += 1
        elif q == AD:
            dealerscore += 1
        else:
            dealerscore += 10
        
        if r == H2:
            dealerscore += 2
        elif r == S2:
            dealerscore += 2
        elif r == D2:
            dealerscore += 2
        elif r == C2:
            dealerscore += 2
        elif r == H3:
            dealerscore += 3
        elif r == S3:
            dealerscore += 3
        elif r == D3:
            dealerscore += 3
        elif r == C3:
            dealerscore += 3
        elif r == H4:
            dealerscore += 4
        elif r == S4:
            dealerscore += 4
        elif r == D4:
            dealerscore += 4
        elif r == C4:
            dealerscore += 4
        elif r == H5:
            dealerscore += 5
        elif r == C5:
            dealerscore += 5
        elif r == D5:
            dealerscore += 5
        elif r == S5:
            dealerscore += 5
        elif r == H6:
            dealerscore += 6
        elif r == S6:
            dealerscore += 6
        elif r == D6:
            dealerscore += 6
        elif r == C6:
            dealerscore += 6
        elif r == H7:
            dealerscore += 7
        elif r == C7:
            dealerscore += 7
        elif r == S7:
            dealerscore += 7
        elif r == D7:
            dealerscore += 7
        elif r == D8:
            dealerscore += 8
        elif r == C8:
            dealerscore += 8
        elif r == S8:
            dealerscore += 8
        elif r == H8:
            dealerscore += 8
        elif r == D9:
            dealerscore += 9
        elif r == H9:
            dealerscore += 9
        elif r == S9:
            dealerscore += 9
        elif r == C9:
            dealerscore += 9
        elif r == AH:
            dealerscore += 1
        elif r == AS:
            dealerscore += 1
        elif r == AC:
            dealerscore += 1
        elif r == AD:
            dealerscore += 1
        else:
            dealerscore += 10
        #check for dealer blackjack
        if q == H10 or q == JH or q == QH or q == KH or q == D10 or q == JD or q == QD or q == KD or q == S10 or q == JS or q == QS or q == KS or q == C10 or q == JC or q == QC or q == KC:
            if r == AH or r == AD or r == AS or r == AC:
                if s == H10 or s == JH or s == QH or s == KH or s == D10 or s == JD or s == QD or s == KD or s == S10 or s == JS or s == QS or s == KS or s == C10 or s == JC or s == QC or s == KC:
                    if b == AH or b == AD or b == AS or b == AC:
                        print("You both have blackjack")
                
                elif b == H10 or b == JH or b == QH or b == KH or b == D10 or b == JD or b == QD or b == KD or b == S10 or b == JS or b == QS or b == KS or b == C10 or b == JC or b == QC or b == KC:
                    if s == AH or s == AD or s == AS or s == AC:
                        print("You both blackjack")
                else:
                    print("Dealer has blackjack")
                    t = 3
                    j = r((150,25))
                    j.scale = .1
                    db = 5
                    money = int(money) - int(bet)
                    print("You have $" + str(money))
                cards.pop(0)
        
        if r == H10 or r == JH or r == QH or r == KH or r == D10 or r == JD or r == QD or r == KD or r == S10 or r == JS or r == QS or r == KS or r == C10 or r == JC or r == QC or r == KC:
            if q == AH or q == AD or q == AS or q == AC:
                if s == H10 or s == JH or s == QH or s == KH or s == D10 or s == JD or s == QD or s == KD or s == S10 or s == JS or s == QS or s == KS or s == C10 or s == JC or s == QC or s == KC:
                    if b == AH or b == AD or b == AS or b == AC:
                        print("You both have blackjack")
                
                elif b == H10 or b == JH or b == QH or b == KH or b == D10 or b == JD or b == QD or b == KD or b == S10 or b == JS or b == QS or b == KS or b == C10 or b == JC or b == QC or b == KC:
                    if s == AH or s == AD or s == AS or s == AC:
                        print("You both blackjack")
                else:
                    print("Dealer has blackjack")
                    t = 3
                    money = int(money) - int(bet)
                    print("You have $" + str(money))
                    j = r((150,25))
                    j.scale = .1
                    db = 5
                cards.pop(0)
        
        
        
        #check if player blackjack(todo)
        if s == H10 or s == JH or s == QH or s == KH or s == D10 or s == JD or s == QD or s == KD or s == S10 or s == JS or s == QS or s == KS or s == C10 or s == JC or s == QC or s == KC:
            if b == AH or b == AD or b == AS or b == AC:
                print("You have blackjack")
                j = r((150,25))
                j.scale = .1
                db = 5
                money = int(money) + 1.5*int(bet)
                print("You have $" + str(money))
                t = 3
            cards.pop(0)
            
        
        if b == H10 or b == JH or b == QH or b == KH or b == D10 or b == JD or b == QD or b == KD or b == S10 or b == JS or b == QS or b == KS or b == C10 or b == JC or b == QC or b == KC:
            if s == AH or s == AD or s == AS or s == AC:
                print("You have blackjack")
                j = r((150,25))
                j.scale = .1
                money = int(money) + 1.5*int(bet)
                print("You have $" + str(money))
                t = 3
            cards.pop(0)
        #getting the starting score
        if s == H2:
            yourscore += 2
            
        elif s == S2:
            yourscore += 2
            
        elif s == D2:
            yourscore += 2
            
        elif s == C2:
            yourscore += 2
            
        elif s == H3:
            yourscore += 3
            
        elif s == S3:
            yourscore += 3
            
        elif s == D3:
            yourscore += 3
            
        elif s == C3:
            yourscore += 3
            
        elif s == H4:
            yourscore += 4
            
        elif s == S4:
            yourscore += 4
            
        elif s == D4:
            yourscore += 4
            
        elif s == C4:
            yourscore += 4
            
        elif s == H5:
            yourscore += 5
            
        elif s == C5:
            yourscore += 5
            
        elif s == D5:
            yourscore += 5
            
        elif s == S5:
            yourscore += 5
            
        elif s == H6:
            yourscore += 6
            
        elif s == S6:
            yourscore += 6
            
        elif s == D6:
            yourscore += 6
            
        elif s == C6:
            yourscore += 6
            
        elif s == H7:
            yourscore += 7
            
        elif s == C7:
            yourscore += 7
            
        elif s == S7:
            yourscore += 7
            
        elif s == D7:
            yourscore += 7
            
        elif s == D8:
            yourscore += 8
            
        elif s == C8:
            yourscore += 8
            
        elif s == S8:
            yourscore += 8
            
        elif s == H8:
            yourscore += 8
            
        elif s == D9:
            yourscore += 9
            
        elif s == H9:
            yourscore += 9
            
        elif s == S9:
            yourscore += 9
            
        elif s == C9:
            yourscore += 9
            
        elif s == AH:
            yourscore += 1
            ace = 1
            
        elif s == AS:
            yourscore += 1
            ace = 1
            
        elif s == AC:
            yourscore += 1
            
            ace = 1
        elif s == AD:
            yourscore += 1
            
            ace = 1
        else:
            yourscore += 10
            
        
        if b == H2:
            yourscore += 2
            
        elif b == S2:
            yourscore += 2
            
        elif b == D2:
            yourscore += 2
            
        elif b == C2:
            yourscore += 2
            
        elif b == H3:
            yourscore += 3
            
        elif b == S3:
            yourscore += 3
            
        elif b == D3:
            yourscore += 3
            
        elif b == C3:
            yourscore += 3
            
        elif b == H4:
            yourscore += 4
            
        elif b == S4:
            yourscore += 4
            
        elif b == D4:
            yourscore += 4
            
        elif b == C4:
            yourscore += 4
            
        elif b == H5:
            yourscore += 5
            
        elif b == C5:
            yourscore += 5
            
        elif b == D5:
            yourscore += 5
            
        elif b == S5:
            yourscore += 5
            
        elif b == H6:
            yourscore += 6
            
        elif b == S6:
            yourscore += 6
            
        elif b == D6:
            yourscore += 6
            
        elif b == C6:
            yourscore += 6
            
        elif b == H7:
            yourscore += 7
            
        elif b == C7:
            yourscore += 7
            
        elif b == S7:
            yourscore += 7
            
        elif b == D7:
            yourscore += 7
            
        elif b == D8:
            yourscore += 8
            
        elif b == C8:
            yourscore += 8
            
        elif b == S8:
            yourscore += 8
            
        elif b == H8:
            yourscore += 8
            
        elif b == D9:
            yourscore += 9
            
        elif b == H9:
            yourscore += 9
            
        elif b == S9:
            yourscore += 9
            
        elif b == C9:
            yourscore += 9
            
        elif b == AH:
            yourscore += 1
            
            ace = 1
        elif b == AS:
            yourscore += 1
            
            ace = 1
        elif b == AC:
            yourscore += 1
            
            ace = 1
        elif b == AD:
            yourscore += 1
            
            ace = 1
        else:
            yourscore += 10
            

def step():
    global t
    while t == 19:
        t = 3
n = 2
m = 2
db = 0
yb = 0

#what to do when staying
def stay(event):
    global t, r, n, ace, dealerscore, cards, m, yourscore, db, yb, money, bet, showing, p
    if t != 3:
        t = 3
        print("You stayed")
        j = r((150,25))
        j.scale = .1
    #    while dealerscore < 17:
    
        if ace == 1 and yourscore + 10 < 22:
            yourscore = yourscore + 10
            print("yourscore: " + str(yourscore))
        else:
            print("yourscore: " + str(yourscore))
        while dealerscore < 17:
            o = cards[0]
            p = o((100*n+50,25))
            showing.append(p)
            p.scale = .1
            cards.pop(0)
            n = n + 1
            if o == H2:
                dealerscore += 2
                print(dealerscore)
            elif o == S2:
                dealerscore += 2
                print(dealerscore)
            elif o == D2:
                dealerscore += 2
                print(dealerscore)
            elif o == C2:
                dealerscore += 2
                print(dealerscore)
        
            elif o == H3:
                dealerscore += 3
                print(dealerscore)
            elif o == S3:
                dealerscore += 3
                print(dealerscore)
            elif o == D3:
                dealerscore += 3
                print(dealerscore)
            elif o == C3:
                dealerscore += 3
                print(dealerscore)
            elif o == H4:
                dealerscore += 4
                print(dealerscore)
            elif o == S4:
                dealerscore += 4
                print(dealerscore)
            elif o == D4:
                dealerscore += 4
                print(dealerscore)
            elif o == C4:
                dealerscore += 4
                print(dealerscore)
            elif o == H5:
                dealerscore += 5
                print(dealerscore)
            elif o == C5:
                dealerscore += 5
                print(dealerscore)
            elif o == D5:
                dealerscore += 5
                print(dealerscore)
            elif o == S5:
                dealerscore += 5
                print(dealerscore)
            elif o == H6:
                dealerscore += 6
                print(dealerscore)
            elif o == S6:
                dealerscore += 6
                print(dealerscore)
            elif o == D6:
                dealerscore += 6
                print(dealerscore)
            elif o == C6:
                dealerscore += 6
                print(dealerscore)
            elif o == H7:
                dealerscore += 7
                print(dealerscore)
            elif o == C7:
                dealerscore += 7
                print(dealerscore)
            elif o == S7:
                dealerscore += 7
                print(dealerscore)
            elif o == D7:
                dealerscore += 7
                print(dealerscore)
            elif o == D8:
                dealerscore += 8
                print(dealerscore)
            elif o == C8:
                dealerscore += 8
                print(dealerscore)
            elif o == S8:
                dealerscore += 8
                print(dealerscore)
            elif o == H8:
                dealerscore += 8
                print(dealerscore)
            elif o == D9:
                dealerscore += 9
                print(dealerscore)
            elif o == H9:
                dealerscore += 9
                print(dealerscore)
            elif o == S9:
                dealerscore += 9
                print(dealerscore)
            elif o == C9:
                dealerscore += 9
                print(dealerscore)
            elif o == AH:
                dealerscore += 1
                ace = 1
                print(dealerscore)
    
            elif o == AS:
                dealerscore += 1
                print(dealerscore)
    
            elif o == AC:
                dealerscore += 1
    
                print(dealerscore)
            elif o == AD:
                dealerscore += 1
                print(dealerscore)
    
            else:
                dealerscore += 10
                print(dealerscore)
            if dealerscore > 21:
                print("dealer busted")
                t = 3
                db = 5

        if yb == 5:
            print("You lose")
            money = int(money) - int(bet)
            print("You have $" + str(money))
        if db == 5:
            print("You win")
            money = int(money) + int(bet)
            print("You have $" + str(money))
        elif yourscore == dealerscore:
            print("Push")
            print("You have $" + str(money))
        elif yourscore < dealerscore:
            print("You lose")
            money = int(money) - int(bet)
            print("You have $" + str(money))
        else:
            print("You win")
            money = int(money) + int(bet)
            print("You have $" + str(money))



m = 2
def hit(event):
    global cards, y, m, yourscore, t, ace, o, p, yb, showing, money
    y = 150
    if t == 2:
        o = cards[0]
        p = o((100*m+50,y))
        p.scale = .1
        cards.pop(0)
        showing.append(p)
        m = m + 1
    if t == 2:
        if o == H2:
            yourscore += 2
            
        elif o == S2:
            yourscore += 2
            
        elif o == D2:
            yourscore += 2
            
        elif o == C2:
            yourscore += 2
            
    
        elif o == H3:
            yourscore += 3
            
        elif o == S3:
            yourscore += 3
            
        elif o == D3:
            yourscore += 3
            
        elif o == C3:
            yourscore += 3
            
        elif o == H4:
            yourscore += 4
            
        elif o == S4:
            yourscore += 4
            
        elif o == D4:
            yourscore += 4
            
        elif o == C4:
            yourscore += 4
            
        elif o == H5:
            yourscore += 5
            
        elif o == C5:
            yourscore += 5
            
        elif o == D5:
            yourscore += 5
            
        elif o == S5:
            yourscore += 5
            
        elif o == H6:
            yourscore += 6
            
        elif o == S6:
            yourscore += 6
            
        elif o == D6:
            yourscore += 6
            
        elif o == C6:
            yourscore += 6
            
        elif o == H7:
            yourscore += 7
            
        elif o == C7:
            yourscore += 7
            
        elif o == S7:
            yourscore += 7
            
        elif o == D7:
            yourscore += 7
            
        elif o == D8:
            yourscore += 8
            
        elif o == C8:
            yourscore += 8
            
        elif o == S8:
            yourscore += 8
            
        elif o == H8:
            yourscore += 8
            
        elif o == D9:
            yourscore += 9
            
        elif o == H9:
            yourscore += 9
            
        elif o == S9:
            yourscore += 9
            
        elif o == C9:
            yourscore += 9
            
        elif o == AH:
            yourscore += 1
            ace = 1
        elif o == AS:
            yourscore += 1
            ace = 1
        elif o == AC:
            yourscore += 1
            ace = 1
        elif o == AD:
            yourscore += 1
            ace = 1
        else:
            yourscore += 10
        if yourscore > 21.5:
            print("You busted")
            yb = 5
            t = 3
            money = int(money) - int(bet)
            print("You have $" + str(money))
    #changing you score










myapp = App()
app = App(500,500)  
app.run(step)
myapp.listenKeyEvent('keydown','space',pauseplay)
myapp.listenKeyEvent('keydown','s',stay)
myapp.listenKeyEvent('keydown','h',hit)
myapp.listenKeyEvent('keydown','r',rules)