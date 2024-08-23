import random 
n = random.randint(1,100)
a = 0
guesses = 0
while (a != n):
    guesses = guesses + 1
    a = int(input("Enter the number: "))
    if(a>n):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"Congratulation you have guessed {n} correctly in {guesses} attempts")      




