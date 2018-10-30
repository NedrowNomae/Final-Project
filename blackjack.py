
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
import random

cards = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH']
random.shuffle(cards)
print(cards)
#hearts
"""
class 2H(Sprite):
    2H = ImageAsset("2H.png")
    def __init__(self,  position):
        super().__init__(2H.2H, position)
class 3H(Sprite):
    3H = ImageAsset("3H.png")
    def __init__(self,  position):
        super().__init__(3H.3H, position)
class 4H(Sprite):
    4H = ImageAsset("4H.png")
    def __init__(self,  position):
        super().__init__(4H.4H, position)
class 5H(Sprite):
    5H = ImageAsset("2H.png")
    def __init__(self,  position):
        super().__init__(5H.5H, position)
6H
7H
8H
9H
10H
JH
QH
KH
AH

#diamonds
2D
3D
4D
5D
6D
7D
8D
9D
10D
JD
QD
KD
AD

#spades
2S
3S
4S
5S
6S
7S
8S
9S
10S
JS
QS
KS
AS

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

"""

    
    


app = App(500,500)  
app.run()