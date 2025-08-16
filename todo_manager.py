

# Stage 1 - Basic setup
import sys

def main():
    print("Welcome to the Dummy TODO Manager")

if __name__ == "__main__":
    main()

# Core placeholders
todo_list = []
MAX_ITEMS = 10

def add_todo(item):
    # Pretend to add an item
    if len(todo_list) < MAX_ITEMS:
        todo_list.append(item)
        print(f"[DEBUG] Added: {item}")
    else:
        print("[DEBUG] List full - cannot add item")

def view_todos():
    # Pretend to show list
    print("[DEBUG] Viewing all todos:")
    for idx, item in enumerate(todo_list, start=1):
        print(f"{idx}. {item}")

def remove_todo(index):
    # Pretend to remove item
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"[DEBUG] Removed: {removed}")
    else:
        print("[DEBUG] Invalid index")

def explain_add_todo():
    """
    Explanation:
    This function *pretends* to add items to the todo_list.
    It checks if the number of items is less than MAX_ITEMS
    and appends the new item if allowed.
    Currently, it only prints debug text.
    """
    print("Explanation: add_todo() adds a new entry to the list.")

def explain_view_todos():
    """
    Explanation:
    This function simulates displaying all todos in the list.
    It simply loops through the todo_list and prints them
    with an index number for clarity.
    """
    print("Explanation: view_todos() displays all items in todo_list.")















