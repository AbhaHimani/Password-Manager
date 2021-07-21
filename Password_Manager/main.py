# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
from random import choice, randint, shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters =[choice(letters) for _ in range(randint(8,10))]
    password_symbols= [choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _  in range(randint(2,4))]
    password_list= password_numbers+password_symbols+password_letters
    shuffle(password_list)
    password= "".join(password_list)
    input_password.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    passw= open("saved_password.txt","w")
    passw.write(input_name.get())
    passw.write("\n |")
    passw.write(input_email.get())
    passw.write("\n | ")
    passw.write(input_password.get())






# ---------------------------- UI SETUP ------------------------------- #
import tkinter
window= tkinter.Tk()
canvas= tkinter.Canvas(width=300, height=300)
window.title("Password Manager")
window.minsize(600,600)
img= tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.place(x=150, y=40)
my_label=tkinter.Label(text="Website:",font=("Arial", 14, "bold"))
my_label.place(x=120,y=255)
input_name= tkinter.Entry()
input_name.place(x=200, y=260)
input_name.focus()

my_label=tkinter.Label(text="Email:",font=("Arial", 14, "bold"))
my_label.place(x=120,y=285)
input_email= tkinter.Entry()
input_email.place(x=200, y=290)

my_label=tkinter.Label(text="Password:",font=("Arial", 14, "bold"))
my_label.place(x=120,y=310)
input_password= tkinter.Entry()
input_password.place(x=240, y=315)

#button
button= tkinter.Button(text="Generate",command=generate_password)
button.place(x=240, y=350)

#button
button= tkinter.Button(text="Add", command=save_password)
button.place(x=240,y=390)




window.mainloop()


