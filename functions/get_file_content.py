import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_absolute = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_absolute, file_path))

        # First, check if the target file is a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Then, check if the target file within working directory
        valid_target_file= os.path.commonpath([working_dir_absolute, target_file]) == working_dir_absolute

        # If not within working directory, raise error
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Read the first MAX_CHARS characters of file and store
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # If there is more, add a truncation message
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'   
        return file_content_string
    except Exception as e:
        return f'Error: {e}'