import tkinter as tk
from tkinter import messagebox


def main():
    root = tk.Tk()


    root.title("Butler-ToDo")

    root.geometry("420x420")

    # ---------- Menu ----------
    menubar = tk.Menu(root)

    # (b) Menu colors: pick 2 complementary-ish colors
    # Example: dark blue background + light gold foreground
    menu_bg = "#1f3b73"   # deep blue
    menu_fg = "#f2c14e"   # golden

    file_menu = tk.Menu(menubar, tearoff=0, background=menu_bg, foreground=menu_fg)

    # (e) File -> Exit closes correctly
    def safe_exit():
        # Optional: confirm exit (you can remove if you want)
        if messagebox.askokcancel("Exit", "Exit the To-Do app?"):
            root.destroy()

    file_menu.add_command(label="Exit", command=safe_exit)
    menubar.add_cascade(label="File", menu=file_menu)

    root.config(menu=menubar)

    # ---------- Header / Instructions ----------
    header = tk.Label(
        root,
        text="To-Do List",
        font=("Arial", 16, "bold")
    )
    header.pack(pady=(10, 4))

    # (d) Instructions label (how to delete)
    instr = tk.Label(
        root,
        text="Tip: Right-click an item to delete it.",
        font=("Arial", 10)
    )
    instr.pack(pady=(0, 10))

    # ---------- Entry + Add button ----------
    entry_frame = tk.Frame(root)
    entry_frame.pack(padx=12, pady=(0, 10), fill="x")

    task_var = tk.StringVar()
    task_entry = tk.Entry(entry_frame, textvariable=task_var, font=("Arial", 11))
    task_entry.pack(side="left", expand=True, fill="x")

    def add_task():
        task = task_var.get().strip()
        if not task:
            return
        listbox.insert(tk.END, task)
        task_var.set("")
        task_entry.focus()

    add_btn = tk.Button(entry_frame, text="Add", command=add_task)
    add_btn.pack(side="left", padx=(8, 0))

    # ---------- Listbox + Scrollbar (Scrolling To-Do style) ----------
    list_frame = tk.Frame(root)
    list_frame.pack(padx=12, pady=10, fill="both", expand=True)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    listbox = tk.Listbox(
        list_frame,
        font=("Arial", 11),
        yscrollcommand=scrollbar.set,
        selectmode=tk.SINGLE
    )
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox.yview)

    # Add a couple starter tasks (optional; you can remove)
    listbox.insert(tk.END, "Grade 325 Discussion Board")
    listbox.insert(tk.END, "Grade 325 Tkinter program")

    # (c) Right-click delete instead of left-click
    def delete_task(event):
        # Figure out which item was right-clicked
        index = listbox.nearest(event.y)
        if index >= 0 and index < listbox.size():
            listbox.delete(index)

    # Windows right-click is Button-3
    listbox.bind("<Button-3>", delete_task)

    # Nice usability: Enter key adds task
    root.bind("<Return>", lambda e: add_task())

    root.mainloop()


if __name__ == "__main__":
    main()