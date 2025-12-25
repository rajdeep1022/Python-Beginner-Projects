import random
def number_guessing_game():
    secretnum=random.randint(1,100)
    attempts=10
    print("Welcome to Number Guessing Game!!!")
    print(f"\nI select a Numnber between 1-100, can you guess it???\nYou have {attempts} attempts to guess it.")
    print("Are you interested to play the game??")
    ans=input("Share your interest with Yes/No: ")
    Ans=(ans.capitalize())
    if Ans=="No":
        print("OK! Thank you !!")
        return
    elif Ans=="Yes":
        for i in range(attempts):
            guess=int(input(f"\nAttempt {i+1}/{attempts}: Enter your guess: "))
            if guess==secretnum:
                print("\nCongratulation!!!!!!You guessed the correct number")
                break
            elif guess<secretnum:
                print("Too low!! PLease Try Again!!!")
            else:
                print("Too high!! PLease Try Again!!!")
            print(f"Your remaining attempts: {attempts-(i+1)} ")
        else:
             print(f"\nGame Over! You used your all attempts..\n The number was: {secretnum}")
    else:
        print("Invalid response! try again.")
number_guessing_game()