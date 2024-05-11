#это игра по угадыванию чисел
import random

guess_taken = 0

name = input("Hello! What is your name?\n")
print(f"Well {name}, try to guess the hidden number in 6 tries!")

number = random.randint(1, 20)

for guess_taken in range(6):
    guess = int(input("Enter a number betweem 1 and 20:\n"))

    if guess > number:
        print("Your number is too high.")

    if guess < number:
        print("Your number is too low.")

    if guess == number:
        break

if guess == number:
    guess_taken = guess_taken + 1
    print(f"Excellent {name}, you have done it in {guess_taken} tries!")

if guess != number:
    print(f"Oh no, I wished for the number {number}.")