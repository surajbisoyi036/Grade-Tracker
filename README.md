# Student Grade Calculator (CLI)

A robust, menu-driven command-line application written in Python that allows users to calculate student grades, generate percentage summaries, and maintain a persistent history of report cards.

# Features

Interactive Menu System: Clean and easy-to-navigate command-line interface.

Input Validation: Ensures user inputs are valid numbers between 0 and 100, preventing program crashes due to typos.

Automatic Calculation: Instantly computes total marks, percentages, and assigns letter grades based on a predefined scale.

Data Persistence: Saves student reports to a local text file (report_card.txt) with a timestamp.

History Viewer: Allows users to view a log of all previously saved report cards directly from the application.

Cross-Platform: Includes a screen clearing function that works on both Windows (cls) and Unix/Linux/macOS (clear) systems.

# Prerequisites

Python 3.x installed on the machine.

No external libraries are required (uses standard os, sys, and datetime modules).

# How to Run

Save the code: Save the provided Python script to a file named grade_calculator.py.

Open Terminal/Command Prompt: Navigate to the folder where you saved the file.

Execute the script:

python grade_calculator.py


# Usage Guide

Upon running the program, you will be presented with the main menu:

===============================
 STUDENT GRADE CALCULATOR
===============================
1. New Calculation
2. View History
3. Exit
===============================


1. New Calculation

Select option 1 to enter a new student record.

Enter the Student Name.

Enter marks (0-100) for the following subjects:

Maths

Physics

Chemistry

English

CS

The program will display the Total, Percentage, and Grade.

You will be asked if you want to Save to file? (y/n). Entering 'y' appends the record to report_card.txt.

2. View History

Select option 2 to read from the local storage.

This displays all records saved in report_card.txt.

If no file exists yet, it will notify you that no reports are found.

# Grading Logic

The application uses the following percentage ranges to determine the final grade:

Percentage Range

Grade

90% - 100%

A+

80% - 89.99%

A

70% - 79.99%

B

60% - 69.99%

C

50% - 59.99%

D

Below 50%

Fail

# Project Structure

.
├── grade_calculator.py    # The main application script
└── report_card.txt        # Generated file storing student history


# Example Output format

When saving to the history file, entries are formatted as follows:
YYYY-MM-DD HH:MM:SS | Student Name | Total: 450.0 | 90.0% | Grade: A+

# Future Improvements

Possible features to add in future versions:

Allow the user to customize the list of subjects.

Add ability to delete specific records from history.

Export data to CSV format.
