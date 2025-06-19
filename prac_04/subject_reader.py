"""
This script reads subject data from a file and displays each subject's
lecturer and student count in a formatted output.
"""

FILENAME = "subject_data.txt"

def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student count to integer
            data.append(parts)
    return data


def display_subject_details(data):
    """Display details of each subject in a formatted manner."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")


main()
