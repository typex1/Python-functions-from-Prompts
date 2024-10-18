import os
import hashlib

def get_file_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicate_files(folder_path):
    """Find duplicate text files in the specified folder."""
    file_hashes = {}
    duplicates = []

    # Walk through all files in the folder
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.txt'):  # Only consider text files
                file_path = os.path.join(root, filename)
                file_hash = get_file_hash(file_path)

                if file_hash in file_hashes:
                    # If the hash already exists, it's a duplicate
                    duplicates.append((file_path, file_hashes[file_hash]))
                else:
                    # If it's a new hash, add it to the dictionary
                    file_hashes[file_hash] = file_path

    return duplicates

def main():
    folder_path = input("Enter the folder path to inspect: ")
    
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    duplicate_files = find_duplicate_files(folder_path)

    if duplicate_files:
        print("Duplicate files found:")
        for duplicate, original in duplicate_files:
            print(f"Duplicate: {duplicate}")
            print(f"Original: {original}")
            print()
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()
