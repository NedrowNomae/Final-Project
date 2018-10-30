
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
import random

cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']
random.shuffle(cards)
print(len(cards))
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
class 10H(Sprite):
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
2C
3C
4C
5C
6C
7C
8C
9C
10C
JC
QC
KC
AC = Sprite(ImageAsset("4D.png"))


H2((100,100))
    
    


app = App(500,500)  
app.run()