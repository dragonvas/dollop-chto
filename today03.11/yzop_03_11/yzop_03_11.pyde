x=1
v=1
z=45
def setup():
     size (1000 ,1000)
def draw():
    global x,z,v
    rotate(z)
    scale(v)
    background (200 ,0 ,0)
    fill (x ,100 ,x)
    ellipse (700 ,700 ,50 ,50)
    triangle (450 ,450 ,600 ,300 ,555 ,444)
    rect (303 ,303 ,30 ,30)
    x=x+1
    z=z+45
    v=v+0.1
    if x == 255:
        x=x-255
    if v == 1.1:
        v=1
