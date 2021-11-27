
#rockpaperscissors
import random
def rps():
    usrinp=input("select something you worthless shank \n'r' for rock,'p' for paper ,'s' for scissors ")
    comp= random.choice(['r','p','s'])

    if usrinp==comp:
        return "its a tie kiddo"
    if wins(usrinp,comp):
        return "player wins"     
    if wins(comp,usrinp):
        return "you suck computer wins"        
def  wins(player,opponent):   #player wins
    if (player=='s' and opponent=='p') or (player=='r'and opponent=='s') or (player=='p'and opponent=='r'):
        return True

print(rps())

