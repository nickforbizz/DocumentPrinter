import os
import time

import tkinter as tk
import tkinter.filedialog as fd

class PrintAllFiles:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Print All Files")

        # Create a label to display the folder path
        self.folder_path_label = tk.Label(self.root, text="Folder Path:")
        self.folder_path_label.place(x=10, y=10)

        # Create an entry widget to display the folder path
        self.folder_path_entry = tk.Entry(self.root)
        self.folder_path_entry.place(x=100, y=10)

        # Create a button to select a folder
        self.select_folder_button = tk.Button(self.root, text="Select Folder", command=self.select_folder)
        self.select_folder_button.place(x=300, y=10)

        # Create a button to print all the files in the folder
        self.print_button = tk.Button(self.root, text="Print", command=self.print_all_files)
        self.print_button.place(x=200, y=50)

        # Create a list to store the errors
        self.errors = []

        # Set the GUI size
        self.root.geometry("400x200")

        # Start the mainloop
        self.root.mainloop()

    def select_folder(self):
        # Get the folder path from the user
        folder_path = fd.askdirectory()

        # Update the entry widget with the folder path
        self.folder_path_entry.delete(0, tk.END)
        self.folder_path_entry.insert(0, folder_path)

    def print_all_files(self):
        # Get the folder path from the entry widget
        folder_path = self.folder_path_entry.get()

        # Check if the folder path is valid
        if not os.path.isdir(folder_path):
            tk.messagebox.showerror("Error", "Invalid folder path")
            return

        # Get a list of all the files in the folder
        files = os.listdir(folder_path)

        # Print all the files
        for file in files:
            file_path = os.path.join(folder_path, file)

            # Try to print the file
            try:
                os.startfile(file_path, 'print')
                print(f'Printing {file}')

                # Sleeping the program for 5 seconds so as to account the 
                # steady processing of the print operation.
                time.sleep(5)
            except:
                # Store the error
                self.errors.append("Failed to print file {}".format(file_path))

        # Display the errors in a dialog
        if self.errors:
            error_dialog = tk.Toplevel(self.root)
            error_dialog.title("Errors")

            error_text = "\n".join(self.errors)
            error_label = tk.Label(error_dialog, text=error_text)
            error_label.pack()

            error_dialog.mainloop()

if __name__ == "__main__":
    PrintAllFiles()
