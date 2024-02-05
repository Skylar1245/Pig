import random as R

playerOneName = input("Who is player 1?")
playerTwoName = input("Who is player 2?")

TotalOne = 0
TotalTwo = 0
Running = 0

currentTurn = 1

yes = ["y", "e", "s", "Y", "E", "S"]
no = ["n", "N", "o", "O"]

while (TotalOne <= 100) and (TotalTwo <= 100):
    d1 = R.randint(1, 6)
    d2 = R.randint(1, 6)
    roll = d1 + d2
    Running += roll
    if d1 != 1 and d2 != 1:
        if currentTurn == 1:
            print(
                "It is",
                playerOneName,
                "'s turn, their roll is:",
                d1,
                "and",
                d2,
                "their running total is",
                Running,
                ". Total bank is:",
                TotalOne,
            )
        else:
            print(
                "It is",
                playerTwoName,
                "'s turn, their roll is:",
                d1,
                "and",
                d2,
                "their running total is",
                Running,
                ". Total bank is:",
                TotalTwo,
            )

        option = input("Do you want to roll again?")
        if option in yes:
            pass

        elif option in no:
            if currentTurn == 1:
                TotalOne += Running
                currentTurn = 2
            elif currentTurn == 2:
                TotalTwo += Running
                currentTurn = 1
            Running = 0

    elif d1 == 1 and d2 == 1:
        if currentTurn == 1:
            print(
                "Looks like",
                playerOneName,
                "rolled Snake Eyes! Your total is now 0 and it is the next players turn, ",
            )
            null = input("Enter any text to move on")
            TotalOne = 0
            currentTurn = 2
        else:
            print(
                "Looks like",
                playerTwoName,
                "rolled Snake Eyes! Your total is now 0 and it is the next players turn, ",
            )
            null = input("Enter any text to move on")
            TotalTwo = 0
            currentTurn = 1
        Running = 0
    else:
        if currentTurn == 1:
            currentTurn = 2
            print("Looks like", playerOneName, "rolled a 1! ")
            null = input("This turn is now void, however you keep your banked score!")
        else:
            currentTurn = 1
            print("Looks like", playerTwoName, "rolled a 1! ")
            null = input("This turn is now void, however you keep your banked score!")
        Running = 0


if TotalOne <= 100:
    print("Cpngrats!", playerOneName, "Won!")
else:
    print("Congrats!", playerTwoName, "Won!")
