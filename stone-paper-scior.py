from tkinter import *
import random
from tkinter import messagebox

win = Tk()
win.title("Stone Paper Scissor")
win.geometry("510x510")

score1 = 0  # Initial player score
player_choice = ""

frame = Frame(win)
frame.grid(row=0, column=0)
score = Label(frame, text=f"Player Score: {score1}", background="#c539cc", width=70, height=2)
score.grid(row=0)

choices = ["rock.png", "paper.png", "scissor.png"]

canva2 = Canvas(win, width=500, height=180, background="black")
canva2.grid(row=1, column=0, padx=2, pady=3)
canva1 = Canvas(win, width=500, height=180, background="black")
canva1.grid(row=2, column=0, padx=2, pady=3)

# Global variable to store the current computer image
current_computer_image = None

def player(image_path):
    global player_choice
    global current_computer_image
    player_choice = image_path
    canva1.delete("all")
    current_image = PhotoImage(file=image_path)
    canva1.create_image(0, 0, anchor=NW, image=current_image)
    computer_choice = random.choice(choices)
    current_computer_image = PhotoImage(file=computer_choice)
    computer(computer_choice)
    announce_winner(player_choice, computer_choice)

def computer(img_path):
    global current_computer_image
    canva2.delete("all")
    canva2.create_image(0, 0, anchor=NW, image=current_computer_image)

def announce_winner(player_choice, computer_choice):
    global score1
    if player_choice == computer_choice:
        messagebox.showinfo("Result", "It's a tie!")
    elif (player_choice == "rock.png" and computer_choice == "paper.png") or \
         (player_choice == "paper.png" and computer_choice == "scissor.png") or \
         (player_choice == "scissor.png" and computer_choice == "rock.png"):
        messagebox.showinfo("Result", "You lose!")
    else:
        messagebox.showinfo("Result", "You win!")
        score1 += 1
    score.config(text=f"Player Score: {score1}")

    # Ask if player wants to play again
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if play_again:
        # Clear canvases and reset
        canva1.delete("all")
        canva2.delete("all")
    else:
        win.destroy()  # Close the game window

frame2 = Frame(win)  
frame2.grid(row=3, column=0)

lab = Label(frame2, text="Make Your Choice:", pady=7)
lab.grid(row=0, columnspan=3)

but1 = Button(frame2, text="Rock", width=20, command=lambda: player("rock.png"), height=3, background="#c539cc")
but1.grid(row=1, column=0, padx=10)

but2 = Button(frame2, text="Paper", width=20, command=lambda: player("paper.png"), height=3, background="#c539cc")
but2.grid(row=1, column=1, padx=10)

but3 = Button(frame2, text="Scissor", width=20, command=lambda: player("scissor.png"), height=3, background="#c539cc")
but3.grid(row=1, column=2, padx=7)

win.mainloop()
