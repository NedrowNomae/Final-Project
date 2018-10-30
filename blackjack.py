
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
"""
#hearts
2H = Sprite
3H
4H
5H
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
AC
"""
s= Sprite(ImageAsset("4D.png"), (100,200))
s.scale = .1


app = App(5000,5000)  
app.run()