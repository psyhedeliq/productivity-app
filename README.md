# Productivity Timer App

A simple command-line productivity timer that helps you manage your tasks with scheduled time blocks and motivational reminders.

## Features

- Task scheduling with time blocks
- Real-time countdown for current task
- Color-coded time warnings
- Random motivational reminders
- Visual task progress tracking

## Project Structure

```
productivity-app/
├── src/
│   └── productivity.py    # Main application code
├── config/
│   └── task.json         # Task configuration file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config/task.json` to define your tasks and their durations (in minutes):

```json
{
    "Project overview": 1,
    "Core functionalities": 10,
    "Documentation": 10,
    "Current file structure": 7,
    "Additional requirements": 15
}
```

## Usage

Run the application from the project root:

```bash
python src/productivity.py
```

The app will:
- Display your task schedule
- Show remaining time for the current task
- Provide color-coded warnings when time is running low
- Display motivational reminders
- Mark tasks as complete when finished

## Color Coding

- Normal time remaining: Blue background
- Less than 5 minutes: Red background
- Less than 2 minutes: Blinking red background
- Task completed: Green background
