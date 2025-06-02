# Program with a menu to handle scores and show results or stars

def main():
    score = get_score()
    option = ""

    while option != "Q":
        print("\nMenu:")
        print("(G)et a new score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        option = input(">>> ").upper()

        if option == "G":
            score = get_score()
        elif option == "P":
            print(get_result(score))
        elif option == "S":
            print("*" * int(score))
        elif option == "Q":
            print("Thanks, goodbye!")
        else:
            print("Invalid input")

def get_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Try again. Score must be 0-100.")
        score = float(input("Enter score (0-100): "))
    return score

def get_result(score):
    """Give feedback based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Okay"
    else:
        return "Bad"

main()
# Week 2 Practical Reflection

**1. What new things did you learn this week?**
I learned how to break my code into smaller functions, and how useful that is for keeping things simple.

**2. What did you find most difficult?**
At first, it was hard to figure out where to put the functions and how to pass data around. I kept getting confused about what should go inside `main()`.

**3. What part did you enjoy or think you did well in?**
I liked using random numbers and creating the menu with options. I think I did well separating the logic into different functions.

**4. What would you do differently next time?**
Next time I will write out a plan of my functions before coding. It will help me avoid mistakes.

**5. How do you feel about Git and GitHub so far?**
It’s starting to make sense. I like how I can track what I’ve done, and it saves everything in case I mess up.
