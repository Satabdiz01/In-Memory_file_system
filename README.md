
<h1 align='center'> In-Memory File System </h1>
<p align='center'>
<img src='http://ForTheBadge.com/images/badges/built-with-love.svg'>
</p>

[![License: Apache](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

### Built by: Satabdi Beuria, Final year, NIT Rourkela

## Overview

This project implements a basic in-memory file system in Python, providing fundamental file system functionalities. It simulates directory structures and supports operations like creating directories, and files, moving, copying, and deleting.

## Implementation Details

### File System Structure (Data Structure):
- The primary data structure is an object (`fs`) representing the file system. It is organized as a hierarchical structure with directories and files.
- Each directory is represented by an object with a `type` property set to 'dir' and a `content` property containing nested files and directories or, an object with keys as file/directory names and values as objects containing type and content information.
- Files are represented similarly but with a `type` property set to 'file' and a `content` property containing the file's data.

### File System Operations:
- `mkdir`: Creates a new directory.
- `cd`: Changes the current directory.
  - Support navigating to the parent directory using `..`
  - Moving to the root directory using `/`
  - Navigating to a specified absolute path.
- `ls`: Lists the contents of the current or specified directory.
- `grep`: Searches for a specified pattern in a file (bonus functionality).
- `cat`: Displays the contents of a file.
- `touch`: Creates a new empty file.
- `echo`: Writes text to a file.
- `mv`: Moves a file or directory to another location.
- `cp`: Copies a file or directory to another location.
- `rm`: Removes a file or directory.

### Design Decisions:

- This code focuses on providing a basic understanding of file system operations in a **Python** environment.
- Utilizes a **composite design pattern**, treating the entire collection of objects similarly to individual objects within the collection.
- The implementation prioritizes simplicity and efficiency using **objects** for representing directories and files.

![Flowchart Illustrating the File System Design](https://miro.medium.com/v2/resize:fit:828/format:webp/1*Urt2Xs4OwqJYxRx1CecKkQ.png)

## Setup Instructions:
Setup Instructions for Running a Python Script on Windows:

### Requirements:
- Python: Ensure that Python is installed on your local machine. You can download the latest version from the official website: [Python Downloads](https://www.python.org/downloads/)

### Verify Installation:
1. Open Command Prompt: Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.
2. Run the following commands to verify that Python is installed:
   ```bash
   python --version
   pip --version
   ```
   You should see version numbers for Python and pip.

### Running the Python Code:
1. **Clone the Repository:**
   Open your terminal or command prompt and run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/Satabdiz01/In-Memory_file_system.git
   ```

2. **Navigate to the Project Directory:**
   Change your current working directory to the cloned project folder:
   ```bash
   cd In-Memory_file_system
   ```

3. **Open Command Prompt:**
   Open a new Command Prompt in the directory where you cloned the GitHub repository.

4. **Run the Script:**
   Execute the main Python file (assuming `main.py` is the main file) using Python:
   ```bash
   python main.py
   ```
   This command runs the Python script, allowing you to interact with the file system.

5. **Interact with the File System:**
   Once the script is running, you can use the provided commands to interact with the file system.

6. **Exit the Script:**
   To exit the script, type `exit` and press Enter. This will close the Python script.

**Note:** Ensure that Python is added to your system's PATH during installation to run commands like `python` and `pip` directly from the Command Prompt.
