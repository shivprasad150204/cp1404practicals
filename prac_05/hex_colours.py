"""Hex Colour Lookup Tool
Estimate: 15 minutes
Actual: 2025-06-23 11:21
"""

COLOUR_NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2"
}

user_input = input("Colour name: ").lower()
while user_input:
    print(COLOUR_NAME_TO_HEX.get(user_input, "No such colour in dictionary"))
    user_input = input("Colour name: ").lower()
