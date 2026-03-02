from app.io.input import input_from_console, read_from_file, read_from_file_pandas
from app.io.output import output_to_console, output_to_file

def main():
    """
    Main program function.
    Calls input functions, outputs results to console,
    and writes them to a file.
    """
    console_text = input_from_console()
    file_text_builtin = read_from_file("data/input.txt")
    file_text_pandas = read_from_file_pandas("data/input.txt")

    output_to_console(console_text)
    output_to_console(file_text_builtin)
    output_to_console(file_text_pandas)

    combined_text = (
        f"Console input:\n{console_text}\n\n"
        f"Built-in file read:\n{file_text_builtin}\n\n"
        f"Pandas file read:\n{file_text_pandas}\n"
    )

    output_to_file("data/output.txt", combined_text)

if __name__ == '__main__':
    main()