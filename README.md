Student Tracker v6 (CLI Application)
Overview

Student Tracker v6 is a command-line Python application designed to manage, analyze, and track student academic performance over time.
The project focuses on clean structure, modular design, defensive programming, and data persistence.

This version represents a major refactor and architectural improvement over previous versions, introducing object-oriented concepts, modular separation of concerns, and historical progress tracking.

Features

Add and store student data (subjects and scores)

Calculate:

Average score per student

Grade per student

Class average and class grade

Number of subjects per student

Identify:

Top-performing student

Lowest-performing student

Top 3 students

Failed vs successful students

Search for a student and display their data

Track a student’s academic progress over time

Persistent storage using JSON with timestamped history

Defensive handling of missing data and edge cases

Project Structure
student_tracker_v6/
│
├── main.py                  # Application entry point and menu loop
├── input_students_data.py   # User input handling and validation
├── calculations_oop.py      # Core calculations and analysis logic
├── tools.py                 # Search, progress tracking, and utilities
├── data_handling.py         # Load/save JSON data with history
├── student_class_oop.py     # Student class (OOP model)
├── students.json            # Persistent data storage
└── README.md

Design Approach

Modular architecture
Each responsibility is separated into its own module (input, calculations, tools, persistence).

Object-Oriented Design
Student data is represented using a Student class, allowing cleaner logic and future extensibility.

Defensive Programming

Handles empty datasets safely

Prevents crashes when insufficient data exists (e.g., fewer than 3 students)

Uses control flow (continue vs break) intentionally to preserve application flow

Versioned Improvement
This version builds on earlier procedural implementations and refactors them into a scalable and maintainable design.

How Data Persistence Works

Student data is saved to a JSON file

Each save operation is stored under a timestamp

This allows historical analysis of a student’s progress over time

Progress tracking reuses existing calculation logic to maintain consistency

How to Run

Ensure Python 3.10+ is installed

Clone or download the repository

Run:

python main.py


Use the menu to interact with the application

What This Project Demonstrates

Strong understanding of Python fundamentals

Practical use of OOP in a CLI environment

Logical problem-solving and data modeling

Clean refactoring from older versions

Real-world handling of user input and edge cases

Code written with maintainability and extensibility in mind

Future Improvements

Enhanced input validation

Export reports (CSV / TXT)

Improved grading system

Unit tests

Transition to a database backend

Author

Amine Mustapha
Python CLI Application Project
