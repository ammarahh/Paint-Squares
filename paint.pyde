def setup():
    global myFill 
    myFill = "red"
    size(500,500)
    background(255)
    fill(255,0,0)
    rect(0,0,250,30)
    fill(0,0,255)
    rect(250,0,250,30)

def draw():
    global myFill
    if mouseButton and mouseY < 30:
        if mouseX < 250:
            myFill = "red"
        else:
            myFill = "blue"
    
    elif mouseButton and mouseY > 30:
        if myFill == "red":
            fill(255,0,0)
        else:
            fill(0,0,255)
        noStroke()
        ellipse(mouseX, mouseY, 10,10)