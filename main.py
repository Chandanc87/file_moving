import shutil
import os

def move_file(src, dest):
    try:
        # Check if the source file exists
        if not os.path.exists(src):
            print(f"Source file {src} does not exist.")
            return
        
        # Check if the destination directory exists
        if not os.path.exists(dest):
            print(f"Destination directory {dest} does not exist. Creating it.")
            os.makedirs(dest)  # Create the destination directory if it doesn't exist

        # Move the file
        shutil.move(src, dest)
        print(f"File has been moved to {dest}")
    
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
source_file = "C:\\Users\\chandan\\OneDrive\\Desktop\\project\\scr\\input\\tb.txt"  # Change to the source file path
destination_folder = 'C:\\Users\\chandan\\OneDrive\\Desktop\\project\\scr\\output'   # Change to the destination folder path

move_file(source_file, destination_folder)
