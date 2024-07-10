import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from firebase_admin import credentials, firestore, initialize_app
import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Firestore DB
json_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if not os.path.exists(json_path):
    print(f"JSON file not found at: {json_path}")
cred = credentials.Certificate(json_path)
initialize_app(cred)
db = firestore.client()

# Collection name
collection_name = 'notes'

def create_note(title, content):
    try:
        notes = db.collection(collection_name).stream()
        used_ids = [int(note.id) for note in notes if note.id.isdigit()]
        new_id = next(i for i in range(101) if i not in used_ids)
        note = {
            'title': title,
            'content': content,
            'timestamp': datetime.datetime.now()
        }
        db.collection(collection_name).document(str(new_id)).set(note)
        print(f'Note "{title}" added successfully with ID {new_id}.')
    except Exception as e:
        print(f'Error adding note: {e}')

def get_notes():
    try:
        notes = db.collection(collection_name).stream()
        notes_list = []
        for note in notes:
            note_dict = note.to_dict()
            note_dict['id'] = note.id
            notes_list.append(note_dict)
        return notes_list
    except Exception as e:
        print(f'Error retrieving notes: {e}')
        return []

def update_note(note_id, title=None, content=None):
    try:
        note_ref = db.collection(collection_name).document(note_id)
        updates = {}
        if title:
            updates['title'] = title
        if content:
            updates['content'] = content
        if updates:
            updates['timestamp'] = datetime.datetime.now()
            note_ref.update(updates)
            print(f'Note "{note_id}" updated successfully.')
        else:
            print('No updates provided.')
    except Exception as e:
        print(f'Error updating note: {e}')

def delete_note(note_id):
    try:
        note_ref = db.collection(collection_name).document(note_id)
        note_ref.delete()
        print(f'Note "{note_id}" deleted successfully.')
    except Exception as e:
        print(f'Error deleting note: {e}')

class NotesOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes Organizer")
        self.root.geometry("1920x1080")  # Set initial window size
        self.show_title_screen()

    def show_title_screen(self):
        self.clear_screen()
        self.title_frame = tk.Frame(self.root, bg="gray20")
        self.title_frame.pack(expand=True, fill=tk.BOTH)

        title_label = tk.Label(self.title_frame, text="Note Organizer DB", font=("Helvetica", 48, "bold"), fg="white", bg="gray20")
        title_label.pack(pady=50)

        subtitle_label = tk.Label(self.title_frame, text="By Jessen Forbush", font=("Helvetica", 24), fg="white", bg="gray20")
        subtitle_label.pack(pady=20)

        start_button = tk.Button(self.title_frame, text="Start", font=("Helvetica", 24), command=self.show_menu, bg="gray30", fg="white", relief="flat", padx=20, pady=10)
        start_button.pack(pady=20)

    def show_menu(self):
        self.clear_screen()
        self.menu_frame = tk.Frame(self.root, bg="gray20")
        self.menu_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

        title_label = tk.Label(self.menu_frame, text="Menu", font=("Helvetica", 36, "bold"), fg="white", bg="gray20")
        title_label.pack(pady=20)

        button_style = {
            "font": ("Helvetica", 24),
            "bg": "gray70",
            "fg": "black",
            "relief": "flat",
            "padx": 20,
            "pady": 10,
            "bd": 3,
            "highlightthickness": 0
        }

        self.view_notes_button = tk.Button(self.menu_frame, text="View Notes", command=self.view_notes, **button_style)
        self.view_notes_button.pack(pady=10)

        self.add_note_button = tk.Button(self.menu_frame, text="Add Note", command=self.add_note, **button_style)
        self.add_note_button.pack(pady=10)

        self.update_note_button = tk.Button(self.menu_frame, text="Update Note", command=self.update_note, **button_style)
        self.update_note_button.pack(pady=10)

        self.delete_note_button = tk.Button(self.menu_frame, text="Delete Note", command=self.delete_note, **button_style)
        self.delete_note_button.pack(pady=10)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.root.quit, **button_style)
        self.exit_button.pack(pady=10)

    def view_notes(self):
        self.clear_screen()
        self.notes_frame = tk.Frame(self.root, bg="gray20")
        self.notes_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

        notes = get_notes()
        for note in notes:
            note_text = f"ID: {note['id']}\nTitle: {note['title']}\nContent: {note['content']}\n"
            note_label = tk.Label(self.notes_frame, text=note_text, pady=5, padx=5, relief="solid", bg="gray30", fg="white")
            note_label.pack(pady=5)

        back_button = tk.Button(self.notes_frame, text="Back", font=("Helvetica", 24), command=self.show_menu, bg="gray70", fg="black", relief="flat", padx=20, pady=10, bd=3, highlightthickness=0)
        back_button.pack(pady=10)

    def add_note(self):
        title = simpledialog.askstring("Input", "Enter Note Title:")
        content = simpledialog.askstring("Input", "Enter Note Content:")

        if title and content:
            create_note(title, content)
            messagebox.showinfo("Success", "Note added successfully!")
        else:
            messagebox.showwarning("Input Error", "Title and Content cannot be empty.")

    def update_note(self):
        note_id = simpledialog.askstring("Input", "Enter Note ID to update:")
        title = simpledialog.askstring("Input", "Enter New Title (leave blank to keep current):")
        content = simpledialog.askstring("Input", "Enter New Content (leave blank to keep current):")

        if note_id:
            update_note(note_id, title, content)
            messagebox.showinfo("Success", "Note updated successfully!")
        else:
            messagebox.showwarning("Input Error", "Note ID cannot be empty.")

    def delete_note(self):
        notes = get_notes()
        notes_text = "\n".join([f"ID: {note['id']} | Title: {note['title']}" for note in notes])
        messagebox.showinfo("Notes List", notes_text)

        note_id = simpledialog.askstring("Input", "Enter Note ID to delete:")

        if note_id:
            delete_note(note_id)
            messagebox.showinfo("Success", "Note deleted successfully!")
        else:
            messagebox.showwarning("Input Error", "Note ID cannot be empty.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesOrganizerApp(root)
    root.mainloop()
