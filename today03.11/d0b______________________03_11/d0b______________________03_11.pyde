x=1
def setup():
     size (1000 ,1000)
def draw():
    global x
    background (200 ,0 ,0)
    fill (x ,x ,x)
    ellipse (500 ,500 ,50 ,50)
    x=x+1
    if x == 255:
        x=x-255
