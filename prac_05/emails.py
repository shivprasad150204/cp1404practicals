"""Email and Name Storage
Estimate: 20 minutes
Actual: 2025-06-23 11:21
"""

def generate_name(email):
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name

email_to_person = {}
email = input("Email: ")
while email:
    name = generate_name(email)
    confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirm not in ("", "y"):
        name = input("Enter your name: ")
    email_to_person[email] = name
    email = input("Email: ")

for address, person in email_to_person.items():
    print(f"{person} ({address})")
