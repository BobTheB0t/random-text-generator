import random
import string

def generate_random_text(length=10, use_digits=True, use_punctuation=True):
    """
    Generates a random text string of specified length.

    Args:
        length (int): The length of the text to generate. Defaults to 10.
        use_digits (bool): Whether to include digits in the text. Defaults to True.
        use_punctuation (bool): Whether to include punctuation in the text. Defaults to True.

    Returns:
        str: A random text string of the specified length.
    """
    # Define the character sets to use
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    # Generate the random text
    random_text = ''.join(random.choice(characters) for _ in range(length))
    return random_text

def main():
    try:
        # Get user input for text length
        length = int(input("Enter the length of the text to generate (default is 10): ") or 10)
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        # Get user input for including digits and punctuation
        use_digits = input("Include digits? (y/n, default is y): ").strip().lower() != 'n'
        use_punctuation = input("Include punctuation? (y/n, default is y): ").strip().lower() != 'n'

        # Generate and print the random text
        random_text = generate_random_text(length, use_digits, use_punctuation)
        print(f"Generated text: {random_text}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()