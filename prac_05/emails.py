def main():
    """Create a dictionary of emails to names."""
    email_to_name = {}
    email = input("Enter email: ")

    while email:
        # Extract name from email
        prefix = email.split('@')[0]
        name_parts = prefix.split('.')
        name = " ".join(name_parts).title()

        # Confirm or update the name
        confirmation = input(f"Is your name {name}? (Y/n): ").strip().lower()
        if confirmation not in ("y", ""):
            name = input("Enter your name: ")

        # Store the email and name
        email_to_name[email] = name

        # Prompt for the next email
        email = input("Enter email: ")

    # Display the result
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
