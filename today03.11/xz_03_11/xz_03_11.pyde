x=1
def setup():
     size (1000 ,1000)
def draw():
    global x
    background (200 ,0 ,0)
    ellipse (x ,x ,50 ,50)
    x=x+1
    if x == 1000:
        x=x-999
