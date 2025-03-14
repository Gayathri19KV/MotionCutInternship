import tkinter as tk
from tkinter import messagebox, filedialog

def reverse_characters():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Input cannot be empty!")
        return
    result.set(text[::-1])

def reverse_words():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Input cannot be empty!")
        return
    result.set(" ".join(text.split()[::-1]))

def save_to_file():
    if not result.get():
        messagebox.showerror("Error", "No reversed text to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(result.get())
        messagebox.showinfo("Success", f"Reversed text saved to {file_path}")

# GUI Setup
root = tk.Tk()
root.title("Text Reverser")
root.geometry("400x300")

tk.Label(root, text="Enter Text:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

result = tk.StringVar()
tk.Label(root, text="Reversed Text:").pack(pady=5)
tk.Entry(root, textvariable=result, state="readonly", width=40).pack(pady=5)

tk.Button(root, text="Reverse Characters", command=reverse_characters).pack(pady=5)
tk.Button(root, text="Reverse Words", command=reverse_words).pack(pady=5)
tk.Button(root, text="Save to File", command=save_to_file).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
