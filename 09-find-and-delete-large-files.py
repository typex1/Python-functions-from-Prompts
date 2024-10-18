"""
In the current directory tree, find the top 10 largest files, and for each of them, ask whether they should be deleted (y) or not (n).
"""
import os
import heapq

def find_and_delete_largest_files(root_dir):
    # List to store the 10 largest files
    largest_files = []

    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            try:
                # Get file size
                file_size = os.path.getsize(filepath)

                # If we haven't found 10 files yet, add this file
                if len(largest_files) < 10:
                    heapq.heappush(largest_files, (file_size, filepath))
                else:
                    # If this file is larger than the smallest in our list, replace it
                    if file_size > largest_files[0][0]:
                        heapq.heapreplace(largest_files, (file_size, filepath))
            except OSError:
                # Handle case where we don't have permission to access the file
                print(f"Unable to access file: {filepath}")

    # Sort the files from largest to smallest
    largest_files.sort(reverse=True)

    # Ask user about deletion for each file
    for size, filepath in largest_files:
        size_mb = size / (1024 * 1024)  # Convert to MB
        print(f"\nFile: {filepath}")
        print(f"Size: {size_mb:.2f} MB")

        user_input = input("Delete this file? (y/n): ").lower()

        if user_input == 'y':
            try:
                os.remove(filepath)
                print(f"File deleted: {filepath}")
            except OSError as e:
                print(f"Error deleting file {filepath}: {e}")
        else:
            print("File not deleted.")

# Usage
if __name__ == "__main__":
    #root_directory = input("Enter the root directory to search: ")
    #root_directory = "/Users/fspiess/Documents/Trainer-Docs"
    root_directory = "/Users/fspiess/Downloads"
    find_and_delete_largest_files(root_directory)
