# ToDo Application using Django

A simple and intuitive ToDo application built with Django that allows users to manage tasks efficiently. The app is designed with a clean, minimalistic UI and offers essential features to organize and track tasks.

## Features

- **Day/Light Mode Toggle**: Switch between day and light mode for a more comfortable user experience based on your preference.
- **Task Management**:
  - Separate sections for **in-progress** and **completed tasks**.
  - Add tasks with a detailed **task description** input.
  - **Edit** tasks to update descriptions or modify them as needed.
  - **Mark tasks as complete**, and they are automatically moved to the completed section.
  - **Delete tasks** permanently if they are no longer needed.
  - **Undo** tasks if they were accidentally marked as complete.
- **Simple and Elegant UI**: A user-friendly interface that makes managing tasks a seamless experience.

## Project Setup

To run this project locally, follow these steps:

### Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.x
- Django (use `pip install django` to install Django if needed)
- Other dependencies mentioned below

### Installation Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/Brian-Mendonca/ToDo-Project-Using-Django.git
   ```
2. Navigate to the project directory:

   ```bash
   cd ToDo_Applications
   ```
3. Run migrations:

   ```bash
   python manage.py migrate
   ```
4. Start the development server:

   ```bash
   python manage.py runserver
   ```
5. Open your browser and visit http://localhost:8000/todo or http://127.0.0.1:8000/todo to view the application.

6. ## Usage

Once the application is running, you can perform the following actions:

1. **Adding a Task**: 
   - Use the input field to enter your task and description.
   - Click on the "Add Task" button to save the task.

2. **Viewing Tasks**: 
   - All your tasks will be displayed in the "In Progress" section.
   - Completed tasks will be shown in the "Completed" section.

3. **Editing a Task**: 
   - Click the 3 dots then, "Edit" button next to the task you want to modify.
   - Update the task description and save your changes.

4. **Marking a Task as Complete**: 
   - Click the 3 dots then, "Mark Completed" button next to a task to move it to the "Completed" section.

5. **Deleting a Task**: 
   - Click the  3 dots then, "Delete" button to remove a task permanently.

6. **Undoing a Task**: 
   - If you accidentally mark a task as complete, you can click the "Undo" button to move it back to the "In Progress" section.

7. **Toggling Day/Light Mode**: 
   - Use the toggle switch to switch between day mode and light mode for a better user experience.

## Contact

For any inquiries or feedback regarding the ToDo application, feel free to reach out:

- **Name**: Brian Mendonca
- **Email**: [your_email@example.com](mailto:brianmendonca12@gmail.com)
- **GitHub**: [Brian-Mendonca](https://github.com/Brian-Mendonca)
- **Instagram**: [peace_warrior.04](https://instagram.com/peace_warrior.04)


