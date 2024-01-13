import random


print(
    " In order to win rock paper scissors the conditions are  :\n"
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Scissors vs Paper -> Scissors wins \n"
)

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your Choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice: "))

    if choice == 1:
        choice == "Rock"

    elif choice == 2:
        choice == "Paper"

    elif choice == 3:
        choice == "Scissor"

    print("You chose ", choice)

    print("Computer chose... ")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"

    elif comp_choice == 2:
        comp_choice_name = "Paper"

    else:
        comp_choice_name = "Scissor"

    print("Computer = \n", comp_choice_name)

    print(choice, "v", comp_choice_name)

    if choice == comp_choice:
        print("Drawn", end="")

        result = "Draw"

    if choice == 1 and comp_choice == 2:
        print("paper wins => ", end="")

        result = "Paper"

    elif choice == 2 and comp_choice == 1:
        print("paper wins => ", end="")

        result = "Paper"

    if choice == 1 and comp_choice == 3:
        print("Rock wins => ", end="")

        result = "Rock"

    elif choice == 3 and comp_choice == 1:
        print("Rock wins => ", end="")

        result = "Rock"

    if choice == 2 and comp_choice == 3:
        print("Scissors wins => ", end="")

        result = "Scissors"

    elif choice == 3 and comp_choice == 2:
        print("Scissors win => ", end="")

        result = "Scissors"

    if result == "Draw":
        print("<== Both win ==>")

    if result == choice:
        print("<== User wins ==>")

    else:
        print("<== Computer wins ==>")

    print("Play again? (Y/N)")

    ans = input().lower

    if ans == "n":
        break

    print("Thank you for playing.")
