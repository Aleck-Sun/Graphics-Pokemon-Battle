from tkinter import *
from random import *

myInterface = Tk()
s = Canvas( myInterface, width=700, height=540, background="black")
s.pack()

#Background
BG = ["#009933", "#33cc33", "#66ff33", "#99ff33", "#ccff33", "#d9ff66", "#ccff33", "#99ff33", "#66ff33", "#33cc33", "#009933"]
y = 40
y2 = 0

for x in range (0, 11):
    color = BG[x]
    s.create_rectangle(0, y, 700, y2, fill = color, outline = color)
    y += 40
    y2 += 40


#Battlergrounds
#ally
s.create_oval(0, 300, 375, 450, fill = "#d1b551", outline = "#d1b551")
s.create_oval(5, 305, 370, 445, fill = "green", outline = "green")
#enemy
s.create_oval(325, 140, 690, 265, fill = "#d1b551", outline = "#d1b551")
s.create_oval(330, 145, 685, 260, fill = "green", outline = "green")
#grass
for grass in range (0, 1000):
    xchoice = randint(1, 2)
    if xchoice == 1:
        x = randint(400, 600)
        y = randint(160, 240)
    else:
        x = randint(50, 300)
        y = randint(325, 375)
    greenchoice = ["#079e2a", "#63ff87", "#19ff00"]
    greencolour = choice(greenchoice)
    grasswidth = randint(1, 2)
    s.create_line(x, y, x, y + 10, fill = greencolour, width = grasswidth)

for grass in range (0, 200):
    xchoice = randint(1, 2)
    if xchoice == 1:
        x = randint(350, 400)
        y = randint(175, 215)
    else:
        x = randint(10, 50)
        y = randint(350, 375)
    greenchoice = ["#079e2a", "#63ff87", "#19ff00"]
    greencolour = choice(greenchoice)
    grasswidth = randint(1, 2)
    s.create_line(x, y, x, y + 10, fill = greencolour, width = grasswidth)

for grass in range (0, 200):
    xchoice = randint(1, 2)
    if xchoice == 1:
        x = randint(600, 650)
        y = randint(175, 215)
    else:
        x = randint(300, 360)
        y = randint(350, 375)
    greenchoice = ["#079e2a", "#63ff87", "#19ff00"]
    greencolour = choice(greenchoice)
    grasswidth = randint(1, 2)
    s.create_line(x, y, x, y + 10, fill = greencolour, width = grasswidth)

