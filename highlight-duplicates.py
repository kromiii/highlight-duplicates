import difflib
import sys
import re

def highlight_duplicates(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Split text into lines
    lines = re.split(r'[.?]', text)

    # Remove leading/trailing whitespace and empty lines
    lines = [line.strip() for line in lines if line.strip()]
    # Remove lines that starts with '\' or '%' (TeX command)
    lines = [line for line in lines if not line.startswith(('\\', '%'))]
    # Remove lines that are too short
    lines = [line for line in lines if len(line) > 10]

    # Find duplicates using difflib's SequenceMatcher
    duplicates = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            similarity_ratio = difflib.SequenceMatcher(None, lines[i], lines[j]).ratio()
            if similarity_ratio > 0.8:  # You can adjust this threshold
                duplicates.append((i, j))

    # Print or process duplicates as needed
    for i, j in duplicates:
        print(f'Duplicate found between lines {i + 1} and {j + 1}:')
        print(lines[i])
        print(lines[j])
        print('-' * 20)

if __name__ == "__main__":
    file_path = sys.argv[1]
    highlight_duplicates(file_path)
