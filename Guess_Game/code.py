# import random 
# n = random.randint(1,100)
# a = 0
# guesses = 0
# while (a != n):
#     guesses = guesses + 1
#     a = int(input("Enter the number: "))
#     if(a>n):
#         print("Lower number please")
#     else:
#         print("Higher number please")

# print(f"Congratulation you have guessed {n} correctly in {guesses} attempts")      
# 
import random

n = random.randint(1, 100)
guesses = 0
a = int(input("Enter the number: "))


for _ in range(100):  # Assuming a maximum of 100 attempts
     guesses += 1
     if a == n:
        print(f"Congratulations! You have guessed {n} correctly in {guesses} attempts")
        break
     elif a > n:
        print("Lower number please")
     else:
        print("Higher number please")
      


