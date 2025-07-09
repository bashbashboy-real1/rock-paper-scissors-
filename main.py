import random
from tkinter import *
    
root=Tk()
root.title("mathyyyyyy")
root.geometry("450x300")
    

options= ("rock", "paper", "scissors")
my_score=0
computer_score=0
count=0

def rock():
        
    play("rock")
      
def paper():
    play("paper")

def scissors():
    play("scissors")
         
def update_status():
    status.config(text=f"My Score: {my_score} | Computer Score: {computer_score}")

def play(my_choice):
    global count, my_score, computer_score
    computer_choice = random.choice(options)
    computer_c.config(text=computer_choice, font=("Times New Roman", 40, "bold"))
    
    if my_choice == "rock":
        if computer_choice == "scissors":
            my_score += 1
        elif computer_choice == "paper":
            computer_score += 1
    elif my_choice == "paper":
        if computer_choice == "rock":
            my_score += 1
        elif computer_choice == "scissors":
            computer_score += 1
    elif my_choice == "scissors":
        if computer_choice == "paper":
            my_score += 1
        elif computer_choice == "rock":
            computer_score += 1
    
    count+=1 
    update_status()
    
    if count>=3 :
        if my_score> computer_score:
        
            status.config(text="you ROCK!!!!")

        elif my_score < computer_score:
        
            status.config(text="-_- i win")
        else: 
            status.config(text="its a tie")
        
        count=0
        my_score=0
        computer_score=0

computer_c= Label(root, text="")
computer_c.pack()
    
status= Label(root, text="" )
status.pack()
        
rock_btn= Button(root, text= "rock", command=rock)
rock_btn.pack(padx= 60, side=LEFT)
        
paper_btn= Button(root, text= "paper", command=paper)
paper_btn.pack(side= LEFT )
        
scissors_btn= Button(root, text= "scissors", command=scissors)
scissors_btn.pack(padx= 60,side=RIGHT)   

root.mainloop()
