from tkinter import *
import tkinter.messagebox
import random
root = Tk()

def gtn():
    code_number = random.randint(0, 1000)
    coins = 100
    count = 0
    wrong_guesses = []
    while coins > 0:
        user_guess = int(input("enter your guess:"))
        if user_guess == code_number:
            print('Congrats ! You won ',coins,' coins')
            break
        else:
            if user_guess > code_number:
                print('your guess is greater than secret code')
                tkinter.messagebox._show('Hint:','your guess is greater than secret code')
            else:
                print('your guess is smaller than secret code')
                tkinter.messagebox._show('Hint:', 'your guess is smaller than secret code')
            wrong_guesses.append(user_guess)
            print('Your Wrong Guesses: ', wrong_guesses)
            tkinter.messagebox._show('Your Wrong Guesses:',wrong_guesses)
            count = count * 2
            coins = coins - 10
    if coins == 0:
        print('YOU LOSE..! You have lost all your coins')
        tkinter.messagebox._show('Game Result:',"YOU LOSE..! You have lost all your coins")
    else:
        print('.....')

def printmyname():
    name = Entry.get(E1)
    printname = "Hello..."+name
    print('Helloo...',name)
    Entry.insert(E2,0,printname)

label1 = Label(root, text = "Welcome to GTN", bg = 'purple', fg ='white')
label1.grid(row=0,columnspan=2)
label2 = Label(root, text = "Name:", bg = 'purple', fg ='white')
label2.grid(row=1,sticky=E,columnspan=1)

b1 = Button(root, text = "Ready !", fg = 'red',command = printmyname)
b1.grid(row=2,columnspan=2)
E1= Entry(root)
E1.grid(row=1,column=1)
E2 = Entry(root)
E2.grid(row=3,columnspan=2)
E3 = Entry(root)
E3.grid(row=5,columnspan=2)
E4 = Entry(root)
E4.grid(row=6,columnspan=2)

b2 = Button(root, text = 'Enter into game', fg = 'blue',command = gtn)
b2.grid(row=4,columnspan=2)

root.mainloop()
