"""Wikipedia API example with exception handling."""
import wikipedia


def main():
    """Prompt for a page title, display summary and URL, handle errors."""
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break
        try:
            page = wikipedia.page(title, autosuggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following:")
            print(e.options)
        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == '__main__':
    main()
