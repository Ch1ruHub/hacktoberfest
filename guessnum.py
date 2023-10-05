import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of attempts
    attempts = 0
    max_attempts = 10
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            
            # Increment the attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")
                
            # Check if the player has run out of attempts
            if attempts == max_attempts:
                print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
if __name__ == "__main__":
    guess_the_number()
