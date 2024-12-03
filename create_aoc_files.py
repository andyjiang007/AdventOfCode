import os


def create_aoc_files_with_template(year: int, template_path: str):
    # Read the content of the template file
    try:
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print(f"Error: Template file '{template_path}' not found.")
        return

    # Define the base directory with the year
    base_dir = str(year)

    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create subfolders and files
    for day in range(1, 31):  # We need 30 subfolders (from day1 to day30)
        day_folder = os.path.join(base_dir, f"day{day}")

        # Create the subfolder if it doesn't exist
        if not os.path.exists(day_folder):
            os.makedirs(day_folder)
        else:
            continue

        # Define the Python and text file names
        python_file = os.path.join(day_folder, f"aoc{year}_day{day}.py")
        text_file = os.path.join(day_folder, f"aoc{year}_day{day}.txt")

        # Create the Python file using the template content
        with open(python_file, "w") as f:
            # Insert placeholders for customization (optional)
            customized_content = template_content.replace("{DAY}", str(day)).replace(
                "{YEAR}", str(year)
            )
            f.write(customized_content)

        # Create the text file
        with open(text_file, "w") as f:
            pass  # Empty text file


if __name__ == "__main__":
    year = int(input("Enter the year: "))
    TEMPLATE_FILE_PATH = "solve_template.py"
    create_aoc_files_with_template(year, TEMPLATE_FILE_PATH)
