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

# Update main function to use the new functions
def main():
    """Main function to run the quote generator"""
    print("Welcome to the Random Quote Generator!")
    
    # Display a random quote
    quote = get_random_quote()
    display_quote(quote)

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