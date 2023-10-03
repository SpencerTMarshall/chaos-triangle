import tkinter as tk
import random

root = tk.Tk()

root.title('Triangle Visualizer')
root.geometry('450x450+50+50')
root.resizable(False, False)

canvas = tk.Canvas(root, height=400, width=400, bg='blue')

p1 = (7.5, 392.5)
p2 = (200, 7.5)
p3 = (392.5, 392.5)
size_of_points = 5

canvas.create_oval(p1[0]-size_of_points/2, p1[1]-size_of_points/2, p1[0]+size_of_points/2, p1[1]+size_of_points, fill="red")
canvas.create_oval(p2[0]-size_of_points/2, p2[1]-size_of_points/2, p2[0]+size_of_points/2, p2[1]+size_of_points, fill="red")
canvas.create_oval(p3[0]-size_of_points/2, p3[1]-size_of_points/2, p3[0]+size_of_points/2, p3[1]+size_of_points, fill="red")

pos = [392.5, 392.5]

def nextCircle(event):
    match random.randint(1,3):
        case 1:
            pos[0] = (pos[0] + p1[0]) / 2
            pos[1] = (pos[1] + p1[1]) / 2
            canvas.create_oval(pos[0]-size_of_points/2, pos[1]-size_of_points/2, pos[0]+size_of_points/2, pos[1]+size_of_points/2, fill="black")
            return
        case 2:
            pos[0] = (pos[0] + p2[0]) / 2
            pos[1] = (pos[1] + p2[1]) / 2
            canvas.create_oval(pos[0]-size_of_points/2, pos[1]-size_of_points/2, pos[0]+size_of_points/2, pos[1]+size_of_points/2, fill="black")
            return
        case 3:
            pos[0] = (pos[0] + p3[0]) / 2
            pos[1] = (pos[1] + p3[1]) / 2
            canvas.create_oval(pos[0]-size_of_points/2, pos[1]-size_of_points/2, pos[0]+size_of_points/2, pos[1]+size_of_points/2, fill="black")
            return

canvas.bind("<Motion>", nextCircle)
canvas.pack()

root.mainloop()
