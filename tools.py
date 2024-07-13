import os
import subprocess

def use_cmd(command):
    if command.startswith('cd '):
        # Extract the directory path
        path = command[3:].strip()
        try:
            os.chdir(path)
            return f"Changed directory to: {os.getcwd()}"
        except FileNotFoundError:
            return f"Directory not found: {path}"
    else:
        # For other commands, use subprocess as before
        try:
            p1 = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
            # Combine stdout and stderr, handling potential None values
            output = (p1.stdout or '') + (p1.stderr or '')
            return output
        except Exception as e:
            return f"An error occurred: {str(e)}"

