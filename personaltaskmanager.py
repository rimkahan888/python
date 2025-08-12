#!/usr/bin/env python3
"""
Personal Task Manager
A simple command-line application for managing personal tasks
Author: Your Name
Date: 2024
"""

import json
import os
from datetime import datetime, date
import sys

# Application constants
APP_NAME = "Personal Task Manager"
VERSION = "1.0.0"
DATA_FILE = "tasks.json"

# ... existing code ...

# Global variables
tasks = []
next_task_id = 1

# Task status constants
STATUS_PENDING = "pending"
STATUS_COMPLETED = "completed"
STATUS_IN_PROGRESS = "in_progress"

class Task:
    """Represents a single task with all its properties"""
    
    def __init__(self, title, description="", priority="medium"):
        global next_task_id
        self.id = next_task_id
        next_task_id += 1
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high
        self.status = STATUS_PENDING
        self.created_date = datetime.now().isoformat()
        self.completed_date = None
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_date': self.created_date,
            'completed_date': self.completed_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        task = cls(data['title'], data['description'], data['priority'])
        task.id = data['id']
        task.status = data['status']
        task.created_date = data['created_date']
        task.completed_date = data['completed_date']
        return task

    # ... existing code ...

def add_task(title, description="", priority="medium"):
    """Add a new task to the task list"""
    global next_task_id
    
    if not title.strip():
        return False, "Task title cannot be empty"
    
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
    
    new_task = Task(title.strip(), description.strip(), priority)
    tasks.append(new_task)
    
    return True, f"Task '{title}' added successfully with ID {new_task.id}"

def get_task_by_id(task_id):
    """Find and return a task by its ID"""
    for task in tasks:
        if task.id == task_id:
            return task
    return None

# ... existing code ...

def list_tasks(status_filter=None, priority_filter=None):
    """List all tasks with optional filtering"""
    filtered_tasks = tasks
    
    if status_filter:
        filtered_tasks = [t for t in filtered_tasks if t.status == status_filter]
    
    if priority_filter:
        filtered_tasks = [t for t in filtered_tasks if t.priority == priority_filter]
    
    return filtered_tasks

def display_tasks(task_list=None):
    """Display tasks in a formatted table"""
    if task_list is None:
        task_list = tasks
    
    if not task_list:
        print("No tasks found.")
        return
    
    print(f"\n{'ID':<4} {'Title':<25} {'Priority':<10} {'Status':<12} {'Created':<12}")
    print("-" * 70)
    
    for task in task_list:
        created_date = datetime.fromisoformat(task.created_date).strftime("%Y-%m-%d")
        print(f"{task.id:<4} {task.title[:24]:<25} {task.priority:<10} {task.status:<12} {created_date:<12}")
        
        if task.description:
            print(f"     Description: {task.description[:50]}{'...' if len(task.description) > 50 else ''}")
    print()

