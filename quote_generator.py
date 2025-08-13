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

# Quote Formatting Explanation
"""
Quote Formatting Details:

The display_quote function creates a visually appealing box around each quote
using Unicode box-drawing characters. This enhances readability and gives the
quotes a more professional appearance.

Box characters used:
- ╔, ╗, ╚, ╝: Corner characters
- ═: Horizontal line
- ║: Vertical line

The function also adds proper spacing and attribution to the author.
A time delay is implemented after displaying each quote to give the user
time to read before showing the next option or quote.

Future enhancements could include:
- Dynamic box sizing based on quote length
- Color coding using ANSI escape sequences
- Different box styles for different quote categories
"""
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

# Quote Selection Explanation
"""
Quote Selection System:

The get_random_quote function uses Python's random module to select quotes
from the QUOTES database. The current implementation uses random.choice(),
which gives each quote an equal probability of being selected.

Potential improvements:
1. Weighted selection based on quote popularity or relevance
2. Tracking previously shown quotes to avoid repetition
3. Categorization of quotes for themed selections
4. Loading quotes from external sources (files, APIs)
5. Allowing users to add their own quotes

The function is designed to be modular, making it easy to replace with
more sophisticated selection algorithms in the future without affecting
other parts of the application.
"""
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

# User Interaction Explanation
"""
User Interaction System:

The get_user_input function provides a simple menu interface for users
to interact with the quote generator. It displays numbered options and
accepts user input to determine the next action.

The main function uses this input in a loop to either continue showing
quotes or exit the program based on user choice.

Possible enhancements:
1. Adding more options (save quote, share quote, etc.)
2. Input validation to handle invalid entries
3. Command-line arguments for batch operation
4. A more sophisticated menu system with submenus
5. GUI interface as an alternative to command-line

The current implementation follows a simple event loop pattern:
1. Display information (quote)
2. Get user input
3. Process input and determine next action
4. Repeat or exit
"""

# Error handling implementation

def safe_get_random_quote():
    """Safely get a random quote with error handling
    
    Returns:
        dict: A randomly selected quote dictionary or a default quote on error
    """
    try:
        if not QUOTES:  # Check if quotes list is empty
            raise ValueError("Quotes database is empty")
        return random.choice(QUOTES)
    except Exception as e:
        print(f"Error selecting quote: {e}")
        # Return a default quote if there's an error
        return {"text": "Error occurred, but life goes on.", "author": "Anonymous"}

def safe_get_user_input():
    """Safely get user input with error handling
    
    Returns:
        str: Validated user choice
    """
    while True:
        try:
            print("\nOptions:")
            print("1. Show another quote")
            print("2. Exit")
            
            choice = input("Enter your choice (1-2): ")
            if choice not in ["1", "2"]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            return choice
        except Exception as e:
            print(f"Error: {e}")
            # Continue the loop to ask again

if __name__ == "__main__":
    main()