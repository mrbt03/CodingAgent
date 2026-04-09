import os
import subprocess
def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_absolute = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_absolute, file_path))

        # First, check if the target file is a file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Then, check if the target file within working directory
        valid_target_file= os.path.commonpath([working_dir_absolute, target_file]) == working_dir_absolute

        # If not within working directory, raise error
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'


        command = ["python", target_file]
        if args:
            command.extend(args)
        completed_process =subprocess.run(command, cwd = working_dir_absolute, capture_output=True, text=True, timeout=30)

        output = ""
        if completed_process.returncode !=0:
            output += f'Process exited with code {completed_process.returncode}\n'
        if completed_process.stderr == "" and completed_process.stdout == "":
            output += f'No output produced'
        else:
            output += f'STDOUT: {completed_process.stdout}\n'
            output += f'STDERR: {completed_process.stderr}\n'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"