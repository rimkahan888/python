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






















