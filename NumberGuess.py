from tkinter import*
from tkinter.font import*
from tkinter import messagebox
from random import randint

#Interface
root = Tk()
root.geometry("700x700")
root.title("NUMBER GUESSING GAME")
root.resizable(False,False)

#Generate Number
def GenFunc():
    global num
    num = randint(1,100)
    #Message
    messagebox.showinfo("Number is Generated!","GUESS THE NUMBER!!\nYou have 10 attempts to guess.")

attempts=10
count=0

#Guess number
def GuessNum():
    global num
    global attempts
    global count
    
    Response=Input.get()
    
    if len(str(Response))==0 or int(Response)>100:
        messagebox.showerror("ERROR","Please enter a number range[1,100].")
    else:
    #Check response 
        Response=int(Response)
        attempts-=1 
        count+=1
        if Response == num:
            ResultLabel.config(text="CORRECT GUESS!!\nThe Number was {}\n\nNo. of attempts {}".format(num,count),fg="green")
        elif attempts==0:
            ResultLabel.config(text="Oops!! You are out of attempts.\nNumber was {}".format(num),fg="red")
        elif Response < num:
            ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.Try Again\n\nHint: Try a higher number.",fg="red")
        else :
            ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining Try Again\n\nHint: Try a lesser number.",fg="red")
            
        Input.delete(0, "end")        
        
    if count==2:
            if num%2==0:
                ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is an Even number.",fg="red")
            else:
                ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is an Odd number.",fg="red")
    elif count==5:
            if num>1:
                for i in range(2,num//2):
                    if(num%i)==0:
                        ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is a Prime number.",fg="red")
                    else:
                        ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is not a Prime number.",fg="red")        
    elif count==8:
            if num%2==0:
                    ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is a multiple of 2.",fg="red")
            elif num%3==0:
                    ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is a multiple of 3.",fg="red")
            elif num%5==0: 
                    ResultLabel.config(text="Incorrect guess!!\nYou have " + str(attempts) + " Attempts remaining.\n\nHint: It is a multiple of 5.",fg="red")   
    else:
        ResultLabel.config("")                           
    return
#Create an object of tkinter ImageTk
img = PhotoImage(file="Guessimages.png")

#Onscreen labelling
Title = Label(root,text="Number Guessing Game !!!", font=('Arial',20,BOLD))
Title.pack()

#Create a Label Widget to display the text or Image
Label(root,image=img).pack()

#Frame
MainFrame = Frame(root)
MainFrame.pack()

#Label 
GuessLabel = Label(MainFrame,text="Guess a number from 1 to 100 :",font=("Oswald",15))
GuessLabel.pack()

#Input
Input = Entry(MainFrame,font="Oswald,12")
Input.pack(pady=10)

#Number Generator
NumGenerator = Button(MainFrame,text="Generate Number",width=16,font=("Roboto",12),bg=("#33E3FF"),command=GenFunc)
NumGenerator.pack()

#Guessbutton
GuessButton = Button(MainFrame,text="Guess",width=16,font=("Roboto",12),bg=("#33E3FF"),command=GuessNum)
GuessButton.pack(pady=5)

#Result
ResultLabel = Label(MainFrame,text="",font=("Roboto",14))
ResultLabel.pack(pady=10)

#Quit Button
Quit=Button(MainFrame,text="Quit",width=12,font=("Roboto",12),command=root.destroy)
Quit.pack(pady=30)

#Main loop
root.mainloop()