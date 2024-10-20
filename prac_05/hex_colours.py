COLOUR_CODES = {
    "aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
    "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
    "beige": "#f5f5dc", "bisque1": "#ffe4c4"
}

def get_colour_code(colour_name):
    """Return the hexadecimal code for a given colour name."""
    return COLOUR_CODES.get(colour_name, "Invalid colour name")

def main():
    colour_name = input("Enter a colour name (or press Enter to quit): ").lower()
    while colour_name:
        print(f"The code for \"{colour_name}\" is {get_colour_code(colour_name)}")
        colour_name = input("Enter another colour name (or press Enter to quit): ").lower()

main()
