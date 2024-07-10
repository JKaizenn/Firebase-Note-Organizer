# Notes Organizer DB

## Overview

The Notes Organizer DB is a software application designed to help users manage their notes efficiently. This project integrates with a Cloud Database to store, retrieve, update, and delete notes. As a software engineer, this project aims to enhance my skills in cloud database integration, GUI design, and Python programming. The application provides a user-friendly interface to interact with the notes stored in the cloud database.

## Description

The Notes Organizer DB is built using Python and Tkinter for the GUI, and it integrates with Google Firestore for cloud-based data storage. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on their notes. Each note consists of a title, content, and a timestamp. The application uses environment variables to securely access the Firestore credentials.

### How to Use the Program

1. **Start the Application**: Run the `main.py` script to launch the application.
2. **Title Screen**: The title screen provides an option to start the application.
3. **Main Menu**:
   - **View Notes**: Displays a list of all notes stored in the cloud database.
   - **Add Note**: Prompts the user to enter a title and content for a new note.
   - **Update Note**: Prompts the user to enter a note ID, new title, and new content to update an existing note.
   - **Delete Note**: Prompts the user to enter a note ID to delete a specific note.
   - **Exit**: Closes the application.

### Purpose

The purpose of writing this software is to create a practical application that demonstrates cloud database integration and enhances my understanding of GUI design in Python. This project serves as a learning experience in managing cloud-stored data securely and efficiently.

### Software Demo Video

[Software Demo Video](https://www.youtube.com)

## Cloud Database

### Description

The cloud database used for this project is Google Firestore. Firestore is a flexible, scalable database for mobile, web, and server development. It provides real-time synchronization and offline support, making it an excellent choice for applications that require real-time data updates.

### Database Structure

The database structure consists of a single collection named `notes`. Each document in the collection represents a note and contains the following fields:
- `id`: Unique identifier for the note (auto-generated).
- `title`: The title of the note.
- `content`: The content of the note.
- `timestamp`: The timestamp when the note was created or last updated.

## Development Environment

### Tools

- **Visual Studio Code**: Used as the code editor for development.
- **Git**: For version control.
- **GitHub**: To host the project repository.

### Programming Language and Libraries

- **Python**: The primary programming language used for the project.
- **Tkinter**: Used for creating the graphical user interface.
- **firebase-admin**: For integrating with Google Firestore.
- **python-dotenv**: To manage environment variables securely.

## Useful Websites

- [Firestore Documentation](https://firebase.google.com/docs/firestore)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
- [Google Firebase Console](https://console.firebase.google.com/)
- [Python Official Website](https://www.python.org/)

## Future Work

- **Improve UI Design**: Enhance the graphical interface for better user experience.
- **Add Search Functionality**: Allow users to search for notes by title or content.
- **User Authentication**: Implement user authentication to manage notes for different users.