def display_task_details(task_id):
    """Display detailed information about a specific task"""
    task = get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    
    print(f"\n--- Task Details ---")
    print(f"ID: {task.id}")
    print(f"Title: {task.title}")
    print(f"Description: {task.description or 'No description'}")
    print(f"Priority: {task.priority}")
    print(f"Status: {task.status}")
    print(f"Created: {datetime.fromisoformat(task.created_date).strftime('%Y-%m-%d %H:%M:%S')}")
    if task.completed_date:
        print(f"Completed: {datetime.fromisoformat(task.completed_date).strftime('%Y-%m-%d %H:%M:%S'
        
    # ... existing code ...

def update_task_status(task_id, new_status):
    """Update the status of a task"""
    valid_statuses = [STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_COMPLETED]
    
    if new_status not in valid_statuses:
        return False, f"Invalid status. Valid options: {', '.join(valid_statuses)}"
    
    task = get_task_by_id(task_id)
    if not task:
        return False, f"Task with ID {task_id} not found"
    
    old_status = task.status
    task.status = new_status
    
    if new_status == STATUS_COMPLETED and old_status != STATUS_COMPLETED:
        task.completed_date = datetime.now().isoformat()
    elif new_status != STATUS_COMPLETED:
        task.completed_date = None
    
    return True, f"Task {task_id} status updated from '{old_status}' to '{new_status}'"

def complete_task(task_id):
    """Mark a task as completed"""
    return update_task_status(task_id, STATUS_COMPLETED)

def delete_task(task_id):
    """Delete a task from the list"""
    global tasks
    task = get_task_by_id(task_id)
    
    if not task:
        return False, f"Task with ID {task_id} not found"
    
    tasks = [t for t in tasks if t.id != task_id]
    return True, f"Task '{task.title}' (ID: {task_id}) deleted successfully"

def edit_task(task_id, new_title=None, new_description=None, new_priority=None):
    """Edit task properties"""
    task = get_task_by_id(task_id)
    
    if not task:
        return False, f"Task with ID {task_id} not found"
    
    changes = []
    
    if new_title and new_title.strip():
        task.title = new_title.strip()
        changes.append("title")
    
    if new_description is not None:
        task.description = new_description.strip()
        changes.append("description")
    
    if new_priority and new_priority in ["low", "medium", "high"]:
        task.priority = new_priority
        changes.append("priority")
    
    if changes:
        return True, f"Task {task_id} updated: {', '.join(changes)}"
    else:
        return False, "No valid changes provided"

# ... existing code ...

def get_task_statistics():
    """Get statistics about tasks"""
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.status == STATUS_COMPLETED])
    pending_tasks = len([t for t in tasks if t.status == STATUS_PENDING])
    in_progress_tasks = len([t for t in tasks if t.status == STATUS_IN_PROGRESS])
    
    priority_counts = {
        "high": len([t for t in tasks if t.priority == "high"]),
        "medium": len([t for t in tasks if t.priority == "medium"]),
        "low": len([t for t in tasks if t.priority == "low"])
    }
    
    return {
        "total": total_tasks,
        "completed": completed_tasks,
        "pending": pending_tasks,
        "in_progress": in_progress_tasks,
        "priority_counts": priority_counts,
        "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    }

def display_statistics():
    """Display task statistics in a formatted way"""
    stats = get_task_statistics()
    
    print("\n--- Task Statistics ---")
    print(f"Total Tasks: {stats['total']}")
    print(f"Completed: {stats['completed']}")
    print(f"In Progress: {stats['in_progress']}")
    print(f"Pending: {stats['pending']}")
    print(f"Completion Rate: {stats['completion_rate']:.1f}%")
    print("\nPriority Distribution:")
    print(f"  High: {stats['priority_counts']['high']}")
    print(f"  Medium: {stats['priority_counts']['medium']}")
    print(f"  Low: {stats['priority_counts']['low']}")
    print()

def search_tasks(search_term):
    """Search tasks by title or description"""
    search_term = search_term.lower()
    matching_tasks = []
    
    for task in tasks:
        if (search_term in task.title.lower() or 
            search_term in task.description.lower()):
            matching_tasks.append(task)
    
    return matching_tasks

def clear_completed_tasks():
    """Remove all completed tasks"""
    global tasks
    completed_count = len([t for t in tasks if t.status == STATUS_COMPLETED])
    tasks = [t for t in tasks if t.status != STATUS_COMPLETED]
    return completed_count

# ... existing code ...

def save_tasks():
    """Save tasks to JSON file"""
    try:
        data = {
            "tasks": [task.to_dict() for task in tasks],
            "next_task_id": next_task_id,
            "last_saved": datetime.now().isoformat()
        }
        
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        
        return True, f"Tasks saved successfully to {DATA_FILE}"
    
    except Exception as e:
        return False, f"Error saving tasks: {str(e)}"

def load_tasks():
    """Load tasks from JSON file"""
    global tasks, next_task_id
    
    if not os.path.exists(DATA_FILE):
        return True, "No existing data file found. Starting fresh."
    
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        
        tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        next_task_id = data.get("next_task_id", 1)
        
        # Update next_task_id to be higher than any existing task ID
        if tasks:
            max_id = max(task.id for task in tasks)
            next_task_id = max(next_task_id, max_id + 1)
        
        return True, f"Loaded {len(tasks)} tasks from {DATA_FILE}"
    
    except Exception as e:
        return False, f"Error loading tasks: {str(e)}"

def backup_tasks():
    """Create a backup of the current tasks"""
    try:
        backup_filename = f"tasks_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        data = {
            "tasks": [task.to_dict() for task in tasks],
            "next_task_id": next_task_id,
            "backup_created": datetime.now().isoformat()
        }
        
        with open(backup_filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        return True, f"Backup created: {backup_filename}"
    
    except Exception as e:
        return False, f"Error creating backup: {str(e)}"

# ... existing code ...

def display_menu():
    """Display the main menu options"""
    print(f"\n=== {APP_NAME} v{VERSION} ===")
    print("1.  Add new task")
    print("2.  List all tasks")
    print("3.  List tasks by status")
    print("4.  List tasks by priority")
    print("5.  View task details")
    print("6.  Update task status")
    print("7.  Edit task")
    print("8.  Complete task")
    print("9.  Delete task")
    print("10. Search tasks")
    print("11. View statistics")
    print("12. Clear completed tasks")
    print("13. Save tasks")
    print("14. Create backup")
    print("0.  Exit")
    print("-" * 30)

def get_user_input(prompt, input_type=str, required=True):
    """Get user input with type validation"""
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input and required:
                print("This field is required. Please enter a value.")
                continue
            
            if not user_input and not required:
                return None
            
            if input_type == int:
                return int(user_input)
            elif input_type == str:
                return user_input
            
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def get_priority_input():
    """Get priority input with validation"""
    print("Priority options: low, medium, high")
    while True:
        priority = input("Enter priority (default: medium): ").strip().lower()
        if not priority:
            return "medium"
        if priority in ["low", "medium", "high"]:
            return priority
        print("Invalid priority. Please enter: low, medium, or high")

def get_status_input():
    """Get status input with validation"""
    print(f"Status options: {STATUS_PENDING}, {STATUS_IN_PROGRESS}, {STATUS_COMPLETED}")
    while True:
        status = input("Enter status: ").strip().lower()
        if status in [STATUS_PENDING, STATUS_IN_PROGRESS, STATUS_COMPLETED]:
            return status
        print(f"Invalid status. Please enter: {STATUS_PENDING}, {STATUS_IN_PROGRESS}, or {STATUS_COMPLETED}")

def confirm_action(message):
    """Get user confirmation for destructive actions"""
    response = input(f"{message} (y/N): ").strip().lower()
    return response in ['y', 'yes']

# ... existing code ...

def handle_menu_choice(choice):
    """Handle user menu selection with error handling"""
    try:
        if choice == 1:  # Add new task
            title = get_user_input("Enter task title: ")
            if title:
                description = get_user_input("Enter task description (optional): ", required=False) or ""
                priority = get_priority_input()
                success, message = add_task(title, description, priority)
                print(f"\n{'✓' if success else '✗'} {message}")
        
        elif choice == 2:  # List all tasks
            display_tasks()
        
        elif choice == 3:  # List by status
            status = get_status_input()
            filtered_tasks = list_tasks(status_filter=status)
            print(f"\nTasks with status '{status}':")
            display_tasks(filtered_tasks)
        
        elif choice == 4:  # List by priority
            priority = get_priority_input()
            filtered_tasks = list_tasks(priority_filter=priority)
            print(f"\nTasks with priority '{priority}':")
            display_tasks(filtered_tasks)
        
        elif choice == 5:  # View task details
            task_id = get_user_input("Enter task ID: ", int)
            if task_id:
                display_task_details(task_id)
        
        elif choice == 6:  # Update task status
            task_id = get_user_input("Enter task ID: ", int)
            if task_id:
                new_status = get_status_input()
                success, message = update_task_status(task_id, new_status)
                print(f"\n{'✓' if success else '✗'} {message}")
        
        elif choice == 7:  # Edit task
            task_id = get_user_input("Enter task ID: ", int)
            if task_id:
                task = get_task_by_id(task_id)
                if task:
                    print(f"\nCurrent task: {task.title}")
                    new_title = get_user_input("Enter new title (press Enter to keep current): ", required=False)
                    new_description = get_user_input("Enter new description (press Enter to keep current): ", required=False)
                    print("Enter new priority (press Enter to keep current):")
                    new_priority = get_user_input("Priority: ", required=False)
                    
                    success, message = edit_task(task_id, new_title, new_description, new_priority)
                    print(f"\n{'✓' if success else '✗'} {message}")
                else:
                    print(f"\n✗ Task with ID {task_id} not found")
        
        elif choice == 8:  # Complete task
            task_id = get_user_input("Enter task ID to complete: ", int)
            if task_id:
                success, message = complete_task(task_id)
                print(f"\n{'✓' if success else '✗'} {message}")
        
        elif choice == 9:  # Delete task
            task_id = get_user_input("Enter task ID to delete: ", int)
            if task_id:
                task = get_task_by_id(task_id)
                if task and confirm_action(f"Delete task '{task.title}'?"):
                    success, message = delete_task(task_id)
                    print(f"\n{'✓' if success else '✗'} {message}")
                elif task:
                    print("\n✗ Deletion cancelled")
        
        elif choice == 10:  # Search tasks
            search_term = get_user_input("Enter search term: ")
            if search_term:
                results = search_tasks(search_term)
                print(f"\nSearch results for '{search_term}':")
                display_tasks(results)
        
        elif choice == 11:  # View statistics
            display_statistics()
        
        elif choice == 12:  # Clear completed tasks
            if confirm_action("Clear all completed tasks?"):
                count = clear_completed_tasks()
                print(f"\n✓ Cleared {count} completed tasks")
            else:
                print("\n✗ Operation cancelled")
        
        elif choice == 13:  # Save tasks
            success, message = save_tasks()
            print(f"\n{'✓' if success else '✗'} {message}")
        
        elif choice == 14:  # Create backup
            success, message = backup_tasks()
            print(f"\n{'✓' if success else '✗'} {message}")
        
        elif choice == 0:  # Exit
            if confirm_action("Save tasks before exiting?"):
                save_tasks()
            print("\nGoodbye! 👋")
            return False
        
        else:
            print("\n✗ Invalid choice. Please select a number from the menu.")
    
    except KeyboardInterrupt:
        print("\n\nOperation interrupted. Returning to menu...")
    except Exception as e:
        print(f"\n✗ An unexpected error occurred: {str(e)}")
        print("Please try again or contact support if the problem persists.")
    
    return True

# ... existing code ...

def initialize_application():
    """Initialize the application and load existing data"""
    print(f"Initializing {APP_NAME}...")
    
    # Load existing tasks
    success, message = load_tasks()
    print(message)
    
    if not success:
        print("Warning: Could not load existing tasks. Starting with empty task list.")
    
    return True

def main():
    """Main program loop"""
    try:
        # Initialize application
        if not initialize_application():
            print("Failed to initialize application. Exiting.")
            sys.exit(1)
        
        print(f"\nWelcome to {APP_NAME}!")
        
        # Main program loop
        while True:
            try:
                display_menu()
                choice = get_user_input("Enter your choice (0-14): ", int)
                
                if choice is None:  # User cancelled input
                    continue
                
                # Handle the menu choice
                continue_running = handle_menu_choice(choice)
                
                if not continue_running:
                    break
                
                # Pause before showing menu again
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\nExiting application...")
                if confirm_action("Save tasks before exiting?"):
                    save_tasks()
                break
            except EOFError:
                print("\n\nEnd of input detected. Exiting...")
                break
    
    except Exception as e:
        print(f"\nCritical error: {str(e)}")
        print("The application will now exit.")
        sys.exit(1)
    
    finally:
        print("\nThank you for using Personal Task Manager!")

if __name__ == "__main__":
    main()