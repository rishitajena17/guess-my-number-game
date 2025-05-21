import random
secret_number = random.randint(1, 100)

print("I am thinking of a number between 1 and 99.")
guess = int(input("Take a guess: "))
while guess != secret_number:
    if guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    print(" ")
    guess = int(input("Take a new guess: "))


print(f"Congrats! the number was {secret_number}.")
print("Thanks for playing!")
