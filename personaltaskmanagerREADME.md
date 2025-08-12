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

### Priority System

- **High**: Urgent or important tasks
- **Medium**: Regular tasks (default)
- **Low**: Nice-to-have or low-priority items

## 6. Data Storage

### File Structure

- **Primary Data**: `tasks.json` - Main task storage file
- **Backups**: `tasks_backup_YYYYMMDD_HHMMSS.json` - Timestamped backups

### Data Format

Tasks are stored in JSON format with the following structure:

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Sample Task",
      "description": "Task description",
      "priority": "medium",
      "status": "pending",
      "created_date": "2024-01-01T10:00:00",
      "completed_date": null
    }
  ],
  "next_task_id": 2,
  "last_saved": "2024-01-01T10:00:00"
}
```

### Automatic Features

- **Auto-save**: Tasks are automatically loaded on startup
- **Data Validation**: Input validation prevents data corruption
- **Error Handling**: Graceful handling of file I/O errors

## 7. Advanced Features

### Search Functionality

- Search through task titles and descriptions
- Case-insensitive matching
- Partial word matching supported
- Results displayed in standard task table format

### Statistics Dashboard

View comprehensive analytics including:

- Total task count
- Completion rate percentage
- Status distribution (pending/in-progress/completed)
- Priority distribution (high/medium/low)

### Backup System

- Manual backup creation with timestamps
- Backup files include all task data and metadata
- Useful for data recovery and archiving

### Bulk Operations

- Clear all completed tasks at once
- Confirmation prompts for destructive operations
- Batch status updates possible through menu navigation

## 8. Error Handling & Safety

### Input Validation

- Required field validation (task titles cannot be empty)
- Type checking for numeric inputs (task IDs)
- Priority and status validation against allowed values
- Graceful handling of invalid menu choices

### Data Safety

- Confirmation prompts for destructive operations (delete, clear)
- Automatic backup suggestions before exit
- Error recovery for corrupted data files
- Keyboard interrupt handling (Ctrl+C)

### User Experience

- Clear success/error messages with ✓/✗ indicators
- Helpful prompts and input guidance
- "Press Enter to continue" pauses for readability
- Consistent menu navigation

## 9. Technical Details

### Architecture

- **Object-Oriented Design**: Task class with methods for serialization
- **Modular Functions**: Separate functions for each operation
- **Global State Management**: Task list and ID counter management
- **Error Boundaries**: Try-catch blocks around critical operations

### Dependencies

- `json`: Data serialization and storage
- `os`: File system operations
- `datetime`: Timestamp management
- `sys`: System operations and exit handling

### Code Structure

- **Constants**: Application name, version, file paths
- **Task Class**: Core data model with serialization methods
- **CRUD Operations**: Create, Read, Update, Delete functions
- **UI Functions**: Menu display and user input handling
- **Data Persistence**: Save/load and backup functions
- **Main Loop**: Application initialization and menu handling

### Performance Considerations

- In-memory task storage for fast operations
- Efficient list comprehensions for filtering
- Minimal file I/O operations
- Lazy loading of task data

## 10. Troubleshooting & Support

### Common Issues

**Problem**: "Permission denied" when saving tasks

- **Solution**: Ensure write permissions in the application directory
- **Alternative**: Run from a directory where you have write access

**Problem**: Tasks not loading on startup

- **Solution**: Check if `tasks.json` exists and is valid JSON
- **Recovery**: Delete corrupted file to start fresh, or restore from backup

**Problem**: Application crashes on startup

- **Solution**: Verify Python 3.6+ is installed
- **Check**: Ensure all required files are present

### Data Recovery

1. **From Backup**: Rename a backup file to `tasks.json`
2. **Manual Recovery**: Edit `tasks.json` to fix JSON syntax errors
3. **Fresh Start**: Delete `tasks.json` to start with empty task list

### Best Practices

- **Regular Backups**: Use option 14 to create backups periodically
- **Descriptive Titles**: Use clear, actionable task titles
- **Priority Management**: Regularly review and adjust task priorities
- **Status Updates**: Keep task statuses current for accurate statistics

### Getting Help

- Check error messages for specific guidance
- Verify file permissions and disk space
- Ensure Python version compatibility
- Review this README for feature explanations

### Future Enhancements

Potential improvements for future versions:

- Due date support with reminders
- Task categories and tags
- Export to different formats (CSV, PDF)
- Multi-user support
- Web interface option
- Integration with calendar applications

---

**Version**: 1.0.0  
**Author**: Your Name  
**License**: See LICENSE file  
**Last Updated**: 2024
