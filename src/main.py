import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.root.title("To-Do List App")
        self.root.geometry("800x600")

        self.create_widgets()
        self.load_tasks_from_file()

    def create_widgets(self):
        # Create a label
        self.enter_task_label = tk.Label(self.root, text="Enter Your Task")
        self.enter_task_label.pack()

        # Create an entry widget
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        # Create a submit button
        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.submit_task
        )
        self.submit_button.pack()

        # Create a listbox to display tasks
        self.tasks_box = tk.Listbox(self.root)
        self.tasks_box.pack()

        # Create a delete button
        self.delete_button = tk.Button(
            self.root, text="Delete", command=self.delete_task
        )
        self.delete_button.pack()

        # Create a delete all button
        self.delete_all_button = tk.Button(
            self.root, text="Delete All Tasks", command=self.delete_all_tasks
        )
        self.delete_all_button.pack()

    def save_tasks_to_file(self):
        """Saves tasks to a file."""
        try:
            with open("tasks.txt", "w") as f:
                for task in self.tasks:
                    f.write(f"{task}\n")
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks_from_file(self):
        """Loads tasks from a file."""
        try:
            with open("tasks.txt", "r") as f:
                for task in f:
                    task = task.strip()
                    self.tasks.append(task)
                    self.tasks_box.insert(tk.END, task)
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty list
        except IOError as e:
            messagebox.showerror("Error", f"Failed to load tasks: {e}")

    def submit_task(self):
        """Submits a new task."""
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.tasks_box.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
            self.save_tasks_to_file()

    def delete_task(self):
        """Deletes the selected task."""
        selected_task = self.tasks_box.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks_box.delete(index)
            del self.tasks[index]
            self.save_tasks_to_file()

    def delete_all_tasks(self):
        """Deletes all tasks."""
        self.tasks_box.delete(0, tk.END)
        self.tasks.clear()
        self.save_tasks_to_file()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
