import pgzrun
def draw():
    screen.clear()
    screen.fill("red")
    screen.draw.circle((40,200),50,"blue")
    screen.draw.filled_circle((60,300),50,"blue")
    screen.draw.rect(Rect((150,150),(50,100)),"white")
    screen.draw.line((10,10),(100,100),"white")
pgzrun.go()    