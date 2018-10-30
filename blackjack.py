
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset


s = Sprite(ImageAsset("4D.png"), (100,200))
s.scale = .1


app = App(500,500)  
app.run()