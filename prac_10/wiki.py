import wikipedia

def fetch_wikipedia_details():
    """
    Prompt user for a page title or search phrase, fetch and display details from Wikipedia.
    """
    while True:
        query = input("Enter page title (or blank to quit): ").strip()
        if not query:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(query, autosuggest=False)
            print(f"\nTitle: {page.title}\n")
            print(f"Summary: {page.summary[:500]}...\n")
            print(f"URL: {page.url}\n")
        except wikipedia.DisambiguationError as e:
            print("DisambiguationError: Be more specific. Suggestions:")
            print(e.options)
        except wikipedia.PageError:
            print(f"PageError: No page found for '{query}'.")

if __name__ == "__main__":
    fetch_wikipedia_details()