#Pokemon
#Digglet
s.create_oval(225, 300+50/3, 240, 300+50/3*2, fill = "#ffccf4", outline = "black")
s.create_rectangle(120, 325, 230, 375, fill = "#c47538", outline = "black")
s.create_arc(120, 270, 230, 380, start  = 0, extent = 180, fill = "#c47538", outline = "black")
s.create_line(121, 325, 229, 325, fill = "#c47538", width = 1)
#Spiritomb
#body
s.create_polygon(450, 250, 550, 250, 525, 175, 475, 175, fill = "#a59c8e", smooth = True)
s.create_polygon(500, 200, 575, 175, 575, 75, 500, 50, 425, 75, 425, 175, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(500, 200, 575, 175, 480, 220, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(575, 175, 575, 75, 600, 200, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(575, 75, 500, 50, 610, 45, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(500, 50, 425, 75, 510, 30, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(425, 75, 425, 175, 390, 50, fill = "#dd9bff", outline = "#dd9bff")
s.create_polygon(425, 175, 500, 200, 385, 185, fill = "#dd9bff", outline = "#dd9bff")
#Decorations
s.create_oval(450, 100, 430, 80, fill = "#59ff54", outline = "#59ff54")
s.create_oval(475, 85, 465, 75, fill = "#59ff54", outline = "#59ff54")
s.create_oval(510, 65, 530, 85, fill = "#59ff54", outline = "#59ff54")
s.create_oval(545, 80, 555, 90, fill = "#59ff54", outline = "#59ff54")
s.create_oval(550, 120, 570, 140, fill = "#59ff54", outline = "#59ff54")
s.create_oval(548, 155, 558, 165, fill = "#59ff54", outline = "#59ff54")
s.create_oval(510, 170, 530, 190, fill = "#59ff54", outline = "#59ff54")
s.create_oval(465, 167, 485, 187, fill = "#59ff54", outline = "#59ff54")
s.create_oval(440, 160, 450, 170, fill = "#59ff54", outline = "#59ff54")
s.create_oval(420, 120, 435, 135, fill = "#59ff54", outline = "#59ff54")
#face
s.create_polygon(450, 100, 495, 120, 465, 130, fill = "#59ff54")
s.create_polygon(545, 95, 500, 120, 530, 135, fill = "#59ff54")
s.create_line(460, 148, 470, 152, 480, 145, 490, 155, 500, 140, 510, 155, 520, 145, 530, 152, 540, 148, fill = "#59ff54", width = 5)
s.create_line(525, 118, 522, 121, 525, 124, 531, 118, 525, 112, 516, 121, 525, 130, 525, 130, smooth = True, width = 2)

#Hp Bars
s.create_polygon(50, 100, 75, 155, 300, 155, 250, 100, fill = "#566b55", outline = "#566b55") 
s.create_oval(25, 75, 45, 95, fill = "#566b55", outline = "#566b55")
s.create_oval(275, 150, 255, 130, fill = "#566b55", outline = "#566b55")
s.create_rectangle(25, 85, 265, 150, fill = "#566b55", outline = "#566b55")
s.create_rectangle(35, 75, 275, 140, fill = "#566b55", outline = "#566b55")
s.create_oval(30, 80, 50, 100, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_oval(270, 145, 250, 125, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_rectangle(30, 90, 260, 145, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_rectangle(35, 80, 270, 135, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_text(105, 100, text = "SPIRITOMB", font = "fixedsys 17")
s.create_text(240, 100, text = "Lv15", font = "fixedsys 17")
s.create_line(75, 125, 260, 125, fill = "grey", width = 15)
s.create_text(85, 125, text = "HP", font = "fixedsys 16", fill = "#ffa42d")
s.create_line(100, 125, 257, 125, fill = "white", width = 10)
hp = randint(120, 252)
s.create_line(105, 125, hp, 125, fill = "#57ff2d", width = 5)
#Hp bar for digglet
s.create_polygon(350, 370, 400, 370, 400, 325, fill = "#566b55", outline = "#566b55")
s.create_oval(670, 370, 650, 350, fill = "#566b55", outline = "#566b55")
s.create_rectangle(400, 325, 660, 370, fill = "#566b55", outline = "#566b55")
s.create_rectangle(650, 305, 670, 360, fill = "#566b55", outline = "#566b55")
s.create_oval(375, 250, 395, 270, fill = "#566b55", outline = "#566b55")
s.create_oval(650, 350, 630, 330, fill = "#566b55", outline = "#566b55")
s.create_rectangle(375, 260, 640, 350, fill = "#566b55", outline = "#566b55")
s.create_rectangle(385, 250, 650, 340, fill = "#566b55", outline = "#566b55")
s.create_oval(380, 255, 400, 275, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_oval(645, 345, 625, 325, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_rectangle(380, 265, 635, 345, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_rectangle(390, 255, 645, 335, fill = "#f2e1c9", outline = "#f2e1c9")
s.create_text(440, 280, text = "DIGGLET", font = "fixedsys 17")
s.create_text(610, 280, text = "Lv45", font = "fixedsys 17")
s.create_line(425, 305, 635, 305, fill = "grey", width = 15)
s.create_text(435, 305, text = "HP", font = "fixedsys 16", fill = "#ffa42d")
s.create_line(450, 305, 632, 305, fill = "white", width = 10)
s.create_line(455, 305, 575, 305, fill = "#57ff2d", width = 5)
s.create_text(575, 330, text = "100/ 127", font = "fixedsys 17")
s.create_text(400, 360, text = "EXP", font = "fixedsys 16", fill = "#ffa42d")
expbar1 = 425
for barincrease in range (0, 55):
    s.create_line(expbar1, 360, expbar1+3, 360, fill = "#ffa42d", width = 3)
    expbar1+=4

#PokeMenu
s.create_rectangle(0, 375, 700, 540, fill = "black", outline = "black")
#Yellow box menu border
s.create_oval(5, 380, 20, 395, fill = "#EEC500", outline = "#EEC500")
s.create_oval(5, 535, 20, 520, fill = "#EEC500", outline = "#EEC500")
s.create_rectangle(5, 387.5, 370, 527.5, fill = "#EEC500", outline = "#EEC500")
s.create_rectangle(12.5, 380, 370, 535, fill = "#EEC500", outline = "#EEC500")
#White box and turquoise menu border
s.create_rectangle(15, 390, 370, 525, fill = "white", outline = "white")
s.create_rectangle(20, 395, 370, 520, fill = "#014E6A", outline = "#014E6A")
#Pokemon Text
s.create_text(110, 440, text = "What  will", font = "fixedsys 24", fill = "white")
s.create_text(90, 485, text = "DIGGLET", font = "fixedsys 24 bold", fill = "white")
s.create_text(195, 485, text = "do?", font = "fixedsys 24", fill = "white")


#Battlemenu
#Blue-Grey
s.create_oval(375, 380, 390, 395, fill = "#595b82", outline = "#595b82")
s.create_oval(695, 380, 680, 395, fill = "#595b82", outline = "#595b82")
s.create_oval(695, 535, 680, 520, fill = "#595b82", outline = "#595b82")
s.create_oval(375, 535, 390, 520, fill = "#595b82", outline = "#595b82")
s.create_rectangle(375, 387.5, 695, 527.5, fill = "#595b82", outline = "#595b82")
s.create_rectangle(382.5, 380, 687.5, 535, fill = "#595b82", outline = "#595b82")
#White
s.create_oval(385, 390, 395, 400, fill = "white", outline = "white")
s.create_oval(685, 390, 675, 400, fill = "white", outline = "white")
s.create_oval(685, 525, 675, 515, fill = "white", outline = "white")
s.create_oval(385, 525, 395, 515, fill = "white", outline = "white")
s.create_rectangle(385, 395, 685, 520, fill = "white", outline = "white")
s.create_rectangle(390, 390, 680, 525, fill = "white", outline = "white")
#Select button
s.create_polygon(395, 420, 395, 440, 405, 430, fill = "black", outline = "black")
#Battle Text
s.create_text(455, 430, text = "FIGHT", font = "fixedsys 24", fill = "black")
s.create_text(470, 485, text = "POKéMON", font = "fixedsys 24", fill = "black")
s.create_text(600, 430, text = "BAG", font = "fixedsys 24", fill = "black")
s.create_text(600, 485, text = "RUN", font = "fixedsys 24", fill = "black")

s.update()
