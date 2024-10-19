def main():
    """Create a dictionary of emails to names."""
    email_to_name = {}
    email = input("Enter email: ")
    while email:
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n): ").strip().lower()
        if confirmation not in ("y", ""):
            name = input("Enter your name: ")
        email_to_name[email] = name
        email = input("Enter email: ")

    # Display the result
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract the name from the email address."""
    prefix = email.split('@')[0]
    name_parts = prefix.split('.')
    return " ".join(name_parts).title()


if __name__ == "__main__":
    main()
