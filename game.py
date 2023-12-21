import random
# snake water gun conditions
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

# computer choosing
print("comp turn: snake(s) water(w) gun(g)")
randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

# user choosing
you = input("your turn, choose: ")
a = gamewin(comp, you)

# printing choices
print(f"computer chose {comp}")
print(f"you chose {you}")

# result of the game
if a is None:
    print("It's a draw!")
elif a is False:
    print("You lost!")
else :
    print("You won!")

        
        

        
        
         
    