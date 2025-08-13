# Random Quote Generator

A simple Python script that displays random inspirational quotes with a clean, formatted interface.

## Overview

This project provides a command-line quote generator that displays random inspirational quotes from famous individuals. It's designed to be simple, modular, and easy to extend.

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library modules)

## Installation

1. Clone this repository or download the script file
2. Ensure you have Python 3.6+ installed
3. Make the script executable (optional):
   ```bash
   chmod +x quote_generator.py
   ```

## Features

- Display random inspirational quotes with attribution
- Clean, formatted output with decorative borders
- Simple user interface for viewing multiple quotes
- Error handling for robust operation
- Data validation to ensure quote integrity

## Usage

When you run the program, it will:

1. Display a welcome message
2. Show a random quote in a formatted box
3. Present options to view another quote or exit
4. Continue showing quotes until you choose to exit

Example interaction:

```bash
python quote_generator.py
```

Or if you made it executable:

```bash
./quote_generator.py
```

## Project Structure

The script is organized into several functional components:

1. **Core Data Structures**:

   - Quote database (list of dictionaries with text and author)
   - Configuration settings (delay time, max quotes)

2. **Display Functions**:

   - `display_quote()`: Formats and displays a quote in a decorative box
   - Includes proper spacing and attribution

3. **Quote Selection**:

   - `get_random_quote()`: Selects a random quote from the database
   - `safe_get_random_quote()`: Adds error handling to quote selection

4. **User Interaction**:

   - `get_user_input()`: Displays options and processes user choices
   - `safe_get_user_input()`: Adds validation to user input processing

5. **Validation**:
   - `validate_quote_format()`: Ensures quotes have the correct structure

## Customization

You can easily customize the script by:

1. **Adding More Quotes**:

   - Edit the `QUOTES` list to add your own inspirational quotes
   - Each quote should be a dictionary with 'text' and 'author' keys

2. **Changing Display Settings**:
   - Modify the `SETTINGS` dictionary to change the delay time or max quotes
   - Adjust the box formatting in the `display_quote()` function

## Future Enhancements

Potential improvements for future versions:

- Loading quotes from external files (JSON, CSV, etc.)
- Categories for quotes (inspirational, funny, philosophical, etc.)
- Color-coded output using ANSI escape sequences
- Web API integration to fetch quotes online
- User ability to add, save, and rate quotes
- GUI interface as an alternative to command-line

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
