# Employee Management Project

A small command-line application for managing employee records. It is intended as a beginner-friendly example of a Python program split into a service layer (the employee operations) and a command-line interface.

## Features

- Add an employee with an ID, name, and department.
- List all employees.
- Search employees by ID or name, without regard to capitalization.
- List employees in a department, without regard to capitalization.
- Change an employee's department.
- Delete an employee.
- Reject blank required fields and duplicate employee IDs.

## Requirements

- Python 3
- No third-party packages are required; the application uses Python's standard library.

## Run the application

From the project directory, run:

```sh
python app.py
```

Use the numbered menu to choose an operation. Employee records are held in memory while the program runs. They are cleared when the application exits.

## Run the tests

From the project directory, run:

```sh
python -m unittest -v
```

## Limitations

- Employee data is stored only in memory and is not saved between runs.
- This is a single-user command-line application; it has no authentication or access controls.
- The application validates required text fields and duplicate IDs, but does not enforce a specific ID format or department list.
- Search matches employee IDs and names; department filtering is a separate operation.

This project is used to demonstrate Git and CI/CD.
