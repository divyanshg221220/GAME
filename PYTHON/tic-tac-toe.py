# TIC TAC TOE
import random
ln=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def board():
    print(ln[0],"|",ln[1],"|", ln [2])
    print("---------")
    print(ln[3],"|",ln[4],"|",ln[5])
    print("---------")
    print(ln [6],"|",ln[7],"|",ln[8])
def win(w):
    if w==pc:
        print("PLAYER WIN")
    elif w==cc:
        print("COMPUTER WIN")
pc=input("O/X:")
if pc=="O":
    cc="X"
elif pc=="X":
    cc="O"
board()
tw="pt"
lm=["O", "X"]
while len(lm)!=0:
    lm=[]
    for i in ln:
        if i!=("O") and i!=("X"):
            lm.append(i)
    if tw=="ct":
        c=random.choice(lm)
        ln.remove(c)
        ln.insert(c-1,cc)
        tw="pt"
        print("\ncomputer's turn:",c)
    elif tw=="pt":
        c=int(input("\nplayer's turn: "))
        if c in ln:
            ln.remove(c)
            lm.remove(c)
            ln.insert(c-1,pc)
            tw="ct"
        else:
            print("invalid input")
            continue
    board()
    if (ln[0]==ln[1]==ln[2]) or (ln[0]==ln[3]==ln[6]):
        win(ln[0])
        break
    elif (ln[6]==ln[7]==ln[8]) or (ln[2]==ln[5]==ln[8]):
        win(ln[8])
        break
    elif (ln[0]==ln[4]==ln[8]) or (ln[2]==ln[4]==ln[6]) or (ln[1]==ln[4]==ln[7]) or (ln[3]==ln[4]==ln[5]):
        win(ln[4])
        break
else:
    print("TIE")