import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        working_dir_absolute = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_absolute, directory))

        # First, check if the target directory is directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # Then, check if the target directory is within working directory
        valid_target_dir = os.path.commonpath([working_dir_absolute, target_dir]) == working_dir_absolute

        # If not within working directory, raise error
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        files = os.listdir(target_dir)
        record = ""
        for file in files:
            size = os.path.getsize(os.path.join(target_dir, file))
            is_dir = os.path.isdir(os.path.join(target_dir, file))
            record +=f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"
        return record
    except Exception as e:
        return f'Error: {e}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)