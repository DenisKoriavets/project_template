import pandas as pd

def input_from_console() -> str:
    """
    Reads text input from the console.

    Returns:
        str: Text entered by the user.
    """
    return input("Enter text: ")

def read_from_file(file_path: str) -> str:
    """
    Reads text from a file using Python built-in capabilities.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File content as a string.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_from_file_pandas(file_path: str) -> str:
    """
    Reads text from a file using pandas library.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File content as a single string.
    """
    series = pd.read_fwf(file_path, header=None)
    return "\n".join(series[0].astype(str))