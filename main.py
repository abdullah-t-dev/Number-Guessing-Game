import random
n = random.randint(1,100)
a = -1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess The Number"))
    if(a>n):
        print("Lower Number please")
    else:
        print("Higher Number please")
print(f"You guess the Correct number in{guesses}attempt")