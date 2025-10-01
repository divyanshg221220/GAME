# ODD EVEN
from random import randint,choice
def user_input():
    while True:
        try:
            user = int(input("Enter a number between 1 and 10: "))
            if 1 <= user <= 10:
                return user
            else:
                raise Exception
        except:
            dash()
            print("Invalid input! Please enter a number between 1 and 10.")
            dash()
def computer_input():
    computer = randint(1, 10)
    print("Computer chose:", computer)
    return computer
def role():
    dash()
    print("Batting:",bat)
    print("Bowling:",ball)
    dash()
def toss():
    global bat, ball
    while True:
        try:
            q=input("Enter 'O' for Odd or 'E' for Even: ").upper()
            if q in ["O","E"]:
                break
            else:
                raise Exception
        except:
            dash()
            print("Invalid input! Please enter 'O' for Odd or 'E' for Even.")
            dash()
    user, computer = user_input(), computer_input()
    print("Toss: ", user + computer, "->", "Odd" if (user + computer) % 2 == 1 else "Even")
    if (q=="O" and (user + computer) % 2 == 1) or (q=="E" and (user + computer) % 2 == 0):
        while True:
            try:
                dash()
                q=input("You won the toss! Enter BAT or BALL: ").upper()
                if q in ["BAT", "BALL"]:
                    if q == "BAT":
                        bat = "user"
                        ball = "computer"
                    else:
                        bat = "computer"
                        ball = "user"
                    break
                else:
                    raise Exception
            except:
                dash()
                print("Invalid input! Please enter 'BAT' or 'BALL'.")
                dash()
    else:
        dash()
        print("Computer won the toss!")
        if choice(["BAT", "BALL"]) == "BAT":
            bat = "computer"
            ball = "user"
            print("Computer chose BAT.")
        else:
            bat = "user"
            ball = "computer"
            print("Computer chose BALL.")
def score(user_input,computer_input):
    global user_score, computer_score
    if bat=="user" or ball=="computer":
        user_score+=user_input
    elif bat=="computer" or ball=="user":
        computer_score+=computer_input
def dash():
    print("-"*30)
def odd_even():
    global flag, bat, ball
    toss()
    dash()
    role()
    while True:
        user, computer = user_input(), computer_input()
        if user!=computer:
            score(user, computer)
        elif user==computer and flag==0:
            dash()
            print("Innings over! Switching roles.")
            print("User Score:", user_score)
            print("Computer Score:", computer_score)
            dash()
            bat, ball = ball, bat
            role()
            flag=1
        else:
            break
    dash()
    print("Final Scores:")
    print("User Score:", user_score)
    print("Computer Score:", computer_score)
    dash()
    if user_score > computer_score:
        print("User wins!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")
    dash()
user_score = 0
computer_score = 0
bat=""
ball=""
flag=0
odd_even()