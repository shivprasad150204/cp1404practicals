
from prac_06.programming_language import ProgrammingLanguage

def main():
    """Demo to filter dynamic programming languages."""
    langs = [
        ProgrammingLanguage("Python", "Dynamic", True, 1991),
        ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
        ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ]

    print("These are the dynamically typed languages:")
    for lang in langs:
        if lang.is_dynamic():
            print(lang.name)

main()
