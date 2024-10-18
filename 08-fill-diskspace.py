"""
Write Python code which does the following: check how much disk space is left on the current filesystem. Then using "dd -if=/dev/random bs=100M count=1" create as many 100 megabyte files in folder "./space that the remaining disk space is filled up to 40 percent.

Here's a Python script that accomplishes the task you described:
"""
import os
import subprocess
import shutil

def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free

def create_file(filename, size):
    subprocess.run(['dd', f'if=/dev/random', f'of={filename}', 'bs=100M', 'count=1'])

def main():
    # Get current disk usage
    total, used, free = get_disk_usage('.')
    
    # Calculate the target usage (40% of total)
    target_usage = total * 0.4
    
    # Calculate how much space we need to fill
    space_to_fill = target_usage - used
    
    # Create the directory if it doesn't exist
    os.makedirs('./space', exist_ok=True)
    
    # Create 100MB files until we reach the target usage
    file_count = 0
    while space_to_fill > 0:
        filename = f'./space/file_{file_count}.bin'
        create_file(filename, 100 * 1024 * 1024)  # 100MB
        file_count += 1
        space_to_fill -= 100 * 1024 * 1024  # Subtract 100MB
        
        # Check disk usage again to ensure we don't overfill
        _, used, _ = get_disk_usage('.')
        if used >= target_usage:
            break
    
    print(f"Created {file_count} files of 100MB each.")
    print(f"Current disk usage: {used / total:.2%}")

if __name__ == "__main__":
    main()
