"""
CP1404/CP5632 Practical - Client code to demonstrate ProgrammingLanguage class
Estimate time: 15 minutes
"""

from programming_language import ProgrammingLanguage

def main():
    """Demo test code to show how to use the ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print the string representation of the Python object
    print(python)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
