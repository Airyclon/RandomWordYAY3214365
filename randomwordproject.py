from tkinter import *
import random
root = Tk()

root.title("Random Word")
root.geometry("500x500")

label = Label(root)

def random_word():
    list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(list1)
    randomletter1 = random.randint(0, 51)
    randomletter2 = random.randint(0, 51)
    randomletter3 = random.randint(0, 51)
    randomletter4 = random.randint(0, 51)
    randomletter5 = random.randint(0, 51)
    alphabet1 = list1[randomletter1]
    alphabet2 = list1[randomletter2]
    alphabet3 = list1[randomletter3]
    alphabet4 = list1[randomletter4]
    alphabet5 = list1[randomletter5]
    if(alphabet1 == "A"):
        alphabet1 = "&"

    if(alphabet1 == "a"):
        alphabet1 = ":)"

    if(alphabet5 == "A"):
        alphabet1 = "QWERTYUIOPASDFGHJKLZXCVBNM"

    label["text"] = "Your random word is- " + alphabet1+alphabet2+alphabet3+alphabet4+alphabet5

btn1 = Button(root, text = "What is ur Random Nuber?", command = random_word)
btn1.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()