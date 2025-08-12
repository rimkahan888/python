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