import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.configure(bg="lightgray")

        self.create_widgets()
        self.load_tasks_from_file()

    def create_widgets(self):
        self.create_main_frame()
        self.create_entry_frame()
        self.create_listbox_frame()
        self.create_button_frame()

    def create_main_frame(self):
        main_frame = tk.Frame(self.root, bg="lightgray", padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame = main_frame

    def create_entry_frame(self):
        entry_frame = tk.Frame(self.main_frame, bg="lightgray")
        entry_frame.pack(fill=tk.X)

        self.enter_task_label = tk.Label(
            entry_frame, text="Enter Your Task", bg="lightgray", font=("Arial", 12)
        )
        self.enter_task_label.pack(side=tk.LEFT, padx=(0, 10))

        self.task_entry = tk.Entry(entry_frame, font=("Arial", 12), width=30)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.task_entry.bind("<Return>", lambda event: self.submit_task())

        self.submit_button = tk.Button(
            entry_frame, text="Submit", command=self.submit_task, bg="blue", fg="white"
        )
        self.submit_button.pack(side=tk.LEFT, padx=(10, 0))

    def create_listbox_frame(self):
        listbox_frame = tk.Frame(self.main_frame, bg="lightgray")
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        self.tasks_box = tk.Listbox(
            listbox_frame, selectmode=tk.SINGLE, font=("Arial", 12), bg="white"
        )
        self.tasks_box.pack(fill=tk.BOTH, expand=True)
        self.tasks_box.bind("<Delete>", lambda event: self.delete_task())

    def create_button_frame(self):
        button_frame = tk.Frame(self.main_frame, bg="lightgray")
        button_frame.pack(fill=tk.X, pady=(10, 0))

        self.delete_button = tk.Button(
            button_frame, text="Delete", command=self.delete_task, bg="red", fg="white"
        )
        self.delete_button.pack(side=tk.LEFT, padx=(0, 10))

        self.delete_all_button = tk.Button(
            button_frame,
            text="Delete All Tasks",
            command=self.delete_all_tasks,
            bg="red",
            fg="white",
        )
        self.delete_all_button.pack(side=tk.LEFT)

    def save_tasks_to_file(self):
        try:
            with open("tasks.txt", "w") as f:
                for task in self.tasks:
                    f.write(f"{task}\n")
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks_from_file(self):
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
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.tasks_box.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task = self.tasks_box.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks_box.delete(index)
            del self.tasks[index]
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "No task selected!")

    def delete_all_tasks(self):
        self.tasks_box.delete(0, tk.END)
        self.tasks.clear()
        self.save_tasks_to_file()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
