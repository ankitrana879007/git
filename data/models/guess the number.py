import random                       #random is used to make computer take random number
comp = random.randint(1,50)         #randint help to set a specific limit

chance = 1
while chance <= 10:
    user = int(input("Guess the number:"))
    print()

    if user == comp:
        print("-----You won-----")
        print(f"Your score:{110 - (chance * 10)}")      #think and understand 
        break
    elif user < comp:
        print('Hint: Guess Higher Number')
        print(f"<------[Chances Left: {10 - chance}]------>")

    elif user > comp:
        print("Hint:Guess Lower Number")
        print(f"<------[Chances Left: {10 - chance}]------>")

    chance += 1
else:
    print("------You Lose-----")
    print(f'Random Number:{comp}')

print('|------Game Over------|')

