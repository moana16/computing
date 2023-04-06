import turtle as t

def rectangle(size):
    for x in range(4):
        t.fd(size)
        t.rt(90)

rectangle(50)
rectangle(100)