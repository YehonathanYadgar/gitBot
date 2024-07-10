import subprocess
import sys

def run_cmd_command(command):
    try:
        
        result = subprocess.run(command, shell=True, check=True, capture_output=True, encoding='cp1252', errors='replace')
        output = "Command output:\n" + result.stdout
        
        if result.stderr:
            output += "\nErrors:\n" + result.stderr
        
        return output
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}\nError output: {e.stderr}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(run_cmd_command("dir"))