import subprocess
import os

def use_cmd(command):
    try:
        # Get the current working directory
        current_location = os.getcwd()
        
        # Run the command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, encoding='cp1252', errors='replace')
        
        # Prepare the output
        cmd_output = result.stdout.strip()  # Remove leading/trailing whitespace
        
        if result.stderr:
            cmd_output += "\n" + result.stderr.strip()
        
        # Combine the location and command output
        full_output = f"{current_location}\n{cmd_output}"
        
        return full_output
    except subprocess.CalledProcessError as e:
        return f"Current location: {os.getcwd()}\n\nAn error occurred: {e}\nError output: {e.stderr}"
    except Exception as e:
        return f"Current location: {os.getcwd()}\n\nAn unexpected error occurred: {e}"
    