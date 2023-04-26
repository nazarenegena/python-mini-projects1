import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper","scissors"]
name = input(" Please enter your name : ")

while True:
    user_input = input(name + " could you type Rock / Paper / Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    # create a list
    if user_input not in options :
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    # the random number btwn 0 & 2 will be the index of the list value picked
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # deciding who won
    if user_input == "rock" and computer_pick == "scissors":
        print("Yeepee You Win!")
        user_wins +=1

   
    elif user_input == "paper" and computer_pick == "rock":
        print("Yepee You win!")
        user_wins +=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Yepee You win!")
        user_wins +=1

    else:
        print("Oopsy You Lost! ")
        computer_wins +=1

print(name,"You won ", user_wins, "times")
print("the computer won", computer_wins, "times")
     

print("Goodbye!")
