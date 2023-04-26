name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

print("You are on a dirt road, it has come to an end.")

answer = input(
    "Choose whether to proceed right or left ? : "
).lower()

if answer == "left":

    print("You come to a river, you can walk around it or swim across ?")

    answer = input("Type walk to walk around and swim to swim across: ")

    if answer == "swim":

        print("Oops! You swam across and were eaten by an alligator.")

    elif answer == "walk":

        print(" You walked for many miles, ran out of water and you lost the game")

    else:
        print("Not a valid option. You loose.")


elif answer == "right":
    print("You come to a bridge, it looks wobbly,")

    print(" do you want to cross it or head back?")

    answer = input("choose either cross / back ? : ")
   
    if answer == " back":
        print("You go back and loose")
    
    elif answer == "cross":
        print("You cross the bridge and meet a stranger.")
        answer = input("Do you talk to them (yes / no) ? : ")

        if answer == "yes":
            print(" Tell the stranger to give you gold")
            print("Yepeee", name, "wins the game and a pot of gold" )

        elif answer == "no":
            print(" You ignored the stranger thus loose")

        else:
            print("Not a valid option. You loose")

    else:
        print('Not a valid option. You loose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
