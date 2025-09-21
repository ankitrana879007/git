import random
print("<------Welcome to Rock - Paper - Scissor Game!------>")
print() # make space by entering nothing
print("Choice: Rock, Paper, Scissor")
print()
Player = 0
Computer = 0
while True:
    user = input("Enter your choice (or 'Exit' for quit):  ").lower()
    if user == 'exit':
        print("Thanks for playing, Goodbye")
        break
    if user not in ['rock','paper','scissor']:
        print("Invalid Choice! Try again.")
        print()
        continue
    comp = random.choice(['rock','paper','scissor'])
    print(f"Computer Chose:{comp}")
    if user == comp:
        print("It's a Draw!")
        print()
    elif(user =='rock' and comp == 'scissor') or (user =='paper' and comp =='stone') or (user =='scissor' and comp =='paper'):
        print("<----You Win---->")
        print()
        Player += 1
    else:
        print("<-----You Lose----->")
        Computer += 1
    print()

print(f"Player Score: {Player}")
print(f"Computer Score: {Computer}")