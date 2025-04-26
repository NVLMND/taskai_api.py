# taskai_api.py
# Mood-Based Task Manager API

This project is a **Flask-based API** that allows users to submit sentences and automatically assigns a mood to each sentence based on predefined keywords. It then stores these sentences and moods in a JSON file and allows users to fetch their task data using a unique task ID.

## Features

- **POST /task**: Accepts a sentence, analyzes the mood from predefined keywords (Happy, Sad, Angry), and returns a task ID, mood, and the sentence.
- **GET /task**: Accepts a task ID and returns the task’s mood and sentence.
  
### Available Moods:
- **Happy**: Associated with words like `happy`, `cheerful`, `smiling`, `joyful`, etc.
- **Sad**: Associated with words like `sad`, `depressed`, `unhappy`, `crying`, etc.
- **Angry**: Associated with words like `angry`, `mad`, `furious`, `irritated`, etc.
- **Unknown**: If no keywords match.

## Installation

To run this project locally, follow these steps:

### 1. Clone this repository:
```bash
git clone https://github.com/your-username/mood-based-task-manager.git
cd mood-based-task-manager
