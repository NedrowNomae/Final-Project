
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
import random

cards = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'JH', 'QH', 'KH', 'AH', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'JD', 'QD', 'KD', 'AD', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'JS', 'QS', 'KS', 'AS', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'JC', 'QC', 'KC', 'AC']
random.shuffle(cards)
#print(len(cards))
print(cards)
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
    H7 = ImageAsset("10H.png")
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

s = cards[0]
print(s)
s((100,100))
#s = s.scale(.1)


    
    


app = App(500,500)  
app.run()