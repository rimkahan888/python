# Stage 1 - Basic setup
import random

def main():
    print("Welcome to Guess the Number Game")

if __name__ == "__main__":
    main()

# Core game data
TARGET_NUMBER = None
MAX_ATTEMPTS = 5
attempts_made = 0

def generate_target_number():
    # Placeholder function to set target number
    global TARGET_NUMBER
    TARGET_NUMBER = random.randint(1, 10)
    print("[DEBUG] Target number generated")

def get_user_guess():
    # Placeholder for user input
    print("[DEBUG] Asking user for guess")
    guess = 5  # dummy value for now
    print(f"[DEBUG] User guessed: {guess}")
    return guess





















