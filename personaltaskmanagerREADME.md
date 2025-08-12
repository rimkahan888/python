# Personal Task Manager

A simple yet powerful command-line application for managing personal tasks with persistent storage and comprehensive task management features.

## 1. Project Overview

The Personal Task Manager is a Python-based command-line application designed to help users organize and track their personal tasks efficiently. Built with simplicity and functionality in mind, it provides a clean interface for task management without the complexity of web-based solutions.

**Key Highlights:**

- Version: 1.0.0
- Pure Python implementation
- JSON-based data persistence
- Interactive command-line interface
- Comprehensive task management capabilities

## 2. Features

### Core Task Management

- ✅ **Add Tasks**: Create new tasks with title, description, and priority
- 📋 **List Tasks**: View all tasks or filter by status/priority
- 🔍 **Search Tasks**: Find tasks by title or description
- ✏️ **Edit Tasks**: Modify task properties (title, description, priority)
- 🗑️ **Delete Tasks**: Remove unwanted tasks with confirmation
- ✅ **Complete Tasks**: Mark tasks as completed with timestamp

### Advanced Features

- 📊 **Statistics**: View task completion rates and priority distribution
- 🔄 **Status Management**: Track tasks through pending, in-progress, and completed states
- 🎯 **Priority Levels**: Organize tasks by low, medium, and high priority
- 💾 **Data Persistence**: Automatic saving and loading of tasks
- 🔒 **Backup System**: Create timestamped backups of your task data
- 🧹 **Cleanup Tools**: Clear completed tasks in bulk

## 3. Installation

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only standard library)

### Setup Steps

1. **Clone or Download**: Get the project files to your local machine

   ```bash
   git clone <repository-url>
   cd personal-task-manager
   ```

2. **Verify Python Installation**:

   ```bash
   python3 --version
   ```

3. **Make Script Executable** (Optional on Unix-like systems):
   ```bash
   chmod +x personaltaskmanager.py
   ```

## 4. Usage Guide

### Starting the Application

```bash
python3 personaltaskmanager.py
```

### Menu Navigation

The application presents a numbered menu (0-14) with the following options:

1. **Add new task** - Create a new task
2. **List all tasks** - Display all tasks in table format
3. **List tasks by status** - Filter tasks by pending/in-progress/completed
4. **List tasks by priority** - Filter tasks by low/medium/high priority
5. **View task details** - Show detailed information for a specific task
6. **Update task status** - Change task status
7. **Edit task** - Modify task properties
8. **Complete task** - Mark task as completed
9. **Delete task** - Remove a task (with confirmation)
10. **Search tasks** - Find tasks by keyword
11. **View statistics** - Display task analytics
12. **Clear completed tasks** - Remove all completed tasks
13. **Save tasks** - Manually save data to file
14. **Create backup** - Generate timestamped backup
15. **Exit** - Close application (with save prompt)

### Basic Workflow Example

1. Start the application
2. Choose option 1 to add a new task
3. Enter task title, description, and priority
4. Use option 2 to view your tasks
5. Use option 6 to update task status as you work
6. Use option 8 to mark tasks as completed

## 5. Task Management System

### Task Properties

Each task contains the following information:

- **ID**: Unique identifier (auto-generated)
- **Title**: Task name (required)
- **Description**: Detailed task information (optional)
- **Priority**: low, medium, or high (default: medium)
- **Status**: pending, in_progress, or completed
- **Created Date**: Timestamp of task creation
- **Completed Date**: Timestamp when task was completed (if applicable)

### Status Workflow
