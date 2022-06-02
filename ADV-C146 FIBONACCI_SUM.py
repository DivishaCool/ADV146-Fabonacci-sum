# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:28:40 2022

@author: 91977
"""

from tkinter import *

root=Tk()
root.title("Febonacci")
root.geometry("400x400")

root.configure(bg='#ffc4d4')


label_series = Label(root , text = "Febonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def Febonacci():
    num = 10
    first_number = 0
    second_number = 1
    sum = 0
    counter = 1
    number = input("Enter a number : ")
    while (counter <= num):
        label_series['text'] += str(sum) + " "
        counter = counter + 1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number
    
    label_flower['text'] = "Flower is fully bloomed"
    label_spiral['text'] = "Spirals in right direction are " + str(first_number) + "And spirals in the left direction are" + str(second_number) + "Total number of spirals are :" + str(sum)

btn = Button(root , text = "Show Febonacci series" ,  command = Febonacci , bg = "#06055c" ,  fg="white" , relief = "groove" , highlightcolor="cyan")
btn.grid(row = 1, column = 3, pady = 10, padx = 100)
btn.pack()
number.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
    
root.mainloop()
