import turtle, math

bob = turtle.Turtle()

"""
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 200)
"""
"""
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(bob, 100, 15)
"""
"""
def circle(t, r):
    for i in range(5):
        t.fd()
        fd.rt()
"""


def turtle_pies(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    
    for i in range(2):
        t.lt(45)
        t.fd(70)
              
        

turtle_pies(bob, 100, 5)



def polyline(t,n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t,r,angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t,r):
    arc(t,r, 35)


turtle.mainloop()
