

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


















