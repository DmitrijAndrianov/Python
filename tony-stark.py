import random;
from random import randrange
from tkinter import*
root=Tk()
root.geometry("800x700")
root.title("Like a BOSS")
canvas=Canvas(bg="white",width=400,height=700)
canvas.pack(anchor=CENTER,expand=1)
canvas.create_polygon(75,145,80,45,115,15,190,15,230,45,235,145,200,210,110,210,fill="red",outline="black",width=2)
canvas.create_polygon(75,145,95,100,100,50,80,45,fill="red",outline="black",width=2)
canvas.create_polygon(235,145,215,100,212,50,230,45,fill="red",outline="black",width=2)
canvas.create_polygon(75,145,95,100,100,50,120,25,135,70,170,70,185,25,212,50,215,100,235,145,190,184,180,175,130,175,120,185,fill="gold",outline="black",width=2)
canvas.create_polygon(100,110,96,90,140,95,142,105,outline="black",fill="white",width=2)
canvas.create_polygon(215,88,211,110,168,105,170,96,fill="white",width=2,outline="black")
canvas.create_polygon(110,210,120,185,130,175,180,175,190,184,200,209,fill="gold",outline="black",width=2)
canvas.create_polygon(130,175,135,170,175,170,180,175)
canvas.create_polygon(130,210,135,200,175,200,180,210,fill="red",width=2,outline="black")
canvas.create_line(140,95,170,96,width=2)
canvas.create_polygon(200,210,200,265,180,290,165,367,145,367,130,290,110,265,110,210,fill="red",outline="black",width=2)
canvas.create_polygon(110,210,110,265,80,240,fill="red",outline="black",width=2)
canvas.create_polygon(200,210,200,265,230,240,fill="red",outline="black",width=2)
canvas.create_polygon(200,265,230,240,235,270,220,285,fill="gold",width=2,outline="black")
canvas.create_polygon(245,270,235,270,220,285,220,320,240,320,fill="red",outline="black",width=2)
canvas.create_polygon(220,320,240,320,220,335,240,320,220,350,215,330,fill="red",outline="black",width=2)
canvas.create_polygon(80,240,110,265,90,285,75,275,fill="gold",outline="black",width=2)
canvas.create_polygon(90,285,75,270,65,270,75,320,90,320,fill="red",outline="black",width=2)
canvas.create_polygon(75,320,90,320,95,325,90,345,fill="red",outline="black",width=2)
canvas.create_oval(145,240,165,260,fill="turquoise1",width=0)
canvas.create_oval(140,235,170,265,width=3,outline="white")
canvas.create_polygon(180,290,168,350,205,350,200,265,fill="gold",outline="black",width=2)
canvas.create_polygon(142,350,130,290,110,265,105,350,fill="gold",outline="black",width=2)
canvas.create_polygon(105,350,142,350,145,367,145,390,100,390,fill="red",width=2,outline="black")
canvas.create_polygon(205,350,168,350,165,367,165,390,210,390,fill="red",width=2,outline="black")



root.mainloop()


