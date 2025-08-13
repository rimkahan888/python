#!/usr/bin/env python3
# Random Quote Generator
# A simple script to display random inspirational quotes

import random
import time

# List of quotes with their authors
QUOTES = [
    {"text": "Be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
]

# Configuration settings
SETTINGS = {
    "delay": 2,  # Seconds between quotes
    "max_display": 5,  # Maximum quotes to display in one session
}

def get_random_quote():
    """Select a random quote from the quotes database
    
    Returns:
        dict: A randomly selected quote dictionary
    """
    return random.choice(QUOTES)

def get_user_input():
    """Get user input for quote generator options
    
    Returns:
        str: User's choice of action
    """
    print("\nOptions:")
    print("1. Show another quote")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
    return choice

# Update main function to include user interaction
def main():
    """Main function to run the quote generator"""
    print("Welcome to the Random Quote Generator!")
    
    running = True
    while running:
        # Display a random quote
        quote = get_random_quote()
        display_quote(quote)
        
        # Get user input
        choice = get_user_input()
        if choice == "2":
            running = False

def display_quote(quote):
    """Display a formatted quote with its author
    
    Args:
        quote (dict): A dictionary containing 'text' and 'author' keys
    """
    print("\n╔═════════════════════════════════════════════╗")
    print(f"║ \"{quote['text']}\" ║")
    print(f"║ - {quote['author']} ║")
    print("╚═════════════════════════════════════════════╝\n")
    time.sleep(SETTINGS["delay"])  # Pause between quotes

if __name__ == "__main__":
    main()