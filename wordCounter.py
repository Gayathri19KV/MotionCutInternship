def count_words(text):
    """
    This function takes a string input and returns the count of words in it.
    A word is considered as a sequence of characters separated by spaces.
    """
    words = text.strip().split()  # Splitting the text into words based on spaces
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    """
    user_input = input("Enter a sentence or paragraph: ").strip()

    if not user_input:  # Handling empty input
        print("Error: No text entered. Please provide a valid input.")
        return

    word_count = count_words(user_input)  # Calling the function to count words
    print(f"Word Count: {word_count}")

if __name__ == "__main__":
    main()
