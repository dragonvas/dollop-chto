x=1
def setup():
     size (1000 ,1000)
def draw():
    global x
    background (200 ,0 ,0)
    ellipse (500 ,500 ,x ,x)
    x=x+1
    if x == 400:
        x=x-399
