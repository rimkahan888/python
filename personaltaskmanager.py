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