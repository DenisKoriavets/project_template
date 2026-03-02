def output_to_console(text: str) -> None:
    """
    Outputs text to the console.

    Args:
        text (str): Text to display.
    """
    print(text)

def output_to_file(file_path: str, text: str) -> None:
    """
    Writes text to a file using Python built-in capabilities.

    Args:
        file_path (str): Path to the file.
        text (str): Text to write.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)