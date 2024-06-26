import tkinter as tk
from tkinter import filedialog

from texteditorapplication import hookspecs
from texteditorapplication import lib

import pluggy

condiments_tray = {"pickled walnuts": 13, "steak sauce": 4, "mushy peas": 2}

def main():
    pm = get_plugin_manager()
    cook = TextEditor(pm.hook)
    cook.run_editor()

def get_plugin_manager():
    pm = pluggy.PluginManager("texteditorapplication")
    pm.add_hookspecs(hookspecs)
    pm.load_setuptools_entrypoints("texteditorapplication")
    pm.register(lib)
    return pm

class TextEditor():
    def __init__(self, hook):
        self.hook = hook

    def new_file(self):
        self.text.delete(0.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfile(mode='r')
        if file:
            data = file.read()
            self.text.delete(0.0, tk.END)
            self.text.insert(0.0, data)

    def save_file(self):
        filename = "Untitled.txt"
        data = self.text.get(0.0, tk.END)
        file = open(filename, 'w')
        file.write(data)

    def save_as(self):
        file = filedialog.asksaveasfile(mode='w')
        if file:
            data = self.text.get(0.0, tk.END)
            file.write(data)

    def update_text(self, event):
        character_count = self.hook.count_characters(text=self.text.get(0.0, tk.END))
        self.label.config(text=f'Character count: {character_count}')

    def run_editor(self):
        self.root = tk.Tk()
        self.root.title = "Text Editor"
        self.root.geometry("600x600")

        self.text = tk.Text(self.root)  # Create text variable here
        self.text.bind('<Key>', self.update_text)  # Bind update on key release
        self.text.pack()

        self.label = tk.Label(self.root, text=('Character count: ', 0))
        self.label.pack(padx=20, pady=20)

        myMenu = tk.Menu()
        fileMenu = tk.Menu()
        fileMenu.add_command(label='New File', command=self.new_file)
        fileMenu.add_command(label='Open File', command=self.open_file)
        fileMenu.add_command(label='Save File', command=self.save_file)
        fileMenu.add_command(label='Save as', command=self.save_as)
        fileMenu.add_command(label='Exit', command=quit)
        myMenu.add_cascade(label='File', menu=fileMenu)

        self.root.mainloop()
    
if __name__ == "__main__":
    main()