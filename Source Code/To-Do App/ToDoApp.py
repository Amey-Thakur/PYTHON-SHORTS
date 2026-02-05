"""
File: ToDoApp.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a graphical To-Do application using Tkinter for 
    the user interface and Python's pickle module for data persistence. It 
    demonstrates event-driven programming, GUI widget management, and 
    binary serialization for storing structured records.

Complexity Analysis:
    - Time Complexity: O(1) for fetch/update operations (hash-based key lookup).
    - Space Complexity: O(n) where n is the number of stored records.

Logic:
    1. Initialize a Tkinter main window with labeled entry fields.
    2. Fetch: Deserialize the pickle database, retrieve record by key, 
       and populate the GUI fields.
    3. Update: Read current field values, serialize to pickle file.
    4. Provide Quit button to gracefully terminate the application.
    5. Handle missing keys with error dialogs.
"""

import tkinter as tk
from tkinter import messagebox
import pickle
import os
from typing import Dict, Any, Optional


class ToDoService:
    """
    A service class managing CRUD operations for the To-Do data store.
    """

    def __init__(self, db_file: str = "todo_data.pkl"):
        """
        Initializes the service with a database file path.
        
        Args:
            db_file: Path to the pickle database file.
        """
        self.db_file = db_file
        self.fields = ('key', 'name', 'description', 'status')
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Creates database file if it doesn't exist."""
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'wb') as f:
                pickle.dump({}, f)

    def _load_db(self) -> Dict[str, Dict[str, Any]]:
        """Loads the database from file."""
        try:
            with open(self.db_file, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return {}

    def _save_db(self, db: Dict[str, Dict[str, Any]]) -> None:
        """Saves the database to file."""
        with open(self.db_file, 'wb') as f:
            pickle.dump(db, f)

    def fetch(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a record by its key.
        
        Args:
            key: The unique identifier for the record.
            
        Returns:
            The record dictionary, or None if not found.
        """
        db = self._load_db()
        return db.get(key)

    def update(self, record: Dict[str, Any]) -> bool:
        """
        Adds or updates a record in the database.
        
        Args:
            record: A dictionary containing the record fields.
            
        Returns:
            True if successful.
        """
        db = self._load_db()
        key = record.get('key', '')
        if key:
            db[key] = record
            self._save_db(db)
            return True
        return False

    def delete(self, key: str) -> bool:
        """
        Removes a record by key.
        
        Args:
            key: The unique identifier to delete.
            
        Returns:
            True if deleted, False if not found.
        """
        db = self._load_db()
        if key in db:
            del db[key]
            self._save_db(db)
            return True
        return False


class ToDoAppGUI:
    """
    A GUI class for the To-Do application using Tkinter.
    """

    def __init__(self, service: ToDoService):
        """
        Initializes the GUI with a service backend.
        
        Args:
            service: The ToDoService instance for data operations.
        """
        self.service = service
        self.entries: Dict[str, tk.Entry] = {}
        
        self.window = tk.Tk()
        self.window.title('To-Do Application')
        self.window.geometry('400x200')
        self._build_widgets()

    def _build_widgets(self) -> None:
        """Constructs the GUI widgets."""
        main_frame = tk.Frame(self.window, padx=10, pady=10)
        main_frame.pack()

        for idx, field in enumerate(self.service.fields):
            label = tk.Label(main_frame, text=field.capitalize() + ":")
            label.grid(row=idx, column=0, sticky='e', padx=5, pady=2)
            
            entry = tk.Entry(main_frame, font=('Arial', 12), width=30)
            entry.grid(row=idx, column=1, padx=5, pady=2)
            self.entries[field] = entry

        button_frame = tk.Frame(self.window, pady=10)
        button_frame.pack()

        tk.Button(button_frame, text="Fetch", command=self._fetch, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Update", command=self._update, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete", command=self._delete, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear", command=self._clear, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Quit", command=self.window.quit, width=10).pack(side=tk.LEFT, padx=5)

    def _fetch(self) -> None:
        """Fetches and displays a record by key."""
        key = self.entries['key'].get()
        record = self.service.fetch(key)
        if record:
            for field in self.service.fields:
                self.entries[field].delete(0, tk.END)
                self.entries[field].insert(0, record.get(field, ''))
        else:
            messagebox.showerror("Error", f"No record found for key: {key}")

    def _update(self) -> None:
        """Saves the current field values as a record."""
        record = {field: self.entries[field].get() for field in self.service.fields}
        if self.service.update(record):
            messagebox.showinfo("Success", "Record saved successfully!")
        else:
            messagebox.showerror("Error", "Key cannot be empty!")

    def _delete(self) -> None:
        """Deletes the record with the current key."""
        key = self.entries['key'].get()
        if self.service.delete(key):
            self._clear()
            messagebox.showinfo("Success", f"Record '{key}' deleted!")
        else:
            messagebox.showerror("Error", f"No record found for key: {key}")

    def _clear(self) -> None:
        """Clears all entry fields."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def run(self) -> None:
        """Starts the Tkinter main loop."""
        self.window.mainloop()


def main():
    """
    Demonstrates the scholarly To-Do App implementation.
    """
    print("--- To-Do App Service Demo ---")
    print("Launching GUI...")
    
    service = ToDoService()
    app = ToDoAppGUI(service)
    app.run()
    
    print("Application Closed.")


if __name__ == "__main__":
    main()
