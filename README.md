# alu-AirBnB_clone
Entreprise web development

# AirBnB Clone - The Console

## Description

This project is the first part of the AirBnB Clone application. It focuses on building a command-line interpreter that allows users to create, view, update, and delete objects.

The application uses Python object-oriented programming to represent different parts of an accommodation booking system, including users, places, cities, states, amenities, and reviews.

It also includes a file storage system that saves objects in JSON format, allowing data to be loaded again when the application is restarted.

## Command Interpreter

The command interpreter provides a simple way to interact with the application through a terminal. It accepts commands that manage the objects stored in the system.

### How to Start It

Clone the project repository and navigate to the project directory. Start the command interpreter using:

```bash
./console.py
```

The application displays the following prompt:

```text
(hbnb)
```

### How to Use It

The command interpreter supports the following commands:

- `help`: Displays available commands and their descriptions.
- `quit`: Exits the command interpreter.
- `EOF`: Exits the command interpreter.
- `create`: Creates a new instance of a specified class.
- `show`: Displays the details of an existing instance.
- `destroy`: Deletes an existing instance.
- `all`: Displays all instances or instances of a specified class.
- `update`: Updates an attribute of an existing instance.

### Examples

Start the console:

```bash
./console.py
```

Create a user:

```text
(hbnb) create User
```

Display all users:

```text
(hbnb) all User
```

Display a specific user using its ID:

```text
(hbnb) show User YOUR_USER_ID
```

Update a user's first name:

```text
(hbnb) update User YOUR_USER_ID first_name "Bertha"
```

Delete a user:

```text
(hbnb) destroy User YOUR_USER_ID
```

Exit the console:

```text
(hbnb) quit
```

The commands that create, display, update, or delete objects will be implemented progressively as the project develops.

## Technologies

- Python 3
- JSON
- Python `cmd` module
- Python `unittest` module
- Git and GitHub

## Authors

See the `AUTHORS` file for the list of project contributors.